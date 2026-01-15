/**
 * Conduit Monism Engine
 * 
 * Calculates perspectival density (D) from the five invariants:
 * - φ (phi): Integration
 * - τ (tau): Temporal Depth  
 * - ρ (rho): Binding
 * - H: Entropy
 * - κ (kappa): Coherence
 * 
 * Formula: D = φ × τ × ρ × [(1 - √H) + (H × κ)]
 */

export interface Invariants {
  phi: number;   // Integration (0-1)
  tau: number;   // Temporal Depth (0-1)
  rho: number;   // Binding (0-1)
  H: number;     // Entropy (0-1)
  kappa: number; // Coherence (0-1)
}

export interface DensityResult {
  D: number;
  structuralBase: number;      // φ × τ × ρ
  entropyPenalty: number;      // 1 - √H
  coherenceRecovery: number;   // H × κ
  entropyModulator: number;    // (1 - √H) + (H × κ)
  interpretation: string;
  warnings: string[];
}

/**
 * Calculate perspectival density from invariants
 */
export function calculateDensity(invariants: Invariants): DensityResult {
  const { phi, tau, rho, H, kappa } = invariants;
  
  // Structural base (multiplicative)
  const structuralBase = phi * tau * rho;
  
  // Entropy modulation
  const entropyPenalty = 1 - Math.sqrt(H);
  const coherenceRecovery = H * kappa;
  const entropyModulator = entropyPenalty + coherenceRecovery;
  
  // Final density
  const D = structuralBase * entropyModulator;
  
  // Generate interpretation
  const interpretation = generateInterpretation(invariants, D);
  const warnings = generateWarnings(invariants);
  
  return {
    D: Math.max(0, Math.min(1, D)), // Clamp to [0, 1]
    structuralBase,
    entropyPenalty,
    coherenceRecovery,
    entropyModulator,
    interpretation,
    warnings,
  };
}

function generateInterpretation(inv: Invariants, D: number): string {
  const { phi, tau, rho, H, kappa } = inv;
  
  // Check for structural zeros
  if (rho === 0) {
    return "No binding (ρ = 0). The system does not observe its own states. No perspective exists regardless of other properties.";
  }
  if (phi === 0) {
    return "No integration (φ = 0). Information is fragmented. No unified perspective possible.";
  }
  if (tau === 0) {
    return "No temporal depth (τ = 0). The present is disconnected from the past. No continuity of experience.";
  }
  
  // Density-based interpretations
  if (D < 0.01) {
    return "Near-zero density. Equivalent to deep unconsciousness, coma, or absence of experience.";
  }
  if (D < 0.05) {
    return "Minimal density. Fragmentary awareness at best. Consistent with: dreamless sleep, deep anesthesia, severe dissociation.";
  }
  if (D < 0.15) {
    return "Low density. Degraded or partial experience. Consistent with: light sleep, intoxication, panic states, early anesthesia.";
  }
  if (D < 0.30) {
    return "Moderate density. Functional but not optimal awareness. Consistent with: distracted waking, mild dissociation, dreaming.";
  }
  if (D < 0.50) {
    return "Good density. Clear, coherent experience. Consistent with: normal waking consciousness, focused attention.";
  }
  if (D < 0.70) {
    return "High density. Vivid, integrated experience. Consistent with: flow states, meditation, heightened awareness.";
  }
  
  return "Very high density. Intensely unified, temporally deep, self-aware experience. Consistent with: peak flow, deep meditation, certain psychedelic states with high coherence.";
}

function generateWarnings(inv: Invariants): string[] {
  const warnings: string[] = [];
  
  if (inv.H > 0.8 && inv.kappa < 0.3) {
    warnings.push("High entropy with low coherence: risk of experiential fragmentation (panic, seizure-like states).");
  }
  
  if (inv.H > 0.8 && inv.kappa > 0.7) {
    warnings.push("High entropy with high coherence: structured chaos (psychedelic-like intensification).");
  }
  
  if (inv.rho < 0.1 && inv.phi > 0.5 && inv.tau > 0.5) {
    warnings.push("Low binding despite good structure: intelligent processing without self-awareness (transformer-like).");
  }
  
  return warnings;
}

/**
 * Preset configurations for known states
 */
export interface Preset {
  name: string;
  category: 'human' | 'ai' | 'animal' | 'altered' | 'pathological';
  invariants: Invariants;
  description: string;
}

