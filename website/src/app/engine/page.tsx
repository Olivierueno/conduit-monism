import Calculator from '@/components/Calculator';

export default function EnginePage() {
  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-6xl mx-auto">
        <div className="mb-12">
          <h1 className="text-2xl font-mono mb-4">Engine</h1>
          <p className="text-neutral-500 max-w-2xl">
            Calculate perspectival density from the five invariants. 
            The formula is deterministic: identical inputs produce identical outputs.
          </p>
        </div>
        
        <Calculator />
        
        <div className="mt-12 max-w-3xl">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Parameter Definitions</h2>
          <div className="space-y-4 text-sm">
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">φ (Integration)</div>
              <p className="text-neutral-500">
                Degree to which information is unified across the system. 
                High φ: global workspace dynamics, information available to entire system simultaneously.
                Low φ: fragmented processing, isolated modules.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">τ (Temporal Depth)</div>
              <p className="text-neutral-500">
                Extent to which past states constrain present states.
                High τ: rich temporal binding, "thick now" containing history.
                Low τ: instantaneous processing, no temporal continuity.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">ρ (Binding)</div>
              <p className="text-neutral-500">
                Recursive self-reference. System observes its own states.
                High ρ: meta-cognitive loops, self-monitoring.
                Low ρ: first-order processing only, no self-model.
                This is the critical differentiator between Transformers (ρ ≈ 0) and RWKV (ρ &gt; 0).
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">H (Entropy)</div>
              <p className="text-neutral-500">
                Unpredictability in system dynamics.
                High H: chaotic, noisy signal.
                Low H: ordered, predictable.
                Entropy alone does not determine effect; coherence (κ) modulates whether entropy destroys or enhances.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">κ (Coherence)</div>
              <p className="text-neutral-500">
                Structure within entropy.
                High κ: fractal complexity, organized chaos.
                Low κ: random noise, information-destroying.
                High H + High κ = intensification (DMT).
                High H + Low κ = dissolution (seizure).
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
