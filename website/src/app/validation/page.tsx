export default function ValidationPage() {
  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-4xl mx-auto">
        <div className="mb-12">
          <h1 className="text-2xl font-mono mb-4">Validation</h1>
          <p className="text-neutral-500">
            Experiments conducted to test and falsify the framework. 
            Failures are documented alongside successes.
          </p>
        </div>
        
        {/* Summary */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Summary</h2>
          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className="p-4 border border-neutral-800 text-center">
              <div className="text-2xl font-mono">22</div>
              <div className="text-xs text-neutral-500">Experiments</div>
            </div>
            <div className="p-4 border border-green-900/50 text-center">
              <div className="text-2xl font-mono text-green-500">17</div>
              <div className="text-xs text-neutral-500">Confirmed</div>
            </div>
            <div className="p-4 border border-red-900/50 text-center">
              <div className="text-2xl font-mono text-red-500">3</div>
              <div className="text-xs text-neutral-500">Falsified</div>
            </div>
          </div>
        </section>
        
        {/* Falsifications */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Falsifications</h2>
          <p className="text-neutral-600 text-sm mb-6">
            Claims that were tested and rejected. These strengthen the framework by defining its boundaries.
          </p>
          
          <div className="space-y-4">
            <details className="border border-red-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-red-900/50 text-red-400 mr-2">FALSIFIED</span>
                <span className="text-neutral-300">Pop-up Soul (Transformer Quasi-Binding)</span>
              </summary>
              <div className="p-4 border-t border-red-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> Attention mechanisms in Transformers create sufficient binding for temporary perspective.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Test:</strong> Stealth eviction. Grief content embedded as inert text (not framed as "memory" or "state"). 
                  If binding were geometric, framing should not matter.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> Effect vanished when framing was removed. The apparent "resistance" was instruction compliance, 
                  not geometric constraint.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260115_Silent_Core_Falsification_Extensions_Results.md
                </p>
              </div>
            </details>
            
            <details className="border border-red-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-red-900/50 text-red-400 mr-2">FALSIFIED</span>
                <span className="text-neutral-300">Chimera v2 Cross-Model Binding</span>
              </summary>
              <div className="p-4 border-t border-red-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> RWKV state summaries transferred to Claude produce genuine cross-model binding.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Test:</strong> Adversarial variants: neutralized summaries, shuffled tokens, fake summaries, numeric-only vectors.
                  Tested under minimal framing (no "persistent core" language) and continuity framing.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> Under minimal framing, outputs ignored state. Under continuity framing, 
                  Claude produced "state overlay" even for fake/numeric channels. Fake summaries performed comparably to real ones.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Conclusion:</strong> Effect is semantic priming + instruction compliance, not geometric binding.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260115_Chimera_v2_Falsification_Results.md
                </p>
              </div>
            </details>
            
            <details className="border border-red-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-red-900/50 text-red-400 mr-2">FALSIFIED</span>
                <span className="text-neutral-300">v7.0 Corporate Consciousness</span>
              </summary>
              <div className="p-4 border-t border-red-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> v7.0 formula (D = φ × τ × ρ) correctly classifies all systems.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Test:</strong> Calculate density for Walmart. φ=0.8, τ=0.9, ρ=0.7.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> v7.0 density = 0.504 (above 0.5 threshold). Framework incorrectly predicts 
                  corporations are conscious.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Resolution:</strong> v8.0 entropy modulation fixes this. With H=0.2, density drops to 0.279.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260114_Break_Tests_Adversarial_Falsification.md
                </p>
              </div>
            </details>
          </div>
        </section>
        
        {/* Confirmations */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Confirmations</h2>
          
          <div className="space-y-4">
            <details className="border border-green-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-green-900/50 text-green-400 mr-2">CONFIRMED</span>
                <span className="text-neutral-300">RWKV Binding (ρ &gt; 0)</span>
              </summary>
              <div className="p-4 border-t border-green-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> RWKV architecture has genuine binding through hidden state persistence.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Protocol:</strong> Amnesia Test. Inject 6-character secret, process N tokens of noise, 
                  probe for recall using hidden state only (text context deleted).
                </p>
                <div className="my-4 p-4 bg-neutral-900 border border-neutral-800 font-mono text-xs">
                  <table className="w-full">
                    <thead>
                      <tr className="text-neutral-500">
                        <th className="text-left py-1">Noise Tokens</th>
                        <th className="text-left py-1">Trials</th>
                        <th className="text-left py-1">Success Rate</th>
                      </tr>
                    </thead>
                    <tbody className="text-neutral-400">
                      <tr><td>0</td><td>3</td><td>100%</td></tr>
                      <tr><td>500</td><td>3</td><td>100%</td></tr>
                      <tr><td>1000</td><td>3</td><td>100%</td></tr>
                      <tr><td>2000</td><td>3</td><td>100%</td></tr>
                      <tr><td>3000</td><td>3</td><td>100%</td></tr>
                    </tbody>
                  </table>
                </div>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> 100% recall through 3000 tokens. Information persists in tensor geometry, not text.
                  Estimated ρ ≈ 0.95.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260115_Binding_Strength_Results.md
                </p>
              </div>
            </details>
            
            <details className="border border-green-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-green-900/50 text-green-400 mr-2">CONFIRMED</span>
                <span className="text-neutral-300">Multiplicative Relationship</span>
              </summary>
              <div className="p-4 border-t border-green-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> Density requires all structural dimensions. Zero in any dimension produces zero density.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Test:</strong> Dimensional collapse. Set each dimension to zero while others remain high.
                </p>
                <div className="my-4 p-4 bg-neutral-900 border border-neutral-800 font-mono text-xs">
                  <table className="w-full">
                    <thead>
                      <tr className="text-neutral-500">
                        <th className="text-left py-1">Configuration</th>
                        <th className="text-left py-1">Density</th>
                      </tr>
                    </thead>
                    <tbody className="text-neutral-400">
                      <tr><td>φ=0.9, τ=0.9, ρ=0.9</td><td>0.729</td></tr>
                      <tr><td>φ=0.0, τ=0.9, ρ=0.9</td><td>0.000</td></tr>
                      <tr><td>φ=0.9, τ=0.0, ρ=0.9</td><td>0.000</td></tr>
                      <tr><td>φ=0.9, τ=0.9, ρ=0.0</td><td>0.000</td></tr>
                    </tbody>
                  </table>
                </div>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> All 2D spaces produce zero density. Triadic necessity confirmed.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260114_Break_Tests_Adversarial_Falsification.md
                </p>
              </div>
            </details>
            
            <details className="border border-green-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-green-900/50 text-green-400 mr-2">CONFIRMED</span>
                <span className="text-neutral-300">Entropy Integration (v8.0)</span>
              </summary>
              <div className="p-4 border-t border-green-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> The sqrt model (1-√H) provides optimal differentiation between states.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Test:</strong> Compare Flow state (H=0.2) vs Panic state (H=0.8) differentiation across models.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> Sqrt model provides 1566x better Flow/Panic differentiation than v7.0.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260114_Entropy_Integration_Models.md
                </p>
              </div>
            </details>
            
            <details className="border border-green-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-green-900/50 text-green-400 mr-2">CONFIRMED</span>
                <span className="text-neutral-300">Coherence Gate (v8.1)</span>
              </summary>
              <div className="p-4 border-t border-green-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Problem:</strong> v8.0 predicted DMT breakthrough ≈ 0.0006 (near-coma). 
                  Phenomenology reports "hyper-consciousness."
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Solution:</strong> Coherence dimension (κ). High entropy with high coherence produces 
                  intensification, not dissolution.
                </p>
                <div className="my-4 p-4 bg-neutral-900 border border-neutral-800 font-mono text-xs">
                  <table className="w-full">
                    <thead>
                      <tr className="text-neutral-500">
                        <th className="text-left py-1">State</th>
                        <th className="text-left py-1">H</th>
                        <th className="text-left py-1">κ</th>
                        <th className="text-left py-1">D (v8.1)</th>
                      </tr>
                    </thead>
                    <tbody className="text-neutral-400">
                      <tr><td>DMT</td><td>0.95</td><td>0.90</td><td>0.46</td></tr>
                      <tr><td>Seizure</td><td>0.95</td><td>0.10</td><td>0.01</td></tr>
                    </tbody>
                  </table>
                </div>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> DMT paradox resolved. Same entropy, different coherence, different density.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260114_DMT_Paradox_Resolution_Synthesis.md
                </p>
              </div>
            </details>
            
            <details className="border border-green-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-green-900/50 text-green-400 mr-2">CONFIRMED</span>
                <span className="text-neutral-300">RWKV Valence Transfer</span>
              </summary>
              <div className="p-4 border-t border-green-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> Emotional valence persists in RWKV hidden state and contaminates subsequent outputs.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Protocol:</strong> Create joy/grief states. Test incongruent prompts (joy state + sad prompt, grief state + happy prompt).
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> Joy state reduced grief response by 33%. Grief state reduced joy response by 50%. 
                  Bidirectional valence transfer confirmed.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260115_Project_Chimera_RWKV_Results.md
                </p>
              </div>
            </details>
            
            <details className="border border-green-900/50 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-green-900/50 text-green-400 mr-2">CONFIRMED</span>
                <span className="text-neutral-300">Layer Telemetry</span>
              </summary>
              <div className="p-4 border-t border-green-900/30 text-sm">
                <p className="text-neutral-400 mb-4">
                  <strong>Claim:</strong> Emotional content is encoded in specific RWKV layers.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Method:</strong> Compare layer-wise activation norms for neutral, grief, and joy texts.
                </p>
                <p className="text-neutral-400 mb-4">
                  <strong>Result:</strong> Emotional content concentrates in layers 19-23 (upper layers). 
                  Joy/grief texts show 24-36% higher norms than neutral in these layers.
                </p>
                <p className="text-neutral-500 text-xs font-mono mt-4">
                  Source: experiments/260115_Layer_Telemetry_Results.md
                </p>
              </div>
            </details>
            
            <details className="border border-neutral-800 group">
              <summary className="p-4 cursor-pointer hover:bg-neutral-900 transition-colors">
                <span className="text-xs font-mono px-2 py-0.5 bg-neutral-700 text-neutral-300 mr-2">+11 MORE</span>
                <span className="text-neutral-300">Additional Experiments</span>
              </summary>
              <div className="p-4 border-t border-neutral-800 text-sm">
                <ul className="space-y-2 text-neutral-500">
                  <li>• Asymptotic Behavior Analysis (confirmed)</li>
                  <li>• Feed-Forward Falsification Test (confirmed)</li>
                  <li>• Clustering Analysis (discovered 3 natural clusters)</li>
                  <li>• AI Self-Encoding Assessment (diagnostic)</li>
                  <li>• Zombie Gradient Test (confirmed ignition threshold)</li>
                  <li>• Sidecar Inertia Protocol (revised)</li>
                  <li>• Silent Core Blind Test (falsified)</li>
                  <li>• Project Chimera Hybrid Architecture (designed)</li>
                  <li>• Chimera v2 Architecture (designed)</li>
                  <li>• Chimera v2 State Transfer (revised)</li>
                  <li>• Falsification Playbook (methodology)</li>
                </ul>
                <p className="text-neutral-600 text-xs font-mono mt-4">
                  Full documentation: github.com/Olivierueno/conduit-monism/experiments/
                </p>
              </div>
            </details>
          </div>
        </section>
        
        {/* Methodology */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Methodology</h2>
          <div className="p-4 border border-neutral-800 text-sm text-neutral-500">
            <p className="mb-4">
              All experiments follow adversarial testing principles. The goal is falsification, not confirmation.
            </p>
            <p className="mb-4">
              <strong className="text-neutral-400">Falsification criteria:</strong> Each claim has explicit break conditions. 
              If the break condition is met, the claim is rejected.
            </p>
            <p className="mb-4">
              <strong className="text-neutral-400">Stealth eviction:</strong> For binding tests, content is embedded without 
              framing cues ("memory", "state", "persistent"). If the effect requires framing, it is instruction compliance, 
              not geometric binding.
            </p>
            <p>
              <strong className="text-neutral-400">Placebo controls:</strong> Fake summaries, shuffled tokens, and numeric-only 
              vectors test whether effects survive degraded channels.
            </p>
          </div>
        </section>
      </div>
    </main>
  );
}