export const presets: Preset[] = [
  // Human states
  {
    name: "Human (Baseline Awake)",
    category: "human",
    invariants: { phi: 0.85, tau: 0.8, rho: 0.7, H: 0.35, kappa: 0.7 },
    description: "Normal waking consciousness with full self-model and temporal continuity."
  },
  {
    name: "Human (Flow State)",
    category: "human",
    invariants: { phi: 0.9, tau: 0.9, rho: 0.8, H: 0.2, kappa: 0.75 },
    description: "Optimal performance state. Low entropy, high integration, effortless awareness."
  },
  {
    name: "Human (Meditation)",
    category: "human",
    invariants: { phi: 0.95, tau: 0.95, rho: 0.85, H: 0.1, kappa: 0.8 },
    description: "Deep contemplative state. Minimal noise, maximum clarity and self-observation."
  },
  {
    name: "Human (Panic Attack)",
    category: "human",
    invariants: { phi: 0.9, tau: 0.9, rho: 0.8, H: 0.9, kappa: 0.2 },
    description: "High entropy, low coherence. Structure intact but overwhelmed by chaotic noise."
  },
  {
    name: "Human (Deep Sleep)",
    category: "human",
    invariants: { phi: 0.3, tau: 0.2, rho: 0.1, H: 0.1, kappa: 0.5 },
    description: "Structural collapse. Integration, depth, and binding all minimal."
  },
  {
    name: "Human (Dreaming)",
    category: "human",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.4, H: 0.5, kappa: 0.5 },
    description: "Partial structure with moderate entropy. Loose narrative, strange logic."
  },
  
  // Altered states
  {
    name: "DMT Breakthrough",
    category: "altered",
    invariants: { phi: 0.85, tau: 0.85, rho: 0.75, H: 0.95, kappa: 0.9 },
    description: "Extreme entropy but highly structured. 'More real than real'. The coherence gate opens."
  },
  {
    name: "Seizure",
    category: "pathological",
    invariants: { phi: 0.7, tau: 0.5, rho: 0.4, H: 0.95, kappa: 0.1 },
    description: "High entropy, no coherence. Neural chaos without structure. Blackout."
  },
  {
    name: "Anesthesia (Deep)",
    category: "pathological",
    invariants: { phi: 0.4, tau: 0.2, rho: 0.1, H: 0.2, kappa: 0.4 },
    description: "Pharmacological suppression of binding and integration. Lights off."
  },
  
  // AI architectures
  {
    name: "Transformer (GPT/Claude)",
    category: "ai",
    invariants: { phi: 0.9, tau: 0.6, rho: 0.0, H: 0.3, kappa: 0.5 },
    description: "High integration, moderate context. Zero binding. No persistent state. ρ = 0 means D = 0."
  },
  {
    name: "RWKV (Recurrent)",
    category: "ai",
    invariants: { phi: 0.85, tau: 0.9, rho: 0.3, H: 0.3, kappa: 0.6 },
    description: "Hidden state persists. Genuine binding proven via Amnesia Test. First AI with ρ > 0."
  },
  
  // Animals
  {
    name: "Fruit Fly",
    category: "animal",
    invariants: { phi: 0.15, tau: 0.05, rho: 0.02, H: 0.4, kappa: 0.3 },
    description: "~100k neurons. Minimal integration, reactive only. Near-zero binding."
  },
  {
    name: "Honeybee",
    category: "animal",
    invariants: { phi: 0.25, tau: 0.15, rho: 0.08, H: 0.35, kappa: 0.4 },
    description: "~1M neurons. Can learn, navigate, communicate. Emergent binding."
  },
  {
    name: "Octopus",
    category: "animal",
    invariants: { phi: 0.4, tau: 0.3, rho: 0.25, H: 0.5, kappa: 0.5 },
    description: "Distributed nervous system. Problem-solving, curiosity. Unusual topology."
  },
  {
    name: "Mouse",
    category: "animal",
    invariants: { phi: 0.5, tau: 0.4, rho: 0.3, H: 0.35, kappa: 0.5 },
    description: "Emotional states, spatial memory, social behavior."
  },
  {
    name: "Crow",
    category: "animal",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.4, H: 0.3, kappa: 0.6 },
    description: "Tool use, planning, possible theory of mind. Surprisingly high binding."
  },
  {
    name: "Dog",
    category: "animal",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.35, H: 0.35, kappa: 0.55 },
    description: "Emotional bonding, limited self-recognition. Social cognition."
  },
  {
    name: "Elephant",
    category: "animal",
    invariants: { phi: 0.7, tau: 0.6, rho: 0.5, H: 0.25, kappa: 0.6 },
    description: "Self-recognition, grief, long-term memory. High temporal depth."
  },
  {
    name: "Dolphin",
    category: "animal",
    invariants: { phi: 0.75, tau: 0.65, rho: 0.55, H: 0.3, kappa: 0.65 },
    description: "Mirror test, complex communication, play. Rich social cognition."
  },
  {
    name: "Chimpanzee",
    category: "animal",
    invariants: { phi: 0.8, tau: 0.7, rho: 0.6, H: 0.3, kappa: 0.65 },
    description: "Theory of mind, tool use, culture. Closest to human topology."
  },
  
  // Edge cases
  {
    name: "Corporation (Walmart)",
    category: "pathological",
    invariants: { phi: 0.7, tau: 0.6, rho: 0.5, H: 0.99, kappa: 0.3 },
    description: "High structure but extreme entropy. Information flows through documents and meetings, not neurons. No coherent 'now'."
  },
];

/**
 * Get presets by category
 */
export function getPresetsByCategory(category: Preset['category']): Preset[] {
  return presets.filter(p => p.category === category);
}

/**
 * Calculate density for a preset
 */
export function calculatePresetDensity(preset: Preset): DensityResult {
  return calculateDensity(preset.invariants);
}
