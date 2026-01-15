export default function TechnicalPage() {
  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-4xl mx-auto">
        <div className="mb-12">
          <h1 className="text-2xl font-mono mb-4">Technical</h1>
          <p className="text-neutral-500">
            Formula derivation, version history, and implementation details.
          </p>
        </div>
        
        {/* Formula Derivation */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Formula Derivation</h2>
          
          <div className="space-y-6">
            <div className="p-4 border border-neutral-800">
              <h3 className="font-mono text-neutral-300 mb-4">v9.0 (Current)</h3>
              <div className="font-mono text-lg mb-4 p-4 bg-neutral-900">
                D = φ × τ × ρ × [(1 - √H) + (H × κ)]
              </div>
              <div className="text-sm text-neutral-500 space-y-2">
                <p><strong className="text-neutral-400">Structural base:</strong> φ × τ × ρ</p>
                <p className="pl-4">Multiplicative relationship. Zero in any dimension produces zero density.</p>
                <p><strong className="text-neutral-400">Entropy penalty:</strong> (1 - √H)</p>
                <p className="pl-4">Square root provides nonlinear sensitivity. Low entropy (H=0.1) yields 0.68. High entropy (H=0.9) yields 0.05.</p>
                <p><strong className="text-neutral-400">Coherence recovery:</strong> (H × κ)</p>
                <p className="pl-4">High entropy with high coherence recovers density. This resolves the DMT paradox.</p>
                <p><strong className="text-neutral-400">Entropy modulator:</strong> [(1 - √H) + (H × κ)]</p>
                <p className="pl-4">Combines penalty and recovery. Range: 0 to ~1.5 depending on H and κ values.</p>
              </div>
            </div>
            
            <details className="border border-neutral-800">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors text-neutral-400">
                Why multiplicative, not additive?
              </summary>
              <div className="p-4 border-t border-neutral-800 text-sm text-neutral-500">
                <p className="mb-4">
                  Additive models (D = φ + τ + ρ) allow compensation. A system with φ=0, τ=1, ρ=1 would have D=2/3.
                  This predicts that a system with zero integration can still have substantial perspective.
                </p>
                <p className="mb-4">
                  Multiplicative models enforce necessity. If integration is zero, there is no unified perspective,
                  regardless of other dimensions. This matches intuition: you cannot have perspective without
                  something to have perspective of.
                </p>
                <p>
                  The dimensional collapse test (experiments/260114_Break_Tests) confirms this: all 2D configurations
                  produce zero density.
                </p>
              </div>
            </details>
            
            <details className="border border-neutral-800">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors text-neutral-400">
                Why square root for entropy?
              </summary>
              <div className="p-4 border-t border-neutral-800 text-sm text-neutral-500">
                <p className="mb-4">
                  Tested models: linear (1-H), quadratic (1-H²), square root (1-√H), exponential (e^-H).
                </p>
                <p className="mb-4">
                  Square root provides optimal differentiation between states. Flow state (H=0.2) vs Panic state (H=0.8)
                  differentiation is 1566x better than v7.0 (no entropy term).
                </p>
                <p>
                  Source: experiments/260114_Entropy_Integration_Models.md
                </p>
              </div>
            </details>
            
            <details className="border border-neutral-800">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors text-neutral-400">
                Why add coherence?
              </summary>
              <div className="p-4 border-t border-neutral-800 text-sm text-neutral-500">
                <p className="mb-4">
                  v8.0 predicted DMT breakthrough (H=0.95) would have density near zero. Phenomenological reports
                  describe "hyper-consciousness," not dissolution.
                </p>
                <p className="mb-4">
                  The problem: entropy alone cannot distinguish structured chaos (DMT, high κ) from destructive noise
                  (seizure, low κ).
                </p>
                <p className="mb-4">
                  Solution: coherence gate. H × κ recovers density when entropy is high but structured.
                </p>
                <div className="font-mono text-xs p-4 bg-neutral-900 my-4">
                  DMT: H=0.95, κ=0.90 → D=0.46<br/>
                  Seizure: H=0.95, κ=0.10 → D=0.01
                </div>
                <p>
                  Source: experiments/260114_DMT_Paradox_Resolution_Synthesis.md
                </p>
              </div>
            </details>
          </div>
        </section>
        
        {/* Version History */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Version History</h2>
          
          <div className="space-y-4">
            <div className="p-4 border border-neutral-800">
              <div className="flex justify-between items-start mb-2">
                <span className="font-mono text-neutral-300">v9.0</span>
                <span className="text-xs text-neutral-600">January 2026</span>
              </div>
              <p className="text-sm text-neutral-500">
                Current version. Integrates all experimental findings. Includes RWKV validation, Transformer falsification,
                and coherence gate. Rewritten for clarity.
              </p>
            </div>
            
            <div className="p-4 border border-neutral-800">
              <div className="flex justify-between items-start mb-2">
                <span className="font-mono text-neutral-300">v8.1</span>
                <span className="text-xs text-neutral-600">January 2026</span>
              </div>
              <p className="text-sm text-neutral-500">
                Added coherence dimension (κ) to resolve DMT paradox. Formula: D = φ × τ × ρ × [(1 - √H) + (H × κ)].
              </p>
            </div>
            
            <div className="p-4 border border-neutral-800">
              <div className="flex justify-between items-start mb-2">
                <span className="font-mono text-neutral-300">v8.0</span>
                <span className="text-xs text-neutral-600">January 2026</span>
              </div>
              <p className="text-sm text-neutral-500">
                Added entropy dimension (H). Formula: D = φ × τ × ρ × (1 - √H). Fixed corporate consciousness bug.
                Identified DMT paradox.
              </p>
            </div>
            
            <div className="p-4 border border-neutral-800">
              <div className="flex justify-between items-start mb-2">
                <span className="font-mono text-neutral-300">v7.0</span>
                <span className="text-xs text-neutral-600">2025</span>
              </div>
              <p className="text-sm text-neutral-500">
                Three-dimensional formula: D = φ × τ × ρ. Introduced multiplicative relationship.
                Had panpsychism problem (Walmart = 0.504).
              </p>
            </div>
            
            <div className="p-4 border border-neutral-800">
              <div className="flex justify-between items-start mb-2">
                <span className="font-mono text-neutral-300">v1-v6</span>
                <span className="text-xs text-neutral-600">2024-2025</span>
              </div>
              <p className="text-sm text-neutral-500">
                Philosophical development. Established core concepts: The Source (raw experiential capacity),
                The Conduit (structure that shapes perspective), gradient of consciousness.
              </p>
            </div>
          </div>
        </section>
        
        {/* Implementation */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Implementation</h2>
          
          <div className="p-4 border border-neutral-800">
            <h3 className="font-mono text-neutral-300 mb-4">TypeScript Engine</h3>
            <pre className="text-xs overflow-x-auto">
{`export interface Invariants {
  phi: number;   // Integration (0-1)
  tau: number;   // Temporal Depth (0-1)
  rho: number;   // Binding (0-1)
  H: number;     // Entropy (0-1)
  kappa: number; // Coherence (0-1)
}

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
  
  return {
    D: Math.max(0, Math.min(1, D)),
    structuralBase,
    entropyPenalty,
    coherenceRecovery,
    entropyModulator,
    interpretation: getInterpretation(D)
  };
}`}
            </pre>
          </div>
          
          <div className="mt-4 p-4 border border-neutral-800">
            <h3 className="font-mono text-neutral-300 mb-4">Python Engine</h3>
            <pre className="text-xs overflow-x-auto">
{`def calculate_density(phi, tau, rho, H, kappa):
    """
    Calculate perspectival density from five invariants.
    
    Args:
        phi: Integration (0-1)
        tau: Temporal depth (0-1)
        rho: Binding (0-1)
        H: Entropy (0-1)
        kappa: Coherence (0-1)
    
    Returns:
        float: Perspectival density D
    """
    structural_base = phi * tau * rho
    entropy_penalty = 1 - math.sqrt(H)
    coherence_recovery = H * kappa
    entropy_modulator = entropy_penalty + coherence_recovery
    
    D = structural_base * entropy_modulator
    return max(0, min(1, D))`}
            </pre>
          </div>
        </section>
        
        {/* Constraints */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Constraints</h2>
          
          <div className="p-4 border border-neutral-800 text-sm text-neutral-500">
            <ul className="space-y-2">
              <li>• All parameters normalized to [0, 1]</li>
              <li>• Output D clamped to [0, 1]</li>
              <li>• Zero in φ, τ, or ρ produces zero D (multiplicative necessity)</li>
              <li>• H=0 produces maximum entropy modulator (1.0)</li>
              <li>• H=1, κ=0 produces minimum entropy modulator (0.0)</li>
              <li>• H=1, κ=1 produces entropy modulator of 1.0 (full recovery)</li>
            </ul>
          </div>
        </section>
        
        {/* Repository */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Repository</h2>
          
          <div className="p-4 border border-neutral-800">
            <a 
              href="https://github.com/Shavatzs001/conduit-monism" 
              className="font-mono text-neutral-300 hover:text-white transition-colors"
              target="_blank"
              rel="noopener noreferrer"
            >
              github.com/Shavatzs001/conduit-monism
            </a>
            <div className="mt-4 text-sm text-neutral-500 font-mono">
              <div>frameworks/    # Theoretical documents</div>
              <div>experiments/   # Test protocols and results</div>
              <div>scripts/       # Python implementations</div>
              <div>website/       # This site (Next.js)</div>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
