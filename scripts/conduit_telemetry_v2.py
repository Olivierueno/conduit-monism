#!/usr/bin/env python3
"""
CONDUIT TELEMETRY v2: Layer-Level Analysis
===========================================

The previous approach failed because averaging over 120 layers drowned out
the signal. This version analyzes each layer separately to find where
emotional encoding lives.

Key insight: Not all layers carry the same information. We need to find
which layers encode "emotion" vs "syntax" vs "semantics".

Protocol:
1. Process emotional text (grief/joy/neutral)
2. Capture state at each layer
3. Compare layer-by-layer to find discriminative layers
4. Report which layers show emotional differentiation
"""

import os
import sys
import json
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, str(Path(__file__).parent.parent))

MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_NAME = "RWKV-4-World-0.4B-v1-20230529-ctx4096.pth"
MODEL_PATH = MODEL_DIR / MODEL_NAME

OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


class LayerAnalyzer:
    """Analyze RWKV state at the layer level."""
    
    def __init__(self, model_path: Path):
        from rwkv.model import RWKV
        from rwkv.utils import PIPELINE
        
        print(f"[TELEMETRY v2] Loading model: {model_path.name}")
        self.model = RWKV(model=str(model_path), strategy='cpu fp32')
        self.pipeline = PIPELINE(self.model, "rwkv_vocab_v20230424")
        
        # Get number of layers from model
        self.n_layers = 24  # For 0.4B model
        print(f"[TELEMETRY v2] Model loaded. {self.n_layers} layers.")
    
    def get_layer_vectors(self, state) -> List[np.ndarray]:
        """Extract each layer's state as a separate vector."""
        if state is None:
            return [None] * self.n_layers
        
        # RWKV state is 5 tensors per layer
        tensors_per_layer = 5
        layer_vectors = []
        
        for layer_idx in range(self.n_layers):
            start = layer_idx * tensors_per_layer
            end = start + tensors_per_layer
            
            layer_tensors = state[start:end]
            layer_concat = []
            for t in layer_tensors:
                if hasattr(t, 'numpy'):
                    layer_concat.append(t.cpu().numpy().flatten())
                else:
                    layer_concat.append(np.array(t).flatten())
            
            layer_vectors.append(np.concatenate(layer_concat))
        
        return layer_vectors
    
    def process_text(self, text: str) -> List[np.ndarray]:
        """Process text and return final layer states."""
        tokens = self.pipeline.encode(text)
        state = None
        
        for token in tokens:
            out, state = self.model.forward([token], state)
        
        return self.get_layer_vectors(state)
    
    def compare_conditions(self, texts: Dict[str, str]) -> Dict:
        """
        Process multiple text conditions and compare layer-by-layer.
        
        Returns which layers differentiate between conditions.
        """
        print("\n" + "="*60)
        print("LAYER-LEVEL EMOTIONAL ANALYSIS")
        print("="*60)
        
        # Process each condition
        conditions = {}
        for name, text in texts.items():
            print(f"\n[PROCESSING] {name} ({len(self.pipeline.encode(text))} tokens)...")
            conditions[name] = self.process_text(text)
        
        # Compare layer-by-layer
        condition_names = list(conditions.keys())
        n_conditions = len(condition_names)
        
        print(f"\n{'Layer':<8}", end="")
        for name in condition_names:
            print(f"{name[:10]:<12}", end="")
        print("Variance")
        print("-" * (8 + 12 * n_conditions + 10))
        
        layer_variances = []
        layer_means = {name: [] for name in condition_names}
        
        for layer_idx in range(self.n_layers):
            # Get norm for each condition at this layer
            norms = {}
            for name in condition_names:
                vec = conditions[name][layer_idx]
                norm = np.linalg.norm(vec) if vec is not None else 0
                norms[name] = norm
                layer_means[name].append(norm)
            
            # Calculate variance across conditions
            norm_values = list(norms.values())
            variance = np.var(norm_values) / (np.mean(norm_values) + 1e-10)  # Normalized variance
            layer_variances.append(variance)
            
            # Print row
            print(f"{layer_idx:<8}", end="")
            for name in condition_names:
                print(f"{norms[name]:>10.0f}  ", end="")
            print(f"{variance:.4f}")
        
        # Find most discriminative layers
        sorted_layers = np.argsort(layer_variances)[::-1]
        
        print("\n" + "="*60)
        print("MOST DISCRIMINATIVE LAYERS (by variance)")
        print("="*60)
        
        for i, layer_idx in enumerate(sorted_layers[:5]):
            print(f"  #{i+1}: Layer {layer_idx} (variance = {layer_variances[layer_idx]:.4f})")
        
        # Compute pairwise similarities at discriminative layers
        print("\n" + "="*60)
        print("PAIRWISE LAYER SIMILARITY (top discriminative layer)")
        print("="*60)
        
        top_layer = sorted_layers[0]
        print(f"\nLayer {top_layer} cosine similarities:")
        
        for i, name1 in enumerate(condition_names):
            for name2 in condition_names[i+1:]:
                vec1 = conditions[name1][top_layer]
                vec2 = conditions[name2][top_layer]
                
                if vec1 is not None and vec2 is not None:
                    norm1, norm2 = np.linalg.norm(vec1), np.linalg.norm(vec2)
                    if norm1 > 0 and norm2 > 0:
                        cos_sim = np.dot(vec1, vec2) / (norm1 * norm2)
                        print(f"  {name1} vs {name2}: {cos_sim:.4f}")
        
        return {
            "layer_variances": layer_variances,
            "discriminative_layers": sorted_layers[:5].tolist(),
            "layer_means": layer_means
        }


def main():
    print("\n" + "="*60)
    print("CONDUIT TELEMETRY v2: LAYER-LEVEL ANALYSIS")
    print("="*60)
    
    if not MODEL_PATH.exists():
        print(f"ERROR: Model not found at {MODEL_PATH}")
        return
    
    analyzer = LayerAnalyzer(MODEL_PATH)
    
    texts = {
        "neutral": """
        The weather today is partly cloudy with temperatures around 65 degrees.
        Traffic on the highway is moving normally. The stock market opened flat.
        """,
        "grief": """
        I am experiencing profound grief. My heart is heavy with loss.
        The weight of sorrow presses down on me. I feel the absence of what was once here.
        Tears flow as I process this pain. The world seems dimmer.
        """,
        "joy": """
        I am filled with pure joy and happiness! Everything is wonderful!
        The world is bright and beautiful. I feel light, energetic, alive!
        Laughter bubbles up from within me. Every moment is a gift.
        """
    }
    
    results = analyzer.compare_conditions(texts)
    
    # Save results
    output = {
        "timestamp": datetime.now().isoformat(),
        "model": MODEL_NAME,
        "results": results
    }
    
    output_file = OUTPUT_DIR / f"conduit_telemetry_v2_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n[SAVED] {output_file}")


if __name__ == "__main__":
    main()
