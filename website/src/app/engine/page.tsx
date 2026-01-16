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

        {/* Methodology: How Values Were Calculated */}
        <div className="mt-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Methodology: How Animal & State Values Were Calculated</h2>
          
          <div className="p-4 border border-neutral-800 bg-neutral-900/50 mb-4">
            <p className="text-sm text-neutral-400 mb-4">
              <strong className="text-neutral-300">Important:</strong> The values for animals and states in this engine are <strong>estimates</strong> based on comparative neuroscience literature. They are <strong>NOT direct measurements</strong>. The framework provides a way to think about consciousness structurally, but assigning precise values requires assumptions about how neural properties map to the five invariants.
            </p>
            <p className="text-sm text-neutral-500">
              These estimates should be treated as <strong>hypotheses, not facts</strong>. They are useful for exploring the framework's predictions, but should not be taken as definitive measurements of consciousness.
            </p>
          </div>

          <div className="space-y-4 text-sm">
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-3">φ (Integration) - Estimation Method</div>
              <p className="text-neutral-500 mb-2">
                Based on brain connectivity studies, EEG coherence measurements, and anatomical integration evidence.
              </p>
              <ul className="text-neutral-500 text-xs space-y-1 ml-4 list-disc">
                <li>Presence and size of corpus callosum (interhemispheric integration)</li>
                <li>Global workspace connectivity patterns</li>
                <li>EEG coherence across brain regions</li>
                <li>Information integration capacity (IIT-inspired measures)</li>
              </ul>
              <p className="text-neutral-600 text-xs mt-3 font-mono">
                Example: Humans (φ=0.85) - high integration via large corpus callosum and global workspace. C. elegans (φ=0.05) - minimal integration, 302 neurons with simple reflex pathways.
              </p>
            </div>

            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-3">τ (Temporal Depth) - Estimation Method</div>
              <p className="text-neutral-500 mb-2">
                Based on working memory studies, episodic memory evidence, and temporal binding window research.
              </p>
              <ul className="text-neutral-500 text-xs space-y-1 ml-4 list-disc">
                <li>Working memory capacity and duration</li>
                <li>Episodic memory formation and recall</li>
                <li>Temporal binding window (how far back influences present)</li>
                <li>Evidence of "mental time travel" (past/future simulation)</li>
              </ul>
              <p className="text-neutral-600 text-xs mt-3 font-mono">
                Example: Humans (τ=0.8) - rich autobiographical memory, decades of temporal depth. Fruit fly (τ=0.05) - minimal temporal binding, primarily reactive.
              </p>
            </div>

            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-3">ρ (Binding) - Estimation Method</div>
              <p className="text-neutral-500 mb-2">
                Based on self-recognition tests (mirror test), metacognition studies, and evidence of self-monitoring behavior.
              </p>
              <ul className="text-neutral-500 text-xs space-y-1 ml-4 list-disc">
                <li>Mirror self-recognition test results</li>
                <li>Metacognitive awareness (knowing what you know)</li>
                <li>Self-monitoring and error detection</li>
                <li>Re-entrant neural pathways (thalamocortical loops)</li>
                <li>For AI: Amnesia Test results (RWKV vs Transformers)</li>
              </ul>
              <p className="text-neutral-600 text-xs mt-3 font-mono">
                Example: Chimpanzee (ρ=0.6) - passes mirror test, shows metacognition. Transformer (ρ=0.0) - no persistent state, fails Amnesia Test. RWKV (ρ=0.3) - passes Amnesia Test, maintains hidden state.
              </p>
            </div>

            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-3">H (Entropy) - Estimation Method</div>
              <p className="text-neutral-500 mb-2">
                Based on neural variability studies and behavioral predictability (lower for more stereotyped behavior).
              </p>
              <ul className="text-neutral-500 text-xs space-y-1 ml-4 list-disc">
                <li>Neural signal variability (Lempel-Ziv complexity)</li>
                <li>Behavioral predictability vs. flexibility</li>
                <li>Response diversity to similar stimuli</li>
                <li>EEG spectral entropy measurements</li>
              </ul>
              <p className="text-neutral-600 text-xs mt-3 font-mono">
                Example: Human awake (H=0.35) - moderate entropy, flexible responses. Deep sleep (H=0.1) - very low entropy, minimal variability. Panic attack (H=0.9) - extreme entropy, chaotic neural activity.
              </p>
            </div>

            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-3">κ (Coherence) - Estimation Method</div>
              <p className="text-neutral-500 mb-2">
                Based on neural synchronization studies and evidence of structured vs. random neural activity.
              </p>
              <ul className="text-neutral-500 text-xs space-y-1 ml-4 list-disc">
                <li>Phase-locking value across frequency bands</li>
                <li>Mutual information structure between brain regions</li>
                <li>Fractal dimension of neural dynamics</li>
                <li>Pattern vs. randomness in high-entropy states</li>
              </ul>
              <p className="text-neutral-600 text-xs mt-3 font-mono">
                Example: DMT breakthrough (H=0.95, κ=0.9) - high entropy but highly structured, "more real than real". Seizure (H=0.95, κ=0.1) - high entropy but random, information-destroying chaos.
              </p>
            </div>
          </div>

          <div className="mt-6 p-4 border border-neutral-800 bg-neutral-900/50">
            <div className="font-mono text-neutral-300 mb-2 text-sm">Key References</div>
            <ul className="text-xs text-neutral-500 space-y-1">
              <li>• Edelman & Seth (2009) - Animal consciousness</li>
              <li>• Barron & Klein (2016) - Insect consciousness</li>
              <li>• Birch et al. (2020) - Invertebrate sentience</li>
              <li>• Boly et al. (2013) - Neural correlates of consciousness</li>
              <li>• Tononi & Koch (2015) - Integrated Information Theory</li>
            </ul>
            <p className="text-xs text-neutral-600 mt-3">
              For detailed methodology, see the comments in <code className="text-neutral-500">website/src/lib/engine.ts</code>
            </p>
          </div>

          <div className="mt-6 p-4 border border-yellow-900/50 bg-yellow-950/10">
            <p className="text-sm text-yellow-400/80 mb-2">
              <strong>Limitations & Caveats:</strong>
            </p>
            <ul className="text-xs text-yellow-500/70 space-y-1 ml-4 list-disc">
              <li>These are cross-species estimates based on limited comparative data</li>
              <li>Different species may have different neural architectures that map differently to the invariants</li>
              <li>Within-species variation is significant (individual differences)</li>
              <li>Some values (especially κ) are particularly difficult to estimate</li>
              <li>AI architecture values are based on structural analysis, not behavioral testing</li>
            </ul>
          </div>
        </div>
      </div>
    </main>
  );
}
