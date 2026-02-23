import Link from 'next/link';
import ParticleCanvas from '@/components/ParticleCanvas';

export default function Home() {
  return (
    <main className="min-h-screen">
      {/* Hero */}
      <section className="relative min-h-screen flex items-center px-6 border-b border-neutral-800">
        <ParticleCanvas />
        <div className="max-w-5xl mx-auto relative z-10">
          <p className="text-neutral-500 text-sm mb-4 font-mono">v9.3.2 / February 2026</p>
          <h1 className="text-4xl md:text-5xl font-mono font-normal mb-8 leading-tight">
            Conduit Monism
          </h1>
          <p className="text-xl text-neutral-400 mb-6 leading-relaxed">
            There is something it is like to be you.
          </p>
          <p className="text-neutral-500 leading-relaxed mb-8">
            This project maps the structural conditions of experience from first principles.
            It started as philosophy, became mathematics, and now makes testable predictions
            about which systems can be conscious and which cannot. It does not claim to solve
            the hard problem. It maps the geometry.
          </p>
          <div className="flex gap-4">
            <Link
              href="/framework"
              className="px-4 py-2 bg-white text-black text-sm font-mono hover:bg-neutral-200 transition-colors"
            >
              Read Framework
            </Link>
            <Link
              href="/engine"
              className="px-4 py-2 border border-neutral-700 text-sm font-mono hover:border-neutral-500 transition-colors"
            >
              Use Engine
            </Link>
          </div>
        </div>
      </section>

      {/* Formula */}
      <section className="py-16 px-6 border-b border-neutral-800">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-6 uppercase tracking-wide">The Formula</h2>
          <code className="block font-mono text-2xl mb-6 p-6 bg-neutral-900 border border-neutral-800">
            D = φ × τ × ρ × [(1 - √H) + (H × κ)]
          </code>
          <p className="text-neutral-500 text-sm leading-relaxed">
            Five conditions must all be present for experience to occur.
            If any one drops to zero, experience disappears entirely.
          </p>
        </div>
      </section>

      {/* Invariants */}
      <section className="py-16 px-6 border-b border-neutral-800">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-8 uppercase tracking-wide">Five Invariants</h2>
          <div className="space-y-4">
            {[
              { symbol: 'φ', name: 'Integration', human: 'Is it one thing or many?', desc: 'Information unified across the system' },
              { symbol: 'τ', name: 'Temporal Depth', human: 'Does the moment contain history?', desc: 'Past states constrain present states' },
              { symbol: 'ρ', name: 'Binding', human: 'Does it know that it knows?', desc: 'The system observes its own states' },
              { symbol: 'H', name: 'Entropy', human: 'How chaotic is the signal?', desc: 'Noise in system dynamics' },
              { symbol: 'κ', name: 'Coherence', human: 'Is the chaos meaningful?', desc: 'Structure within entropy' },
            ].map((inv) => (
              <div key={inv.symbol} className="py-3 border-b border-neutral-900">
                <div className="flex items-baseline gap-4">
                  <span className="text-neutral-300">{inv.name}</span>
                  <span className="text-neutral-500 text-sm">{inv.human}</span>
                </div>
                <div className="mt-1 text-xs text-neutral-600">
                  <span className="font-mono">{inv.symbol}</span> / {inv.desc}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* What We Explored */}
      <section className="py-16 px-6 border-b border-neutral-800">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-8 uppercase tracking-wide">What We Explored</h2>

          <div className="grid md:grid-cols-2 gap-4">
            <Link
              href="/validation"
              className="p-4 border border-neutral-800 hover:border-neutral-600 transition-colors group"
            >
              <h3 className="font-mono text-neutral-300 group-hover:text-white transition-colors mb-2">Consciousness and AI</h3>
              <p className="text-neutral-500 text-sm leading-relaxed">
                Can ChatGPT or Claude be conscious? We tested it. Short answer: no.
                But one architecture surprised us.
              </p>
              <span className="text-xs text-neutral-600 group-hover:text-neutral-400 transition-colors mt-3 block font-mono">
                See experiments →
              </span>
            </Link>

            <Link
              href="/framework"
              className="p-4 border border-neutral-800 hover:border-neutral-600 transition-colors group"
            >
              <h3 className="font-mono text-neutral-300 group-hover:text-white transition-colors mb-2">Other Animals</h3>
              <p className="text-neutral-500 text-sm leading-relaxed">
                Where does experience begin in the animal kingdom?
                The framework predicts what kinds of nervous systems can support it.
              </p>
              <span className="text-xs text-neutral-600 group-hover:text-neutral-400 transition-colors mt-3 block font-mono">
                Read framework →
              </span>
            </Link>

            <Link
              href="/implications"
              className="p-4 border border-neutral-800 hover:border-neutral-600 transition-colors group"
            >
              <h3 className="font-mono text-neutral-300 group-hover:text-white transition-colors mb-2">States of Being</h3>
              <p className="text-neutral-500 text-sm leading-relaxed">
                Why does a psychedelic trip feel &quot;more real than real&quot; while a seizure feels like
                dissolution? Both are chaotic. The difference is structure.
              </p>
              <span className="text-xs text-neutral-600 group-hover:text-neutral-400 transition-colors mt-3 block font-mono">
                Explore implications →
              </span>
            </Link>

            <Link
              href="/implications"
              className="p-4 border border-neutral-800 hover:border-neutral-600 transition-colors group"
            >
              <h3 className="font-mono text-neutral-300 group-hover:text-white transition-colors mb-2">Our Own Existence</h3>
              <p className="text-neutral-500 text-sm leading-relaxed">
                What happens to experience when you fall asleep, meditate, or enter flow?
                The formula maps these transitions.
              </p>
              <span className="text-xs text-neutral-600 group-hover:text-neutral-400 transition-colors mt-3 block font-mono">
                Explore implications →
              </span>
            </Link>
          </div>
        </div>
      </section>

      {/* Navigation */}
      <section className="py-16 px-6">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-8 uppercase tracking-wide">Contents</h2>
          <div className="grid md:grid-cols-2 gap-4">
            {[
              { href: '/framework', title: 'Framework', desc: 'The full theory, written to be understood' },
              { href: '/engine', title: 'Engine', desc: 'Try the formula yourself' },
              { href: '/calibration', title: 'Calibration', desc: 'How each variable maps to brain measurements' },
              { href: '/validation', title: 'Validation', desc: 'Every experiment, including the failures' },
              { href: '/technical', title: 'Technical', desc: 'Formula derivation and version history' },
              { href: '/about', title: 'About', desc: 'Methodology and contributors' },
            ].map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="p-4 border border-neutral-800 hover:border-neutral-600 transition-colors group"
              >
                <h3 className="font-mono text-neutral-300 group-hover:text-white transition-colors">{item.title}</h3>
                <p className="text-neutral-600 text-sm mt-1">{item.desc}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 px-6 border-t border-neutral-800 text-center">
        <p className="text-neutral-600 text-xs font-mono">
          O.U. / 2026 /
          <a href="https://github.com/Olivierueno/conduit-monism" className="hover:text-neutral-400 ml-1">GitHub</a>
        </p>
      </footer>
    </main>
  );
}
