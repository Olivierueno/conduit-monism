import Calculator from '@/components/Calculator';
import Link from 'next/link';

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

          <div className="p-4 border border-neutral-800 bg-neutral-900/50 mb-4">
            <p className="text-sm text-neutral-400 mb-2">
              <strong className="text-neutral-300">Important:</strong> The values for animals and states in this engine are <strong>estimates</strong> based on comparative neuroscience literature. They are <strong>NOT direct measurements</strong>.
            </p>
            <p className="text-sm text-neutral-500">
              These estimates should be treated as <strong>hypotheses, not facts</strong>. They are useful for exploring the framework's predictions, but should not be taken as definitive measurements of consciousness.
            </p>
          </div>

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
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2 mb-2">
                <strong>Measurement proxy:</strong> Global Efficiency (E_glob) + PCI + ISD — MODERATE-HIGH confidence
              </div>
              <div className="text-xs text-neutral-600">
                <strong>Estimation basis:</strong> Multi-metric approach validated by 4 independent AI reviews (AT11). Rank-order preserved across 5+ consciousness states. Hyper-integrated states (Jhana, psychedelics) exceed baseline wakefulness.
              </div>
              <p className="text-neutral-600 text-xs mt-2 font-mono">
                Calibrated: Human wakefulness (φ=0.80). C. elegans (φ=0.05) via 302 neurons with simple reflex pathways.
              </p>
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
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2 mb-2">
                <strong>Measurement proxy:</strong> Temporal integration window; decay rate of mutual information — MODERATE confidence
              </div>
              <div className="text-xs text-neutral-600">
                <strong>Estimation basis:</strong> Working memory capacity, episodic memory evidence, temporal binding window research.
              </div>
              <p className="text-neutral-600 text-xs mt-2 font-mono">
                Calibrated: Human wakefulness (τ=0.75). Fruit fly (τ=0.05) via primarily reactive behavior.
              </p>
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
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2 mb-2">
                <strong>Measurement proxy:</strong> Perturbational Complexity Index (PCI*) via TMS-EEG — HIGH confidence
              </div>
              <div className="text-xs text-neutral-600">
                <strong>Estimation basis:</strong> PCI threshold of 0.31 separates conscious from unconscious states with 100% accuracy (Casali et al., 2013). Grounded in re-entrant connectivity and recursive self-observation.
              </div>
              <p className="text-neutral-600 text-xs mt-2 font-mono">
                Calibrated: Human wakefulness (ρ=0.65). PCI* ≥ 0.31 → conscious. Non-biological systems (ρ=0) → no recursive self-observer.
              </p>
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
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2 mb-2">
                <strong>Measurement proxy:</strong> Lempel-Ziv complexity (LZc) — HIGH confidence
              </div>
              <div className="text-xs text-neutral-600">
                <strong>Estimation basis:</strong> Neural signal variability, behavioral predictability, EEG spectral entropy. Well-validated in altered states research.
              </div>
              <p className="text-neutral-600 text-xs mt-2 font-mono">
                Calibrated: Human wakefulness (H=0.50). Propofol anesthesia (H=0.15). DMT peak (H=0.70).
              </p>
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
              <div className="text-xs text-neutral-600 border-t border-neutral-800 pt-2 mt-2 mb-2">
                <strong>Measurement proxy:</strong> Multi-scale entropy slope (MSE) — MODERATE confidence (AT07 validated, r=0.987)
              </div>
              <div className="text-xs text-neutral-600">
                <strong>Estimation basis:</strong> Fractal signals maintain complexity across timescales (Costa 2002, 2005). Flat MSE slope = fractal = high κ.
              </div>
              <p className="text-neutral-600 text-xs mt-2 font-mono">
                Calibrated: DMT (H=0.70, κ=0.90) structured chaos. Seizure (H=0.85, κ=0.15) random chaos.
              </p>
            </div>
          </div>

          <div className="mt-6 p-4 border border-blue-900/50 bg-blue-950/10">
            <div className="font-mono text-neutral-300 mb-2 text-sm">Empirical Calibration</div>
            <p className="text-xs text-neutral-500 mb-2">
              These values are grounded in peer-reviewed neuroscience literature. Confidence levels indicate measurement reliability:
            </p>
            <ul className="text-xs text-neutral-500 space-y-1 mb-3">
              <li>• <strong>HIGH:</strong> ρ ↔ PCI*, H ↔ LZc (robust empirical validation)</li>
              <li>• <strong>MODERATE-HIGH:</strong> φ ↔ E_glob + PCI + ISD (AT11 extended validation, 4/4 AI support)</li>
              <li>• <strong>MODERATE:</strong> τ ↔ Temporal Integration Window, κ ↔ MSE slope (AT07 validated)</li>
            </ul>
            <Link href="/calibration" className="text-xs text-blue-400 hover:text-blue-300 transition-colors">
              → View full calibration methodology and state comparisons
            </Link>
          </div>

          <div className="mt-4 p-4 border border-neutral-800 bg-neutral-900/50">
            <div className="font-mono text-neutral-300 mb-2 text-sm">Key References</div>
            <ul className="text-xs text-neutral-500 space-y-1">
              <li>• Casali et al. (2013) - PCI threshold for consciousness</li>
              <li>• Schartner et al. (2017) - LZc in altered states</li>
              <li>• Costa et al. (2002, 2005) - Multi-Scale Entropy</li>
              <li>• Edelman & Seth (2009) - Animal consciousness</li>
              <li>• Tononi & Koch (2015) - Integrated Information Theory</li>
            </ul>
          </div>

          <div className="mt-4 p-4 border border-yellow-900/50 bg-yellow-950/10">
            <p className="text-sm text-yellow-400/80 mb-2">
              <strong>Limitations & Caveats:</strong>
            </p>
            <ul className="text-xs text-yellow-500/70 space-y-1 ml-4 list-disc">
              <li>Cross-species estimates based on limited comparative data</li>
              <li>Different species may map differently to the invariants</li>
              <li>Within-species variation is significant</li>
              <li>Formula predicts structural MAGNITUDE, not VALENCE (positive vs negative experience)</li>
              <li>AI architecture values are based on structural analysis, not behavioral testing</li>
            </ul>
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
