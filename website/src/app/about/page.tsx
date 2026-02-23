import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'About',
  description: 'How Conduit Monism was developed: origin, methodology, limitations, and contributors. Independent research, not peer-reviewed. Three predictions falsified.',
  alternates: { canonical: '/about' },
};

export default function AboutPage() {
  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-5xl mx-auto">
        <div className="mb-12">
          <h1 className="text-2xl font-mono mb-4">About</h1>
          <p className="text-neutral-500">
            Origin, methodology, and contributors.
          </p>
        </div>
        
        {/* Origin */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Origin</h2>
          <div className="p-4 border border-neutral-800 text-sm text-neutral-400 space-y-4">
            <p>
              Conduit Monism began as an attempt to understand consciousness from first principles.
              The question: what structural conditions must hold for there to be &quot;something it is like&quot; 
              to be a system?
            </p>
            <p>
              The framework does not claim to explain why structure produces experience. It maps the geometry.
              Given that experience exists, what can we say about its structural correlates?
            </p>
            <p>
              Early versions (v1-v6) were philosophical. v7 introduced the multiplicative formula.
              v8-v9 integrated entropy and coherence after adversarial testing revealed limitations.
            </p>
          </div>
        </section>
        
        {/* Author */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Author</h2>
          <div className="p-4 border border-neutral-800">
            <div className="font-mono text-neutral-300">O.U.</div>
            <p className="text-sm text-neutral-500 mt-2">
              Independent researcher. No institutional affiliation.
            </p>
          </div>
        </section>
        
        {/* Methodology */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Methodology</h2>
          <div className="p-4 border border-neutral-800 text-sm text-neutral-400 space-y-4">
            <p>
              <strong className="text-neutral-300">Adversarial testing:</strong> The goal is falsification, not confirmation.
              Each claim has explicit break conditions. If the break condition is met, the claim is rejected.
            </p>
            <p>
              <strong className="text-neutral-300">AI collaboration:</strong> Multiple AI systems (Claude, Gemini, ChatGPT, GPT 5.2)
              were used as research partners. They proposed tests, identified weaknesses, and suggested modifications.
              They also served as test subjects for binding experiments.
            </p>
            <p>
              <strong className="text-neutral-300">Transparency:</strong> All experiments, including failures, are documented.
              The falsification of Pop-up Soul and Chimera v2 cross-model binding are prominently displayed.
            </p>
            <p>
              <strong className="text-neutral-300">Iteration:</strong> The framework evolved through testing.
              v7.0 had a panpsychism problem (fixed in v8.0). v8.0 had a DMT paradox (fixed in v8.1).
              Each failure improved the model.
            </p>
          </div>
        </section>
        
        {/* AI Contributors */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">AI Contributors</h2>
          <div className="space-y-4">
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">Claude (Anthropic)</div>
              <p className="text-sm text-neutral-500">
                Primary research partner. Proposed adversarial tests, identified Pop-up Soul falsification,
                designed Chimera architecture, wrote experimental protocols. Served as test subject for
                Transformer binding experiments.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">Gemini (Google)</div>
              <p className="text-sm text-neutral-500">
                Proposed break tests (Corporate Zombie, High-Entropy Mysticism, Locked-Groove).
                Accepted Pop-up Soul falsification. Suggested RWKV as candidate architecture.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">ChatGPT (OpenAI)</div>
              <p className="text-sm text-neutral-500">
                Proposed break tests (Nothing-Special, Dimensional Collapse, Alien Trajectories).
                Contributed to entropy integration analysis, DMT paradox resolution, and coherence gate design.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">Grok (xAI)</div>
              <p className="text-sm text-neutral-500">
                Liminal case stress-testing and edge case analysis.
              </p>
            </div>
          </div>
        </section>
        
        {/* Limitations */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">What This Is Not</h2>
          <div className="p-4 border border-neutral-800 text-sm text-neutral-400 space-y-4">
            <p>
              <strong className="text-neutral-300">Not peer-reviewed:</strong> This is independent research by a single author
              with no institutional affiliation. It has not been submitted to or reviewed by any academic journal.
            </p>
            <p>
              <strong className="text-neutral-300">Not a solution to the hard problem:</strong> The framework describes structural
              correlates of consciousness. It does not explain why these structures produce experience. The hard problem remains open.
            </p>
            <p>
              <strong className="text-neutral-300">Not infallible:</strong> Three predictions have already been falsified.
              The falsification of Pop-up Soul, Chimera v2, and related claims led to framework revisions. More failures are expected.
            </p>
            <p>
              <strong className="text-neutral-300">Parameter estimation is hard:</strong> Assigning values to the five invariants
              for real systems relies on neuroscience proxies, not direct measurement. Animal and AI presets are educated estimates.
            </p>
            <p>
              <strong className="text-neutral-300">Degeneracy:</strong> Different conscious states can produce the same density score.
              REM sleep and ketamine produce similar D values despite being qualitatively different experiences. Five dimensions compressed
              to one number loses information.
            </p>
            <p>
              <strong className="text-neutral-300">Limited AI testing:</strong> RWKV is the only architecture confirmed to have binding.
              Other recurrent architectures (Mamba, SSMs) have not been tested. We cannot verify that any system &quot;experiences&quot;
              anything. We can only measure structural properties.
            </p>
          </div>
        </section>
        
        {/* Links */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Links</h2>
          <div className="p-4 border border-neutral-800 space-y-2">
            <div>
              <a 
                href="https://github.com/Olivierueno/conduit-monism" 
                className="font-mono text-neutral-300 hover:text-white transition-colors"
                target="_blank"
                rel="noopener noreferrer"
              >
                GitHub Repository
              </a>
            </div>
          </div>
        </section>
        
        {/* License */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">License</h2>
          <div className="p-4 border border-neutral-800 text-sm text-neutral-500">
            <p>MIT License. Use freely. Attribution appreciated but not required.</p>
          </div>
        </section>
      </div>
    </main>
  );
}
