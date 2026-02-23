import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Empirical Calibration',
  description: 'Grounding the five invariants in measurable neuroscience. How each framework variable maps to empirical measurements from consciousness research.',
  alternates: { canonical: '/calibration' },
  keywords: [
    'PCI',
    'perturbational complexity index',
    'Lempel-Ziv complexity',
    'consciousness measurement',
    'neural correlates',
    'empirical consciousness',
    'calibration',
  ],
  openGraph: {
    title: 'Empirical Calibration | Conduit Monism',
    description: 'Grounding the five invariants in measurable neuroscience. How each framework variable maps to empirical measurements from consciousness research.',
  },
};

export default function CalibrationPage() {
  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-5xl mx-auto">
        <div className="mb-12">
          <h1 className="text-2xl font-mono mb-4">Empirical Calibration</h1>
          <p className="text-neutral-500 max-w-2xl">
            Grounding the five invariants in measurable neuroscience. This page documents
            how each framework variable maps to empirical measurements from consciousness research.
          </p>
        </div>

        {/* Overview */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Overview</h2>
          <div className="p-4 border border-neutral-800 bg-neutral-900/50">
            <p className="text-sm text-neutral-400 mb-4">
              The calibration system transforms Conduit Monism from a theoretical framework into an
              empirically-testable model. Each of the five invariants is mapped to specific measurement
              proxies from peer-reviewed neuroscience literature.
            </p>
            <div className="grid md:grid-cols-2 gap-4 text-xs">
              <div className="p-3 border border-neutral-700 bg-neutral-800/50">
                <div className="text-green-400 mb-1">HIGH CONFIDENCE</div>
                <div className="text-neutral-400">Direct measurement mapping with strong literature support</div>
              </div>
              <div className="p-3 border border-neutral-700 bg-neutral-800/50">
                <div className="text-yellow-400 mb-1">MODERATE CONFIDENCE</div>
                <div className="text-neutral-400">Indirect mapping requiring interpretation</div>
              </div>
              <div className="p-3 border border-neutral-700 bg-neutral-800/50">
                <div className="text-orange-400 mb-1">LOW CONFIDENCE</div>
                <div className="text-neutral-400">Phenomenological inference or extrapolation</div>
              </div>
              <div className="p-3 border border-neutral-700 bg-neutral-800/50">
                <div className="text-red-400 mb-1">THEORETICAL</div>
                <div className="text-neutral-400">No empirical anchor available</div>
              </div>
            </div>
          </div>
        </section>

        {/* Variable Mappings */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Variable Mappings</h2>

          {/* Rho - PCI */}
          <div className="p-4 border border-green-900/50 bg-green-950/10 mb-4">
            <div className="flex items-baseline justify-between mb-2">
              <div className="font-mono text-neutral-300">ρ (Binding) ← PCI</div>
              <div className="text-xs text-green-400">HIGH CONFIDENCE</div>
            </div>
            <p className="text-neutral-500 text-sm mb-3">
              Binding maps directly to the Perturbational Complexity Index (PCI). PCI measures
              how a TMS perturbation propagates through the brain, creating complex, differentiated
              &quot;echoes.&quot; This captures recursive self-reference: the system observing its own states.
            </p>
            <div className="text-xs text-neutral-600 mb-3">
              <strong>Mapping:</strong> ρ = PCI (direct)
            </div>
            <div className="grid md:grid-cols-2 gap-3 text-xs">
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Wakefulness</div>
                <div className="font-mono text-green-400">PCI: 0.44-0.67 → ρ = 0.65</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Propofol Anesthesia</div>
                <div className="font-mono text-red-400">PCI: 0.12-0.31 → ρ = 0.24</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Ketamine</div>
                <div className="font-mono text-yellow-400">PCI: 0.35-0.55 → ρ = 0.44</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">PCI* Threshold</div>
                <div className="font-mono text-neutral-300">0.31 (100% accuracy)</div>
              </div>
            </div>
            <div className="mt-3 text-xs text-neutral-600">
              <strong>Key Citations:</strong> Casali et al. (2013), Casarotto et al. (2016), Sarasso et al. (2015)
            </div>
          </div>

          {/* H - LZc */}
          <div className="p-4 border border-green-900/50 bg-green-950/10 mb-4">
            <div className="flex items-baseline justify-between mb-2">
              <div className="font-mono text-neutral-300">H (Entropy) ← LZc</div>
              <div className="text-xs text-green-400">HIGH CONFIDENCE</div>
            </div>
            <p className="text-neutral-500 text-sm mb-3">
              Entropy maps to Lempel-Ziv Complexity (LZc), a measure of signal compressibility
              that captures the unpredictability of neural dynamics. Higher LZc indicates more
              entropy in the system.
            </p>
            <div className="text-xs text-neutral-600 mb-3">
              <strong>Mapping:</strong> H = 0.5 × (1 + percent_change_from_baseline)
            </div>
            <div className="grid md:grid-cols-2 gap-3 text-xs">
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Wakefulness (baseline)</div>
                <div className="font-mono text-neutral-300">H = 0.50</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Propofol (-30%)</div>
                <div className="font-mono text-blue-400">H = 0.35</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Psilocybin (+20%)</div>
                <div className="font-mono text-purple-400">H = 0.60</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Ketamine (+10%)</div>
                <div className="font-mono text-yellow-400">H = 0.55</div>
              </div>
            </div>
            <div className="mt-3 text-xs text-neutral-600">
              <strong>Key Citations:</strong> Schartner et al. (2015, 2017), Carhart-Harris et al. (2014)
            </div>
          </div>

          {/* Tau - Temporal Window */}
          <div className="p-4 border border-yellow-900/50 bg-yellow-950/10 mb-4">
            <div className="flex items-baseline justify-between mb-2">
              <div className="font-mono text-neutral-300">τ (Temporal Depth) ← Temporal Integration Window</div>
              <div className="text-xs text-yellow-400">MODERATE CONFIDENCE</div>
            </div>
            <p className="text-neutral-500 text-sm mb-3">
              Temporal depth maps to the temporal integration window, the duration over which
              the brain binds information into a unified &quot;now.&quot; The baseline window for waking
              adults is approximately 2-3 seconds (Pöppel 1997).
            </p>
            <div className="text-xs text-neutral-600 mb-3">
              <strong>Mapping:</strong> τ = window_ms / 3000ms (normalized to baseline)
            </div>
            <div className="grid md:grid-cols-2 gap-3 text-xs">
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Normal waking</div>
                <div className="font-mono text-neutral-300">τ = 0.75 (baseline)</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Anesthesia (collapsed)</div>
                <div className="font-mono text-red-400">τ = 0.10</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Meditation (expanded)</div>
                <div className="font-mono text-green-400">τ = 0.80</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">DMT (&quot;eternity&quot;)</div>
                <div className="font-mono text-purple-400">τ = 0.90</div>
              </div>
            </div>
            <div className="mt-3 text-xs text-neutral-600">
              <strong>Key Citations:</strong> Pöppel (1997), Wittmann (2015)
            </div>
          </div>

          {/* Phi - Global Efficiency + Multi-Metric */}
          <div className="p-4 border border-green-900/50 bg-green-950/10 mb-4">
            <div className="flex items-baseline justify-between mb-2">
              <div className="font-mono text-neutral-300">φ (Integration) ← E_glob + PCI + ISD</div>
              <div className="text-xs text-green-400">MODERATE-HIGH CONFIDENCE</div>
            </div>
            <p className="text-neutral-500 text-sm mb-3">
              Integration maps to a multi-metric approach combining Global Efficiency (E_glob),
              Perturbational Complexity Index (PCI), and Integration-Segregation Difference (ISD).
              <strong> Extended validation (AT11, 2026-01-20)</strong> confirmed rank-order preservation
              across 5+ states with 4/4 independent AI support.
            </p>
            <div className="text-xs text-neutral-600 mb-3">
              <strong>Primary Mapping:</strong> φ = normalized_global_efficiency (E_glob)
            </div>
            <div className="grid md:grid-cols-2 gap-3 text-xs">
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Jhana / Peak States</div>
                <div className="font-mono text-purple-400">φ = 0.90-1.00 (hyper-integrated)</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Wakefulness (baseline)</div>
                <div className="font-mono text-neutral-300">φ = 0.80</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">REM Sleep</div>
                <div className="font-mono text-blue-400">φ = 0.60</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Propofol</div>
                <div className="font-mono text-red-400">φ = 0.25</div>
              </div>
            </div>
            <div className="mt-3 text-xs text-green-500/70">
              <strong>Key Discovery:</strong> Hyper-integrated states (Jhana, psychedelics) exceed baseline wakefulness in E_glob
            </div>
            <div className="mt-2 text-xs text-neutral-600">
              <strong>Key Citations:</strong> Liu et al. (2013), Kim et al. (2018), Jang et al. (2024), Kan et al. (2025)
            </div>
          </div>

          {/* Kappa - MSE */}
          <div className="p-4 border border-yellow-900/50 bg-yellow-950/10 mb-4">
            <div className="flex items-baseline justify-between mb-2">
              <div className="font-mono text-neutral-300">κ (Coherence) ← Multi-Scale Entropy Slope</div>
              <div className="text-xs text-yellow-400">MODERATE CONFIDENCE</div>
            </div>
            <p className="text-neutral-500 text-sm mb-3">
              Coherence maps to the slope of entropy across timescales. Fractal signals maintain
              complexity when &quot;zoomed out&quot; (flat MSE slope → high κ), while random noise loses
              complexity at larger scales (steep MSE drop → low κ). <strong>Validated in AT07</strong> with
              r = 0.987 correlation between phenomenological κ and MSE-derived κ.
            </p>
            <div className="text-xs text-neutral-600 mb-3">
              <strong>Mapping:</strong> κ = 1 - |normalized_MSE_slope| (Costa et al. 2002, 2005)
            </div>
            <div className="grid md:grid-cols-2 gap-3 text-xs">
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Baseline waking</div>
                <div className="font-mono text-neutral-300">κ = 0.65 (moderate slope)</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Seizure (non-fractal)</div>
                <div className="font-mono text-red-400">κ = 0.10 (steep slope)</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">Flow state (fractal)</div>
                <div className="font-mono text-green-400">κ = 0.75 (flat slope)</div>
              </div>
              <div className="p-2 bg-neutral-900/50 border border-neutral-800">
                <div className="text-neutral-400">DMT (scale-invariant)</div>
                <div className="font-mono text-purple-400">κ = 0.90 (near-flat)</div>
              </div>
            </div>
            <div className="mt-3 text-xs text-neutral-600">
              <strong>Key Citations:</strong> Costa et al. (2002, 2005), Schartner et al. (2017)
            </div>
          </div>
        </section>

        {/* Critical Threshold */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Critical Threshold: PCI*</h2>
          <div className="p-4 border border-neutral-800 bg-neutral-900/50">
            <p className="text-sm text-neutral-400 mb-4">
              Casarotto et al. (2016) established PCI* = 0.31 as the threshold that separates
              conscious from unconscious states with <strong>100% accuracy</strong> across a large
              clinical dataset including:
            </p>
            <ul className="text-sm text-neutral-500 space-y-1 ml-4 list-disc mb-4">
              <li>Healthy awake subjects</li>
              <li>Patients under various anesthetics (propofol, xenon, midazolam, ketamine)</li>
              <li>Patients in minimally conscious state (MCS)</li>
              <li>Patients in vegetative state / unresponsive wakefulness syndrome (VS/UWS)</li>
              <li>Locked-in syndrome patients (conscious but paralyzed)</li>
            </ul>
            <div className="p-3 border border-green-900/50 bg-green-950/20 text-sm">
              <div className="text-green-400 mb-1 font-mono">Implication for Conduit Monism:</div>
              <div className="text-neutral-400">
                Since ρ maps to PCI, the threshold ρ = 0.31 provides an empirically-grounded
                boundary for consciousness. Systems with ρ &lt; 0.31 are predicted to be unconscious.
              </div>
            </div>
          </div>
        </section>

        {/* Calibrated States */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Calibrated States</h2>
          <div className="overflow-x-auto">
            <table className="w-full text-xs border border-neutral-800">
              <thead>
                <tr className="bg-neutral-900">
                  <th className="p-2 text-left border-b border-neutral-800">State</th>
                  <th className="p-2 text-center border-b border-neutral-800">φ</th>
                  <th className="p-2 text-center border-b border-neutral-800">τ</th>
                  <th className="p-2 text-center border-b border-neutral-800">ρ</th>
                  <th className="p-2 text-center border-b border-neutral-800">H</th>
                  <th className="p-2 text-center border-b border-neutral-800">κ</th>
                  <th className="p-2 text-center border-b border-neutral-800">D</th>
                  <th className="p-2 text-left border-b border-neutral-800">Conf.</th>
                </tr>
              </thead>
              <tbody className="text-neutral-400">
                <tr className="border-b border-neutral-800/50">
                  <td className="p-2 font-mono">DMT</td>
                  <td className="p-2 text-center">0.85</td>
                  <td className="p-2 text-center">0.90</td>
                  <td className="p-2 text-center">0.70</td>
                  <td className="p-2 text-center">0.70</td>
                  <td className="p-2 text-center">0.90</td>
                  <td className="p-2 text-center text-purple-400 font-mono">0.425</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr className="border-b border-neutral-800/50">
                  <td className="p-2 font-mono">Meditation</td>
                  <td className="p-2 text-center">0.85</td>
                  <td className="p-2 text-center">0.80</td>
                  <td className="p-2 text-center">0.70</td>
                  <td className="p-2 text-center">0.40</td>
                  <td className="p-2 text-center">0.80</td>
                  <td className="p-2 text-center text-green-400 font-mono">0.327</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr className="border-b border-neutral-800/50">
                  <td className="p-2 font-mono">Flow</td>
                  <td className="p-2 text-center">0.90</td>
                  <td className="p-2 text-center">0.70</td>
                  <td className="p-2 text-center">0.65</td>
                  <td className="p-2 text-center">0.55</td>
                  <td className="p-2 text-center">0.75</td>
                  <td className="p-2 text-center text-green-400 font-mono">0.275</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr className="border-b border-neutral-800/50 bg-neutral-900/30">
                  <td className="p-2 font-mono">Wakefulness</td>
                  <td className="p-2 text-center">0.80</td>
                  <td className="p-2 text-center">0.75</td>
                  <td className="p-2 text-center">0.65</td>
                  <td className="p-2 text-center">0.50</td>
                  <td className="p-2 text-center">0.65</td>
                  <td className="p-2 text-center text-neutral-300 font-mono">0.241</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr className="border-b border-neutral-800/50">
                  <td className="p-2 font-mono">Psilocybin</td>
                  <td className="p-2 text-center">0.70</td>
                  <td className="p-2 text-center">0.65</td>
                  <td className="p-2 text-center">0.55</td>
                  <td className="p-2 text-center">0.60</td>
                  <td className="p-2 text-center">0.85</td>
                  <td className="p-2 text-center text-purple-400 font-mono">0.184</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr className="border-b border-neutral-800/50">
                  <td className="p-2 font-mono">Ketamine</td>
                  <td className="p-2 text-center">0.50</td>
                  <td className="p-2 text-center">0.50</td>
                  <td className="p-2 text-center">0.44</td>
                  <td className="p-2 text-center">0.55</td>
                  <td className="p-2 text-center">0.80</td>
                  <td className="p-2 text-center text-yellow-400 font-mono">0.077</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr className="border-b border-neutral-800/50">
                  <td className="p-2 font-mono">REM Sleep</td>
                  <td className="p-2 text-center">0.60</td>
                  <td className="p-2 text-center">0.50</td>
                  <td className="p-2 text-center">0.45</td>
                  <td className="p-2 text-center">0.55</td>
                  <td className="p-2 text-center">0.55</td>
                  <td className="p-2 text-center text-blue-400 font-mono">0.076</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr className="border-b border-neutral-800/50">
                  <td className="p-2 font-mono">NREM N3</td>
                  <td className="p-2 text-center">0.40</td>
                  <td className="p-2 text-center">0.15</td>
                  <td className="p-2 text-center">0.23</td>
                  <td className="p-2 text-center">0.40</td>
                  <td className="p-2 text-center">0.30</td>
                  <td className="p-2 text-center text-blue-400 font-mono">0.007</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
                <tr>
                  <td className="p-2 font-mono">Propofol</td>
                  <td className="p-2 text-center">0.25</td>
                  <td className="p-2 text-center">0.10</td>
                  <td className="p-2 text-center">0.24</td>
                  <td className="p-2 text-center">0.35</td>
                  <td className="p-2 text-center">0.20</td>
                  <td className="p-2 text-center text-red-400 font-mono">0.003</td>
                  <td className="p-2 text-orange-400">LOW</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p className="text-xs text-neutral-600 mt-3">
            <strong>Note:</strong> Confidence is limited by the least-confident parameter. With κ upgraded to MODERATE (v9.3.2),
            φ is now the primary limiting factor for most states.
          </p>
        </section>

        {/* Key Findings */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Key Findings</h2>
          <div className="space-y-4">
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">1. Zero-Elimination via ρ</div>
              <p className="text-sm text-neutral-500">
                Non-biological systems (corporations, weather, internet) have ρ = 0 because they
                lack neural substrates and recursive self-reference. The multiplicative formula
                ensures D = 0 regardless of other parameters.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">2. Coherence Rescues Structured Entropy</div>
              <p className="text-sm text-neutral-500">
                DMT&apos;s high entropy (H = 0.70) is &quot;rescued&quot; by high coherence (κ = 0.90), yielding
                D = 0.425. Seizure&apos;s high entropy with low coherence (κ = 0.15) yields D near zero.
                The formula correctly distinguishes structured from random chaos.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">3. Phenomenological Alignment</div>
              <p className="text-sm text-neutral-500">
                Calibrated densities match phenomenological reports: DMT (&quot;more real than real&quot;)
                exceeds wakefulness; flow states and meditation exceed baseline; anesthesia
                approaches zero. The formula captures qualitative distinctions.
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <div className="font-mono text-neutral-300 mb-2">4. Ketamine Paradox</div>
              <p className="text-sm text-neutral-500">
                Ketamine maintains near-waking PCI (ρ = 0.44) despite producing unresponsiveness.
                This explains &quot;dissociative&quot; anesthesia: the binding is preserved (subjective
                experiences occur) even though behavior is absent.
              </p>
            </div>
          </div>
        </section>

        {/* Limitations */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Limitations</h2>
          <div className="p-4 border border-yellow-900/50 bg-yellow-950/10">
            <ul className="text-sm text-yellow-500/80 space-y-2 ml-4 list-disc">
              <li>Formula predicts structural MAGNITUDE, not VALENCE (positive vs negative experience)</li>
              <li>Psychedelic state values are extrapolated from limited psilocybin/ketamine data</li>
              <li>Animal and AI values remain theoretical (no PCI measurements possible)</li>
              <li>Within-state variability is significant but not captured</li>
              <li className="text-green-500/80">φ (Integration) now multi-metric anchored (AT11, 4/4 AI support), upgraded to MODERATE-HIGH</li>
              <li className="text-green-500/80">κ (Coherence) validated via MSE (AT07, r = 0.987), MODERATE</li>
            </ul>
          </div>
        </section>

        {/* References */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Key References</h2>
          <div className="p-4 border border-neutral-800 bg-neutral-900/50">
            <ul className="text-xs text-neutral-500 space-y-2">
              <li>Casali et al. (2013) - A theoretically based index of consciousness (PCI)</li>
              <li>Casarotto et al. (2016) - Stratification of consciousness using PCI</li>
              <li>Sarasso et al. (2015) - Consciousness and complexity during anesthesia</li>
              <li>Schartner et al. (2015, 2017) - LZc and psychedelics</li>
              <li>Carhart-Harris et al. (2014) - Entropic brain hypothesis</li>
              <li>Costa et al. (2002, 2005) - Multi-Scale Entropy (MSE)</li>
              <li>Ferrarelli et al. (2010) - Breakdown of connectivity under anesthesia</li>
              <li>Pöppel (1997) - Temporal integration window</li>
              <li>Wittmann (2015) - Time perception in altered states</li>
            </ul>
          </div>
        </section>
      </div>
    </main>
  );
}
