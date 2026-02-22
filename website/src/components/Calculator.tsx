'use client';

import { useState, useMemo, useEffect, useCallback } from 'react';
import { calculateDensity, presets, Invariants, Preset, findClosestAnimal, findClosestPreset, calculateSensitivity, calculateUncertainty } from '@/lib/engine';
import StateVisualization from './StateVisualization';

// Organic noise using multiple sine waves at different frequencies
function organicNoise(t: number, seed: number): number {
  return (
    Math.sin(t * 0.3 + seed) * 0.4 +
    Math.sin(t * 0.7 + seed * 1.7) * 0.3 +
    Math.sin(t * 1.1 + seed * 2.3) * 0.2 +
    Math.sin(t * 2.3 + seed * 3.1) * 0.1
  );
}

interface SliderProps {
  label: string;
  symbol: string;
  value: number;
  displayValue: number; // The animated display value
  onChange: (value: number) => void;
  isAnimating: boolean;
  sensitivity?: number; // ∂D/∂param - how much D changes per unit change
}

function Slider({ label, symbol, value, displayValue, onChange, isAnimating, sensitivity }: SliderProps) {
  // Normalize sensitivity for display (max bar width)
  const absSens = Math.abs(sensitivity ?? 0);
  const sensWidth = Math.min(100, absSens * 200); // scale so 0.5 fills the bar
  const sensColor = absSens < 0.05 ? 'bg-neutral-700' : absSens < 0.2 ? 'bg-amber-700' : 'bg-green-700';

  return (
    <div className="mb-4">
      <div className="flex justify-between items-center mb-1">
        <label className="text-sm text-neutral-400">
          <span className="font-mono">{symbol}</span> {label}
        </label>
        <div className="flex items-center gap-2">
          {sensitivity !== undefined && (
            <div className="flex items-center gap-1" title={`∂D/∂${symbol} = ${sensitivity.toFixed(4)}`}>
              <div className="w-12 h-1.5 bg-neutral-900 overflow-hidden">
                <div className={`h-full ${sensColor}`} style={{ width: `${sensWidth}%` }} />
              </div>
            </div>
          )}
          <span className="font-mono text-sm tabular-nums">{displayValue.toFixed(2)}</span>
        </div>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.01"
        value={isAnimating ? displayValue : value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
        className="w-full h-2 bg-neutral-900 appearance-none cursor-pointer slider border border-neutral-800"
      />
    </div>
  );
}

function DensityDisplay({ value, isZero, uncertainty }: { value: number; isZero: boolean; uncertainty: { dMin: number; dMax: number; sigma: number } }) {
  const showUncertainty = !isZero && uncertainty.sigma > 0.0001;
  return (
    <div className={`p-6 border ${isZero ? 'border-red-900 bg-red-950/20' : 'border-neutral-800 bg-neutral-900'}`}>
      <div className="text-xs font-mono text-neutral-500 mb-2 uppercase">Perspectival Density</div>
      <div className={`text-4xl font-mono tabular-nums ${isZero ? 'text-red-500' : 'text-white'}`}>
        {value.toFixed(4)}
      </div>
      {showUncertainty && (
        <div className="mt-2">
          <div className="text-xs font-mono text-neutral-600">
            ±{uncertainty.sigma.toFixed(4)} ({uncertainty.dMin.toFixed(3)} – {uncertainty.dMax.toFixed(3)})
          </div>
          {/* Visual uncertainty bar */}
          <div className="mt-1.5 h-1.5 bg-neutral-800 relative overflow-hidden" title="Uncertainty range at ±0.05 per parameter">
            <div
              className="absolute h-full bg-neutral-600"
              style={{
                left: `${uncertainty.dMin * 100}%`,
                width: `${Math.max(1, (uncertainty.dMax - uncertainty.dMin) * 100)}%`,
              }}
            />
            <div
              className="absolute h-full w-px bg-white"
              style={{ left: `${value * 100}%` }}
            />
          </div>
        </div>
      )}
      {isZero && (
        <div className="text-xs text-red-500 mt-2 font-mono">
          Zero in structural dimension produces zero density
        </div>
      )}
      {!isZero && value < 0.10 && (
        <div className="text-xs text-amber-600 mt-2 font-mono">
          Low D region: high degeneracy. Many distinct states share this density.
        </div>
      )}
    </div>
  );
}

function ClosestMatch({ invariants, activePreset }: { invariants: Invariants; activePreset: string | null }) {
  const closestAnimal = useMemo(() => findClosestAnimal(invariants), [invariants]);
  const closestOverall = useMemo(() => findClosestPreset(invariants), [invariants]);
  
  // Don't show if a preset is actively selected (user clicked a preset button)
  if (activePreset) return null;
  
  // Don't show if there's no match
  if (!closestAnimal || !closestOverall) return null;
  
  return (
    <div className="mt-4 p-4 border border-neutral-800 bg-neutral-900/50">
      <div className="text-xs font-mono text-neutral-500 mb-3 uppercase">Closest Match</div>
      
      {/* Closest animal */}
      <div className="mb-3">
        <div className="flex items-center justify-between">
          <span className="text-sm text-neutral-400">Animal:</span>
          <span className="text-sm text-neutral-200 font-mono">{closestAnimal.preset.name}</span>
        </div>
        <div className="flex items-center justify-between mt-1">
          <span className="text-xs text-neutral-600">D = {closestAnimal.density.toFixed(4)}</span>
          <span className="text-xs text-neutral-600">distance: {closestAnimal.distance.toFixed(3)}</span>
        </div>
      </div>
      
      {/* Closest overall (if different from animal) */}
      {closestOverall.preset.name !== closestAnimal.preset.name && (
        <div className="pt-3 border-t border-neutral-800">
          <div className="flex items-center justify-between">
            <span className="text-sm text-neutral-400">Overall:</span>
            <span className="text-sm text-neutral-200 font-mono">{closestOverall.preset.name}</span>
          </div>
          <div className="flex items-center justify-between mt-1">
            <span className="text-xs text-neutral-600">D = {closestOverall.density.toFixed(4)}</span>
            <span className="text-xs text-neutral-600">distance: {closestOverall.distance.toFixed(3)}</span>
          </div>
        </div>
      )}
    </div>
  );
}

export default function Calculator() {
  const [baseInvariants, setBaseInvariants] = useState<Invariants>({
    phi: 0.85,
    tau: 0.8,
    rho: 0.7,
    H: 0.35,
    kappa: 0.7,
  });
  
  const [activePreset, setActivePreset] = useState<string | null>("Human (Baseline Awake)");
  const [selectedCategory, setSelectedCategory] = useState<Preset['category'] | 'all'>('all');
  const [isAnimating, setIsAnimating] = useState(true);
  const [time, setTime] = useState(0);
  
  // Animation loop
  useEffect(() => {
    if (!isAnimating) return;
    
    let animationId: number;
    let lastTime = performance.now();
    
    const animate = (currentTime: number) => {
      const delta = (currentTime - lastTime) / 1000;
      lastTime = currentTime;
      setTime(t => t + delta);
      animationId = requestAnimationFrame(animate);
    };
    
    animationId = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(animationId);
  }, [isAnimating]);
  
  // Calculate modulated invariants - subtle drift around base values
  const modulatedInvariants = useMemo(() => {
    if (!isAnimating) return baseInvariants;
    
    const baseDrift = 0.015; // 1.5% max variance
    const sharedDrift = organicNoise(time, 0) * 0.005;
    
    // Structural invariants (phi, tau, rho) must remain 0 if they are 0 in baseInvariants
    // This prevents fluctuation when density should be zero
    return {
      phi: baseInvariants.phi === 0 ? 0 : Math.min(1, Math.max(0, baseInvariants.phi + organicNoise(time, 1.0) * baseDrift + sharedDrift)),
      tau: baseInvariants.tau === 0 ? 0 : Math.min(1, Math.max(0, baseInvariants.tau + organicNoise(time, 2.3) * baseDrift + sharedDrift)),
      rho: baseInvariants.rho === 0 ? 0 : Math.min(1, Math.max(0, baseInvariants.rho + organicNoise(time, 3.7) * baseDrift * 0.7 + sharedDrift)),
      H: Math.min(1, Math.max(0, baseInvariants.H + organicNoise(time, 4.1) * baseDrift * 1.2)),
      kappa: Math.min(1, Math.max(0, baseInvariants.kappa + organicNoise(time, 5.9) * baseDrift + sharedDrift * 0.5)),
    };
  }, [baseInvariants, time, isAnimating]);
  
  const result = useMemo(() => calculateDensity(modulatedInvariants), [modulatedInvariants]);
  const sensitivity = useMemo(() => calculateSensitivity(modulatedInvariants), [modulatedInvariants]);
  const uncertainty = useMemo(() => calculateUncertainty(modulatedInvariants, 0.05), [modulatedInvariants]);

  const hasStructuralZero = baseInvariants.phi === 0 || baseInvariants.tau === 0 || baseInvariants.rho === 0;
  
  const updateInvariant = (key: keyof Invariants, value: number) => {
    setBaseInvariants(prev => ({ ...prev, [key]: value }));
    setActivePreset(null);
  };
  
  const loadPreset = (preset: Preset) => {
    setBaseInvariants(preset.invariants);
    setActivePreset(preset.name);
  };
  
  const toggleAnimation = useCallback(() => {
    setIsAnimating(prev => !prev);
  }, []);
  
  const filteredPresets = selectedCategory === 'all' 
    ? presets 
    : presets.filter(p => p.category === selectedCategory);
  
  const categories: Array<{ value: Preset['category'] | 'all'; label: string }> = [
    { value: 'all', label: 'All' },
    { value: 'human', label: 'Human' },
    { value: 'animal', label: 'Animal' },
    { value: 'ai', label: 'AI' },
    { value: 'altered', label: 'Altered' },
    { value: 'pathological', label: 'Pathological' },
  ];
  
  return (
    <div className="max-w-5xl mx-auto">
      {/* Animation toggle */}
      <div className="flex justify-end mb-2">
        <button
          onClick={toggleAnimation}
          className="text-xs font-mono text-neutral-600 hover:text-neutral-400 transition-colors"
        >
          {isAnimating ? '◉ live' : '○ paused'}
        </button>
      </div>
      
      {/* Main interactive area - 3 columns on desktop */}
      <div className="grid md:grid-cols-3 gap-6">
        {/* Left: Sliders */}
        <div>
          <h3 className="text-xs font-mono text-neutral-500 mb-4 uppercase tracking-wide">Parameters</h3>
          <div className="p-4 border border-neutral-800">
            <Slider
              label="Integration"
              symbol="φ"
              value={baseInvariants.phi}
              displayValue={modulatedInvariants.phi}
              onChange={(v) => updateInvariant('phi', v)}
              isAnimating={isAnimating}
              sensitivity={sensitivity.phi}
            />
            <Slider
              label="Temporal Depth"
              symbol="τ"
              value={baseInvariants.tau}
              displayValue={modulatedInvariants.tau}
              onChange={(v) => updateInvariant('tau', v)}
              isAnimating={isAnimating}
              sensitivity={sensitivity.tau}
            />
            <Slider
              label="Binding"
              symbol="ρ"
              value={baseInvariants.rho}
              displayValue={modulatedInvariants.rho}
              onChange={(v) => updateInvariant('rho', v)}
              isAnimating={isAnimating}
              sensitivity={sensitivity.rho}
            />
            <Slider
              label="Entropy"
              symbol="H"
              value={baseInvariants.H}
              displayValue={modulatedInvariants.H}
              onChange={(v) => updateInvariant('H', v)}
              isAnimating={isAnimating}
              sensitivity={sensitivity.H}
            />
            <Slider
              label="Coherence"
              symbol="κ"
              value={baseInvariants.kappa}
              displayValue={modulatedInvariants.kappa}
              onChange={(v) => updateInvariant('kappa', v)}
              isAnimating={isAnimating}
              sensitivity={sensitivity.kappa}
            />
          </div>
          
          {/* Breakdown - uses modulated values */}
          <div className="mt-4 p-4 border border-neutral-800 font-mono text-sm">
            <div className="text-xs text-neutral-600 mb-2 uppercase">Formula Breakdown</div>
            <div className="flex justify-between text-neutral-500 mb-1">
              <span>φ × τ × ρ</span>
              <span className="tabular-nums">{result.structuralBase.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-neutral-500 mb-1">
              <span>1 - √H</span>
              <span className="tabular-nums">{result.entropyPenalty.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-neutral-500 mb-1">
              <span>H × κ</span>
              <span className="tabular-nums">{result.coherenceRecovery.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-neutral-400 pt-2 border-t border-neutral-800">
              <span>Modulator</span>
              <span className="tabular-nums">{result.entropyModulator.toFixed(4)}</span>
            </div>
          </div>

        </div>

        {/* Center: Visualization (prominent) */}
        <div>
          <h3 className="text-xs font-mono text-neutral-500 mb-4 uppercase tracking-wide">State Visualization</h3>
          <StateVisualization invariants={modulatedInvariants} isAnimating={isAnimating} />

          {/* Sensitivity legend */}
          <div className="mt-4 p-4 border border-neutral-800 font-mono text-sm">
            <div className="text-xs text-neutral-600 mb-2 uppercase">Sensitivity (∂D/∂param)</div>
            <div className="text-xs text-neutral-700 mb-2">Bars show how much D changes per unit change in each parameter.</div>
            <div className="flex items-center gap-3 text-xs text-neutral-600">
              <span className="flex items-center gap-1"><span className="w-3 h-1.5 bg-neutral-700 inline-block"></span> low</span>
              <span className="flex items-center gap-1"><span className="w-3 h-1.5 bg-amber-700 inline-block"></span> mid</span>
              <span className="flex items-center gap-1"><span className="w-3 h-1.5 bg-green-700 inline-block"></span> high</span>
            </div>
          </div>
        </div>
        
        {/* Right: Output & Interpretation */}
        <div>
          <h3 className="text-xs font-mono text-neutral-500 mb-4 uppercase tracking-wide">Output</h3>
          <DensityDisplay value={result.D} isZero={hasStructuralZero} uncertainty={uncertainty} />
          
          {/* Closest Match */}
          <ClosestMatch invariants={modulatedInvariants} activePreset={activePreset} />
          
          {/* Interpretation */}
          <div className="mt-4 p-4 border border-neutral-800">
            <div className="text-xs text-neutral-600 mb-2 uppercase">Interpretation</div>
            <p className="text-sm text-neutral-500">{result.interpretation}</p>
          </div>
        </div>
      </div>
      
      {/* Presets */}
      <div className="mt-8">
        <div className="flex items-center justify-between mb-4 flex-wrap gap-2">
          <h3 className="text-xs font-mono text-neutral-500 uppercase tracking-wide">Presets</h3>
          <div className="flex gap-1 flex-wrap">
            {categories.map(cat => (
              <button
                key={cat.value}
                onClick={() => setSelectedCategory(cat.value)}
                className={`px-2 py-1 text-xs font-mono transition-colors ${
                  selectedCategory === cat.value
                    ? 'bg-white text-black'
                    : 'text-neutral-500 hover:text-white'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>
        
        {/* Confidence legend */}
        <div className="flex items-center gap-4 mb-3 text-xs font-mono text-neutral-500">
          <span className="flex items-center gap-1.5">
            <span className="inline-block w-2 h-2 rounded-full bg-green-500"></span>
            calibrated
          </span>
          <span className="flex items-center gap-1.5">
            <span className="inline-block w-2 h-2 rounded-full bg-amber-500"></span>
            estimated
          </span>
          <span className="flex items-center gap-1.5">
            <span className="inline-block w-2 h-2 rounded-full bg-red-400"></span>
            speculative
          </span>
          <span className="text-neutral-600 ml-1" title="Calibrated: grounded in peer-reviewed human neuroimaging data. Estimated: some empirical grounding from clinical/pharmacological studies. Speculative: extrapolated from comparative neuroscience literature.">[?]</span>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-2 max-h-96 overflow-y-auto">
          {filteredPresets.map(preset => {
            const d = calculateDensity(preset.invariants).D;
            const confidenceColor = preset.confidence === 'calibrated'
              ? 'bg-green-500'
              : preset.confidence === 'estimated'
                ? 'bg-amber-500'
                : 'bg-red-400';
            return (
              <button
                key={preset.name}
                onClick={() => loadPreset(preset)}
                className={`p-3 text-left border transition-colors ${
                  activePreset === preset.name
                    ? 'border-white bg-neutral-900'
                    : 'border-neutral-800 hover:border-neutral-600'
                }`}
              >
                <div className="flex items-center gap-1.5">
                  <span className={`inline-block w-1.5 h-1.5 rounded-full flex-shrink-0 ${confidenceColor}`}></span>
                  <span className="text-xs text-neutral-400 truncate">{preset.name}</span>
                </div>
                <div className="font-mono text-sm mt-1">{d.toFixed(3)}</div>
              </button>
            );
          })}
        </div>

        {activePreset && (() => {
          const selected = presets.find(p => p.name === activePreset);
          if (!selected) return null;
          return (
            <div className="mt-4 space-y-2">
              <div className="p-4 border border-neutral-800">
                <p className="text-sm text-neutral-500">
                  {selected.description}
                </p>
              </div>
              {selected.confidence === 'speculative' && (
                <div className="p-3 border border-red-900/50 bg-red-950/10">
                  <p className="text-xs text-red-400/90">
                    These values are estimates based on comparative neuroscience literature. They are NOT direct measurements. Treat as hypotheses, not facts.
                  </p>
                </div>
              )}
            </div>
          );
        })()}
      </div>
    </div>
  );
}
