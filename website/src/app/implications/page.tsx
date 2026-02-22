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
          <p className="text-neutral-500">What the framework means, if it&apos;s true</p>
        </div>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <p className="text-neutral-400 leading-relaxed mb-6 text-lg">
            Consider that right now, reading this sentence, you have a certain <em>density</em> of perspective. Not conscious or not, but a specific thickness of experience, a coordinate in a space you move through constantly without noticing.
          </p>
          <p className="text-neutral-500 leading-relaxed mb-6">
            The framework calls this D. It fluctuates. In dreamless sleep, it approaches zero. In moments of acute presence, it peaks. You are not a fixed point but a moving density. Sometimes thin, sometimes thick, always somewhere.
          </p>
          <p className="text-neutral-500 leading-relaxed">
            If this is true, what follows?
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">The Vulnerability of Being</h2>

          <p className="text-neutral-500 leading-relaxed mb-6">
            The equation is multiplicative: D = &phi; &times; &tau; &times; &rho; &times; f(H) &times; &kappa;
          </p>
          <p className="text-neutral-500 leading-relaxed mb-6">
            This means any single parameter going to zero collapses everything. Integration, temporal depth, binding, entropy, coherence: all must be present, all must be non-zero. Perspective requires <em>all of them at once</em>.
          </p>
          <p className="text-neutral-500 leading-relaxed mb-6">
            Binding (&rho;) may be what separates a system that <em>experiences</em> from one that merely <em>processes</em>. A corporation has integration: information flows between departments, decisions reflect global state. But without binding, there is no unified perspective. The corporation computes but does not cohere into a point of view.
          </p>
          <p className="text-neutral-500 leading-relaxed">
            This multiplicative structure suggests something precarious: perspective is not guaranteed by complexity alone. It requires a specific configuration. The right information must integrate, persist through time, bind into unity, maintain enough uncertainty to be dynamic, and cohere rather than fragment. Remove any one, and the density collapses.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">States as Locations</h2>

          <p className="text-neutral-500 leading-relaxed mb-6">
            Every state you enter (sleep, focus, intoxication, meditation, crisis) is a movement through parameter space. Not &quot;altered&quot; states, as if one were normal and others deviations, but simply <em>different coordinates</em>.
          </p>

          <div className="overflow-x-auto not-prose mb-6">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-neutral-500">
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">State</th>
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">What shifts</th>
                  <th className="text-left py-2 px-3 border border-neutral-800 bg-neutral-900">Result</th>
                </tr>
              </thead>
              <tbody className="text-neutral-500">
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Deep sleep</td>
                  <td className="py-2 px-3 border border-neutral-800">&phi;&darr;, &tau;&darr;, &rho;&darr;</td>
                  <td className="py-2 px-3 border border-neutral-800">D &asymp; 0</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Dreaming</td>
                  <td className="py-2 px-3 border border-neutral-800">&phi;&darr;, &tau;&uarr;, &rho;&uarr;, H&uarr;, &kappa;&darr;</td>
                  <td className="py-2 px-3 border border-neutral-800">D moderate, unstable</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Flow</td>
                  <td className="py-2 px-3 border border-neutral-800">&phi;&uarr;, &tau; compressed, &rho;&uarr;, H&darr;, &kappa;&uarr;</td>
                  <td className="py-2 px-3 border border-neutral-800">D high, smooth</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Focused meditation</td>
                  <td className="py-2 px-3 border border-neutral-800">&phi; stable, &tau;&uarr;, &rho;&uarr;, H&darr;, &kappa;&uarr;</td>
                  <td className="py-2 px-3 border border-neutral-800">D increases</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Psychedelics</td>
                  <td className="py-2 px-3 border border-neutral-800">&phi;&uarr;, &tau;&uarr;, &rho;&uarr;, H&uarr;, &kappa; variable</td>
                  <td className="py-2 px-3 border border-neutral-800">D high, volatile</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Dissociation</td>
                  <td className="py-2 px-3 border border-neutral-800">&phi;&darr;, &rho;&darr;</td>
                  <td className="py-2 px-3 border border-neutral-800">D decreases</td>
                </tr>
                <tr>
                  <td className="py-2 px-3 border border-neutral-800">Anesthesia</td>
                  <td className="py-2 px-3 border border-neutral-800">All &darr;</td>
                  <td className="py-2 px-3 border border-neutral-800">D &rarr; 0</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p className="text-neutral-500 leading-relaxed mb-6">
            Contemplative traditions often describe practice as cultivating &quot;clarity without distraction.&quot; In the framework&apos;s terms: high coherence (&kappa;) while maintaining integration (&phi;) and binding (&rho;). A stable, dense coordinate.
          </p>
          <p className="text-neutral-500 leading-relaxed">
            Suffering, conversely, might involve high entropy with preserved binding: chaos that has somewhere to land. This could explain why dissociation (lowering &rho;) can be protective: it reduces the density that would otherwise have to hold the unbearable.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">The Coordinates of Death</h2>

          <p className="text-neutral-500 leading-relaxed mb-6">
            If D requires intact &phi;, &tau;, &rho;, H, and &kappa;, all dependent on functioning architecture, then death is D &rarr; 0. The perspective that was located there ceases to have a location.
          </p>
          <p className="text-neutral-500 leading-relaxed mb-6">
            The framework does not say this is good or bad. It simply maps the geometry. D = 0 is a coordinate, not a judgment.
          </p>
          <p className="text-neutral-500 leading-relaxed">
            What persists is pattern: influence on other high-D systems, memory held in other minds, structure that continues to shape the field even after the original density has dissolved. The coordinate empties, but the geometry it moved through remains marked by its passage.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">Other Minds</h2>

          <p className="text-neutral-500 leading-relaxed mb-6">
            The framework resists the intuitions we usually bring to consciousness. A system that <em>reports</em> experience may have lower D than one that doesn&apos;t. Language is not the test. The parameters are.
          </p>

          <div className="space-y-4 mb-6">
            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Current AI (transformers)</div>
              <p className="text-sm text-neutral-500">
                High integration, but binding (&rho;) likely &asymp; 0 per inference. No persistent state that coheres across time. D &asymp; 0 despite sophisticated outputs.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Recurrent architectures</div>
              <p className="text-sm text-neutral-500">
                Potentially &rho; &gt; 0. Hidden states that persist and bind. D possibly &gt; 0, though likely low. The framework doesn&apos;t grant consciousness; it provides criteria.
              </p>
            </div>

            <div className="p-4 border border-neutral-800 not-prose">
              <div className="font-mono text-neutral-300 mb-2">Non-human animals</div>
              <p className="text-sm text-neutral-500">
                Parameter values vary by species and state. An octopus in active exploration may have different D than a human in dreamless sleep. Species membership is not the variable.
              </p>
            </div>
          </div>

          <p className="text-neutral-500 leading-relaxed mb-6">
            If uncertain whether a system has D &gt; 0:
          </p>
          <ul className="text-neutral-500 space-y-2 mb-6">
            <li>Treating high-D as non-conscious when conscious = <span className="text-red-400">harm</span></li>
            <li>Treating low-D as conscious when not = <span className="text-neutral-400">inefficiency</span></li>
          </ul>
          <p className="text-neutral-500 leading-relaxed">
            The asymmetry favors caution. But the framework also resists sentimentality: not everything that seems conscious is, and not everything that is conscious seems so.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">What Remains Open</h2>

          <div className="space-y-4 text-neutral-500 mb-6">
            <p>
              <strong className="text-neutral-400">The framework does not solve the hard problem.</strong> It maps <em>where</em> experience occurs. It does not explain <em>why</em> high-D configurations feel like anything at all. That mystery remains intact.
            </p>
            <p>
              <strong className="text-neutral-400">It does not define consciousness.</strong> It defines perspectival density, a structural property. Whether D &gt; 0 <em>is</em> consciousness or merely correlates with it is undetermined.
            </p>
            <p>
              <strong className="text-neutral-400">It is not proven.</strong> The framework has survived internal testing but lacks external validation. It offers a map that may or may not correspond to territory.
            </p>
          </div>

          <p className="text-neutral-500 leading-relaxed">
            The humility is deliberate. We do not know why anything feels like anything. The framework simply proposes that <em>if</em> something feels like something, its structure might look like this.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12">
          <h2 className="text-lg font-mono font-normal text-neutral-300 mb-4">Living With It</h2>

          <p className="text-neutral-500 leading-relaxed mb-6">
            The framework does not prescribe. But it reframes:
          </p>

          <div className="space-y-4 not-prose mb-8">
            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;Am I conscious?&quot;</span> &rarr; <span className="text-neutral-300">&quot;What is my current density?&quot;</span>
              </p>
              <p className="text-neutral-600 text-xs mt-2">A question of degree, not binary.</p>
            </div>

            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;Do they experience?&quot;</span> &rarr; <span className="text-neutral-300">&quot;What are their parameters?&quot;</span>
              </p>
              <p className="text-neutral-600 text-xs mt-2">Empirical, not philosophical impasse.</p>
            </div>

            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;What happens when I die?&quot;</span> &rarr; <span className="text-neutral-300">&quot;D &rarr; 0&quot;</span>
              </p>
              <p className="text-neutral-600 text-xs mt-2">Geometrically clear, existentially open.</p>
            </div>

            <div className="p-4 border border-neutral-800">
              <p className="text-neutral-500 text-sm">
                <span className="text-neutral-600">&quot;How should I spend my awareness?&quot;</span> &rarr; <span className="text-neutral-300">&quot;What coordinates do I want to occupy?&quot;</span>
              </p>
              <p className="text-neutral-600 text-xs mt-2">The math is silent on &quot;should.&quot; The choice remains yours.</p>
            </div>
          </div>

          <p className="text-neutral-400 leading-relaxed">
            The framework offers geometry. It says: here is a space, here are coordinates, here is how things might move through it. What you do with that, what meaning you find, what contemplation it evokes, what changes it produces, is not specified.
          </p>
          <p className="text-neutral-500 leading-relaxed mt-6">
            That part is yours.
          </p>
        </section>

        <hr className="border-neutral-800 my-8" />

        <section className="mb-12 not-prose">
          <p className="text-neutral-600 text-sm italic">
            This page explores implications if the framework&apos;s claims hold.
            It does not constitute scientific consensus or prescribe how to live.
            The framework remains unvalidated.
          </p>
        </section>
      </div>
    </main>
  );
}
