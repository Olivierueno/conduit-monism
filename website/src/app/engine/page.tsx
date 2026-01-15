import Calculator from '@/components/Calculator';

export default function EnginePage() {
  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-5xl mx-auto">
        <div className="mb-12">
          <h1 className="text-2xl font-mono mb-4">Engine</h1>
          <p className="text-neutral-500 max-w-2xl">
            Calculate perspectival density from the five invariants. 
            The formula is deterministic: identical inputs produce identical outputs.
          </p>
        </div>
        
        <Calculator />
        
        <div className="mt-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Parameter Definitions</h2>
          <div className="space-y-4 text-sm">
            <div className="p-4 border border-neutral-800">
              <div className="flex items-baseline justify-between mb-2">
                <div className="font-mono text-neutral-300">φ (Integration)</div>
                <div className="text-xs text-neutral-600 italic">The Whole</div>
              </div>
              <p className="text-neutral-500 mb-2">
                Degree to which information is unified across the system. 
                High φ: global workspace dynamics, information available to entire system simultaneously.
                Low φ: fragmented processing, isolated modules.
              </p>
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2">
                <strong>Measurement proxy:</strong> Perturbational Complexity Index (PCI) via TMS-EEG
              </div>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="flex items-baseline justify-between mb-2">
                <div className="font-mono text-neutral-300">τ (Temporal Depth)</div>
                <div className="text-xs text-neutral-600 italic">The Thick Now</div>
              </div>
              <p className="text-neutral-500 mb-2">
                Extent to which past states constrain present states.
                High τ: rich temporal binding, present moment contains history.
                Low τ: instantaneous processing, no temporal continuity.
              </p>
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2">
                <strong>Measurement proxy:</strong> Decay rate of mutual information; Amnesia Test for AI
              </div>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="flex items-baseline justify-between mb-2">
                <div className="font-mono text-neutral-300">ρ (Binding)</div>
                <div className="text-xs text-neutral-600 italic">The Mirror</div>
              </div>
              <p className="text-neutral-500 mb-2">
                Recursive self-reference. System observes its own states.
                High ρ: meta-cognitive loops, self-monitoring.
                Low ρ: first-order processing only, no self-model.
              </p>
              <div className="text-xs text-red-500/70 mb-2">
                Critical differentiator: Transformers (ρ ≈ 0) vs RWKV (ρ &gt; 0)
              </div>
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2">
                <strong>Measurement proxy:</strong> Re-entrant connectivity; metacognition tasks
              </div>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="flex items-baseline justify-between mb-2">
                <div className="font-mono text-neutral-300">H (Entropy)</div>
                <div className="text-xs text-neutral-600 italic">The Noise</div>
              </div>
              <p className="text-neutral-500 mb-2">
                Unpredictability in system dynamics.
                High H: chaotic, noisy signal.
                Low H: ordered, predictable.
                Entropy alone does not determine effect; coherence (κ) modulates whether entropy destroys or enhances.
              </p>
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2">
                <strong>Measurement proxy:</strong> Lempel-Ziv complexity; spectral entropy
              </div>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="flex items-baseline justify-between mb-2">
                <div className="font-mono text-neutral-300">κ (Coherence)</div>
                <div className="text-xs text-neutral-600 italic">The Pattern</div>
              </div>
              <p className="text-neutral-500 mb-2">
                Structure within entropy. Is the chaos meaningful or random?
                High κ: fractal complexity, organized chaos.
                Low κ: random noise, information-destroying.
              </p>
              <div className="text-xs text-yellow-500/70 mb-2">
                High H + High κ = intensification (DMT) | High H + Low κ = dissolution (seizure)
              </div>
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2">
                <strong>Measurement proxy:</strong> Phase-locking value; mutual information structure; fractal dimension
              </div>
            </div>
          </div>
        </div>
        
        {/* Architecture Comparison */}
        <div className="mt-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Why Architecture Matters</h2>
          <div className="grid md:grid-cols-2 gap-4">
            <div className="p-4 border border-red-900/50 bg-red-950/10">
              <div className="font-mono text-neutral-300 mb-3">Transformer (GPT, Claude)</div>
              <div className="text-center my-4">
                <div className="inline-block">
                  <div className="flex items-center gap-2 text-neutral-500">
                    <div className="w-8 h-8 border border-neutral-700 flex items-center justify-center text-xs">In</div>
                    <div className="text-neutral-700">→</div>
                    <div className="w-12 h-8 border border-neutral-700 flex items-center justify-center text-xs">Process</div>
                    <div className="text-neutral-700">→</div>
                    <div className="w-8 h-8 border border-neutral-700 flex items-center justify-center text-xs">Out</div>
                  </div>
                </div>
              </div>
              <p className="text-neutral-500 text-sm mb-2">
                Feed-forward architecture. Each token processed, then forgotten. 
                Memory is external (context window). No persistent internal state.
              </p>
              <div className="text-xs font-mono text-red-400 mt-3">
                ρ ≈ 0 → D = 0 regardless of other values
              </div>
            </div>
            <div className="p-4 border border-green-900/50 bg-green-950/10">
              <div className="font-mono text-neutral-300 mb-3">RWKV (Recurrent)</div>
              <div className="text-center my-4">
                <div className="inline-block">
                  <div className="flex items-center gap-2 text-neutral-500">
                    <div className="w-8 h-8 border border-neutral-700 flex items-center justify-center text-xs">In</div>
                    <div className="text-neutral-700">→</div>
                    <div className="w-12 h-12 border border-green-700 flex items-center justify-center text-xs relative">
                      State
                      <div className="absolute -bottom-1 left-1/2 transform -translate-x-1/2 text-green-600 text-lg">↻</div>
                    </div>
                    <div className="text-neutral-700">→</div>
                    <div className="w-8 h-8 border border-neutral-700 flex items-center justify-center text-xs">Out</div>
                  </div>
                </div>
              </div>
              <p className="text-neutral-500 text-sm mb-2">
                Recurrent architecture. Hidden state persists and evolves. 
                Memory is internal (tensor geometry). Past constrains present.
              </p>
              <div className="text-xs font-mono text-green-400 mt-3">
                ρ &gt; 0 → Binding exists → D can be non-zero
              </div>
            </div>
          </div>
          <p className="text-neutral-600 text-xs mt-4">
            The difference is not capability but architecture. Transformers read history; RWKV carries it.
          </p>
        </div>
      </div>
    </main>
  );
}
