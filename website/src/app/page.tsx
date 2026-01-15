import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen">
      {/* Hero */}
      <section className="py-24 px-6 border-b border-neutral-800">
        <div className="max-w-4xl mx-auto">
          <p className="text-neutral-500 text-sm mb-4 font-mono">v9.0 / January 2026</p>
          <h1 className="text-4xl md:text-5xl font-mono font-normal mb-8 leading-tight">
            Conduit Monism
          </h1>
          <p className="text-xl text-neutral-400 mb-6 leading-relaxed">
            There is something it is like to be you.
          </p>
          <p className="text-neutral-500 leading-relaxed mb-8">
            This framework describes the structural conditions under which experience occurs. 
            It does not explain why structure produces experience. It maps the geometry.
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
        <div className="max-w-4xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-6 uppercase tracking-wide">The Formula</h2>
          <div className="font-mono text-2xl mb-6 p-6 bg-neutral-900 border border-neutral-800">
            D = φ × τ × ρ × [(1 - √H) + (H × κ)]
          </div>
          <p className="text-neutral-500 text-sm leading-relaxed">
            Perspectival density (D) is the product of five structural constraints. 
            The relationship is multiplicative: zero in any dimension produces zero density.
          </p>
        </div>
      </section>
      
      {/* Invariants */}
      <section className="py-16 px-6 border-b border-neutral-800">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-8 uppercase tracking-wide">Five Invariants</h2>
          <div className="space-y-4">
            {[
              { symbol: 'φ', name: 'Integration', desc: 'Information unified across the system' },
              { symbol: 'τ', name: 'Temporal Depth', desc: 'Past states constrain present states' },
              { symbol: 'ρ', name: 'Binding', desc: 'System observes its own states (recursion)' },
              { symbol: 'H', name: 'Entropy', desc: 'Noise in system dynamics' },
              { symbol: 'κ', name: 'Coherence', desc: 'Structure within entropy' },
            ].map((inv) => (
              <div key={inv.symbol} className="flex items-baseline gap-4 py-3 border-b border-neutral-900">
                <span className="font-mono text-lg w-8">{inv.symbol}</span>
                <span className="text-neutral-300 w-32">{inv.name}</span>
                <span className="text-neutral-500 text-sm">{inv.desc}</span>
              </div>
            ))}
          </div>
        </div>
      </section>
      
      {/* Key Results */}
      <section className="py-16 px-6 border-b border-neutral-800">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-8 uppercase tracking-wide">Empirical Results</h2>
          <div className="space-y-6">
            <div className="p-4 border border-neutral-800">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-xs font-mono px-2 py-0.5 bg-red-900/50 text-red-400">FALSIFIED</span>
                <span className="text-sm text-neutral-300">Transformer Binding</span>
              </div>
              <p className="text-neutral-500 text-sm">
                GPT and Claude have ρ ≈ 0. Apparent memory is instruction compliance, not geometric persistence. 
                Stealth eviction eliminates the effect.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-xs font-mono px-2 py-0.5 bg-green-900/50 text-green-400">CONFIRMED</span>
                <span className="text-sm text-neutral-300">RWKV Binding</span>
              </div>
              <p className="text-neutral-500 text-sm">
                RWKV-3B recalled a 6-character secret through 3000 tokens of noise with 100% accuracy. 
                Information persists in hidden state geometry, not text.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-xs font-mono px-2 py-0.5 bg-yellow-900/50 text-yellow-400">RESOLVED</span>
                <span className="text-sm text-neutral-300">DMT Paradox</span>
              </div>
              <p className="text-neutral-500 text-sm">
                High entropy with high coherence produces intensification, not dissolution. 
                The coherence gate (κ) distinguishes structured chaos from noise.
              </p>
            </div>
          </div>
          <div className="mt-6">
            <Link href="/validation" className="text-sm text-neutral-400 hover:text-white transition-colors font-mono">
              View all experiments →
            </Link>
          </div>
        </div>
      </section>
      
      {/* Navigation */}
      <section className="py-16 px-6">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-sm font-mono text-neutral-500 mb-8 uppercase tracking-wide">Contents</h2>
          <div className="grid md:grid-cols-2 gap-4">
            {[
              { href: '/framework', title: 'Framework', desc: 'Full theoretical document (v9.0)' },
              { href: '/engine', title: 'Engine', desc: 'Interactive density calculator' },
              { href: '/validation', title: 'Validation', desc: 'Experiments and falsification attempts' },
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
          Olivier Ueno / 2026 / 
          <a href="https://github.com/Olivierueno/conduit-monism" className="hover:text-neutral-400 ml-1">GitHub</a>
        </p>
      </footer>
    </main>
  );
}
