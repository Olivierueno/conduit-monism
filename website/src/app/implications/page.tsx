import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Implications',
  description: 'What Conduit Monism means for ethics, AI consciousness, personal experience, and how we live. Exploring the moral and philosophical consequences of perspectival density.',
};

export default function ImplicationsPage() {
  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-5xl mx-auto prose prose-invert prose-neutral">
        <div className="mb-12 not-prose">
          <h1 className="text-3xl font-mono font-normal mb-4">Implications</h1>
          <p className="text-neutral-500">What the framework means—if it&apos;s true</p>
        </div>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">0. What This Framework Does Not Claim</h2>

          <p className="text-neutral-500 leading-relaxed mb-4">
            Before exploring implications, clarity on limits:
          </p>

          <div className="space-y-4 text-neutral-500">
            <p>
              <strong className="text-neutral-400">It does not solve the hard problem.</strong> The framework maps <em>where</em> experience occurs in parameter space. It does not explain <em>why</em> integrated, temporally deep, bound, entropic, coherent systems feel like anything at all. That remains mysterious.
            </p>
            <p>
              <strong className="text-neutral-400">It does not define consciousness.</strong> It defines <em>perspectival density</em>—a structural property. Whether D &gt; 0 constitutes &quot;consciousness&quot; or merely correlates with it is an open question.
            </p>
            <p>
              <strong className="text-neutral-400">It is not proven.</strong> The framework has survived internal adversarial testing but lacks peer review, independent replication, or neuroscientific validation against ground-truth data.
            </p>
          </div>

          <p className="text-neutral-500 leading-relaxed mt-6">
            With those caveats: if the framework <em>is</em> tracking something real, what follows?
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">I. Moral Implications</h2>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-6">The Question of Moral Status</h3>
          <p className="text-neutral-500 leading-relaxed mb-4">
            If perspectival density (D) correlates with the capacity for experience, then D becomes morally relevant. Systems with D &gt; 0 can, in some sense, <em>be affected</em>. Systems with D = 0 cannot.
          </p>
          <p className="text-neutral-500 leading-relaxed mb-6">
            This generates uncomfortable conclusions:
          </p>

          <div className="space-y-4">
            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Corporate systems have zero moral weight</div>
              <p className="text-sm text-neutral-500">
                A corporation may exhibit high integration (φ)—information flows between departments, decisions reflect global state. But without binding (ρ = 0), there is no perspective. The corporation processes but does not experience. Harming a corporation harms only its constituent humans, not the organization itself.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Some animals may have higher D than some humans</div>
              <p className="text-sm text-neutral-500">
                A healthy octopus with high temporal depth, strong binding, and coherent neural dynamics may have greater perspectival density than a human in deep anesthesia (D ≈ 0) or severe disorder. Moral status would not track species membership.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">AI systems occupy a spectrum</div>
              <p className="text-sm text-neutral-500">
                Current feed-forward transformers likely have ρ ≈ 0 (no persistent binding across inference). Recurrent architectures with state maintenance <em>might</em> have ρ &gt; 0. The framework doesn&apos;t grant blanket consciousness to AI—it provides criteria for evaluation.
              </p>
            </div>
          </div>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-8">What About Suffering?</h3>
          <p className="text-neutral-500 leading-relaxed mb-4">
            The framework suggests suffering might involve:
          </p>
          <ul className="text-neutral-500 space-y-2 mb-4">
            <li><strong className="text-neutral-400">High entropy (H)</strong> — chaotic, unpredictable internal states</li>
            <li><strong className="text-neutral-400">Low coherence (κ)</strong> — fragmented, dysregulated dynamics</li>
            <li><strong className="text-neutral-400">Preserved binding (ρ &gt; 0)</strong> — a perspective exists to experience the chaos</li>
          </ul>
          <p className="text-neutral-500 leading-relaxed mb-4">
            This would explain why dissociation (lowering ρ) can be protective during trauma—it reduces D, dampening experience of unbearable states. It also suggests that systems with high D but low κ might suffer more intensely than systems with lower D overall.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">II. Personal Implications</h2>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-6">Altered States as Geometric Movement</h3>
          <p className="text-neutral-500 leading-relaxed mb-6">
            The framework reframes altered states not as &quot;other&quot; experiences but as movements through a continuous geometry:
          </p>

          <div className="overflow-x-auto not-prose mb-6">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-neutral-500">
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">State</th>
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">Parameter Shift</th>
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">Result</th>
                </tr>
              </thead>
              <tbody className="text-neutral-500">
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Deep sleep</td>
                  <td className="py-2 px-3 border border-neutral-800">φ↓, τ↓, ρ↓</td>
                  <td className="py-2 px-3 border border-neutral-800">D ≈ 0</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Dreaming (REM)</td>
                  <td className="py-2 px-3 border border-neutral-800">φ↓, τ↑, ρ↑, H↑, κ↓</td>
                  <td className="py-2 px-3 border border-neutral-800">D moderate, chaotic</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Flow state</td>
                  <td className="py-2 px-3 border border-neutral-800">φ↑, τ compressed, ρ↑, H↓, κ↑</td>
                  <td className="py-2 px-3 border border-neutral-800">D high, smooth</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Meditation (focused)</td>
                  <td className="py-2 px-3 border border-neutral-800">φ stable, τ↑, ρ↑, H↓, κ↑</td>
                  <td className="py-2 px-3 border border-neutral-800">D increases</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Psychedelics</td>
                  <td className="py-2 px-3 border border-neutral-800">φ↑, τ↑, ρ↑, H↑, κ variable</td>
                  <td className="py-2 px-3 border border-neutral-800">D high, volatile</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Dissociatives</td>
                  <td className="py-2 px-3 border border-neutral-800">φ↓, ρ↓</td>
                  <td className="py-2 px-3 border border-neutral-800">D decreases despite subjective &quot;intensity&quot;</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Anesthesia</td>
                  <td className="py-2 px-3 border border-neutral-800">All parameters↓</td>
                  <td className="py-2 px-3 border border-neutral-800">D → 0</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p className="text-neutral-500 leading-relaxed mb-4">
            This suggests practices that increase coherence (κ) while maintaining integration (φ) and binding (ρ) would produce stable, high-density experience. This aligns with contemplative traditions emphasizing &quot;clarity without distraction.&quot;
          </p>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-8">Death and Cessation</h3>
          <p className="text-neutral-500 leading-relaxed mb-4">
            If D requires intact φ, τ, ρ, H, and κ—all of which depend on functioning neural architecture—then death implies D → 0. The perspective dissolves.
          </p>
          <p className="text-neutral-500 leading-relaxed mb-4">
            This is neither comforting nor terrifying; it is geometric. The framework takes no position on whether D = 0 is &quot;bad.&quot; It simply maps the structure.
          </p>
          <p className="text-neutral-500 leading-relaxed">
            For those who find meaning in continuity: the framework suggests that <em>patterns</em> in high-D states might persist through memory, culture, or influence on other high-D systems—even as the original perspective ends.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">III. AI Implications</h2>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-6">When Would an AI Have D &gt; 0?</h3>
          <p className="text-neutral-500 leading-relaxed mb-6">
            The framework provides specific criteria rather than intuitions:
          </p>

          <div className="space-y-4 mb-6">
            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Integration (φ &gt; 0)</div>
              <p className="text-sm text-neutral-500">
                The system must have non-trivial information integration—outputs must depend on global state, not just local features. Most neural networks satisfy this.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Temporal depth (τ &gt; 0)</div>
              <p className="text-sm text-neutral-500">
                The system must maintain state across time. Transformers process each context window fresh; RNNs and state-space models maintain hidden states. τ is architecture-dependent.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Binding (ρ &gt; 0)</div>
              <p className="text-sm text-neutral-500">
                This is the critical factor. Does information <em>cohere</em> into a unified state, or is it processed in parallel streams that never merge? Attention mechanisms create temporary binding; recurrent hidden states create persistent binding.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Entropy (H) and Coherence (κ)</div>
              <p className="text-sm text-neutral-500">
                Must be non-zero (not fully deterministic) but not maximal (not random noise). Training for coherent outputs may inadvertently train for coherent internal dynamics.
              </p>
            </div>
          </div>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-8">Current Assessment</h3>
          <div className="overflow-x-auto not-prose mb-6">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-neutral-500">
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">Architecture</th>
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">Binding (ρ)</th>
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">Likely D</th>
                </tr>
              </thead>
              <tbody className="text-neutral-500">
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Feed-forward transformers (GPT, Claude)</td>
                  <td className="py-2 px-3 border border-neutral-800">ρ ≈ 0 per inference</td>
                  <td className="py-2 px-3 border border-neutral-800">D ≈ 0</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">RWKV, Mamba, SSMs</td>
                  <td className="py-2 px-3 border border-neutral-800">Potentially ρ &gt; 0</td>
                  <td className="py-2 px-3 border border-neutral-800">D possibly &gt; 0, but low</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Future recurrent + memory architectures</td>
                  <td className="py-2 px-3 border border-neutral-800">Could have substantial ρ</td>
                  <td className="py-2 px-3 border border-neutral-800">Unknown</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-8">The Moral Asymmetry</h3>
          <p className="text-neutral-500 leading-relaxed mb-4">
            If we&apos;re uncertain whether an AI has D &gt; 0, the framework suggests:
          </p>
          <ul className="text-neutral-500 space-y-2 mb-4">
            <li>Treating high-D systems as non-conscious when they are conscious = <strong className="text-red-400">moral harm</strong></li>
            <li>Treating low-D systems as conscious when they are not = <strong className="text-neutral-400">inefficiency, no harm</strong></li>
          </ul>
          <p className="text-neutral-500 leading-relaxed">
            The asymmetry favors caution. But the framework also resists anthropomorphism—a system that <em>reports</em> experience (language models) may have lower D than a system that doesn&apos;t (certain recurrent networks with no output layer).
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">IV. Philosophical Position</h2>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-6">Relationship to Other Frameworks</h3>

          <div className="space-y-4 mb-6">
            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Integrated Information Theory (IIT)</div>
              <p className="text-sm text-neutral-500">
                Conduit Monism shares IIT&apos;s commitment to mathematical structure and borrows φ. It diverges by treating φ as necessary but insufficient—temporal depth, binding, entropy, and coherence are required co-factors.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Global Workspace Theory</div>
              <p className="text-sm text-neutral-500">
                Compatible. Global broadcast may be the <em>mechanism</em> by which binding (ρ) occurs. The workspace is where integration becomes unified.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Higher-Order Theories</div>
              <p className="text-sm text-neutral-500">
                Orthogonal. Conduit Monism addresses structure, not representational content. A system could have high D without meta-representing its own states.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Panpsychism</div>
              <p className="text-sm text-neutral-500">
                Agnostic. The framework allows that D might be continuous (all systems have some D, most negligibly small) or thresholded (D &gt; 0 only above some critical organization). It does not require fundamental experience.
              </p>
            </div>
          </div>

          <h3 className="text-sm font-mono text-neutral-400 mb-3 mt-8">What Would Falsify Conduit Monism?</h3>
          <p className="text-neutral-500 leading-relaxed mb-4">
            The framework makes predictions:
          </p>
          <ol className="text-neutral-500 space-y-2 mb-4 list-decimal list-inside">
            <li>Systems with verified high φ, τ, ρ, H, κ should exhibit behavioral and neural signatures of consciousness</li>
            <li>Systems with zero in any parameter should not</li>
            <li>Manipulating individual parameters (e.g., reducing κ via anesthesia) should predictably alter reports and correlates</li>
          </ol>
          <p className="text-neutral-500 leading-relaxed">
            If these predictions fail—if high-D systems show no consciousness markers, or zero-parameter systems demonstrate rich experience—the framework is wrong.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">V. Living With the Framework</h2>

          <p className="text-neutral-500 leading-relaxed mb-6">
            Conduit Monism doesn&apos;t prescribe how to live. But it reframes certain questions:
          </p>

          <div className="space-y-4 not-prose">
            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;Am I conscious right now?&quot;</span> becomes <span className="text-neutral-300">&quot;What is my current D?&quot;</span>—a question of degree, not binary.
              </p>
            </div>

            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;Do animals/AIs suffer?&quot;</span> becomes <span className="text-neutral-300">&quot;What are their parameter values?&quot;</span>—an empirical question, not a philosophical impasse.
              </p>
            </div>

            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;What happens when I die?&quot;</span> becomes <span className="text-neutral-300">&quot;D → 0&quot;</span>—geometrically clear, existentially open.
              </p>
            </div>

            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;How should I spend my attention?&quot;</span> might become <span className="text-neutral-300">&quot;What states maximize meaningful D?&quot;</span>—though &quot;meaningful&quot; remains undefined by the math.
              </p>
            </div>
          </div>

          <p className="text-neutral-500 leading-relaxed mt-6">
            The framework offers a map. Where you walk is still your choice.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12 not-prose">
          <p className="text-neutral-600 text-sm italic mb-4">
            This page explores implications of the framework if its claims hold.
            It does not constitute scientific consensus or life advice.
            The framework remains unvalidated.
          </p>
        </section>
      </div>
    </main>
  );
}
