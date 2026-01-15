'use client';

import { useState, useMemo } from 'react';
import { calculateDensity, presets, Invariants, Preset, findClosestAnimal, findClosestPreset } from '@/lib/engine';

interface SliderProps {
  label: string;
  symbol: string;
  value: number;
  onChange: (value: number) => void;
}

function Slider({ label, symbol, value, onChange }: SliderProps) {
  return (
    <div className="mb-4">
      <div className="flex justify-between items-center mb-1">
        <label className="text-sm text-neutral-400">
          <span className="font-mono">{symbol}</span> {label}
        </label>
        <span className="font-mono text-sm">{value.toFixed(2)}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.01"
        value={value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
        className="w-full h-2 bg-neutral-900 appearance-none cursor-pointer slider border border-neutral-800"
      />
    </div>
  );
}

function DensityDisplay({ value, isZero }: { value: number; isZero: boolean }) {
  return (
    <div className={`p-6 border ${isZero ? 'border-red-900 bg-red-950/20' : 'border-neutral-800 bg-neutral-900'}`}>
      <div className="text-xs font-mono text-neutral-500 mb-2 uppercase">Perspectival Density</div>
      <div className={`text-4xl font-mono ${isZero ? 'text-red-500' : 'text-white'}`}>
        {value.toFixed(4)}
      </div>
      {isZero && (
        <div className="text-xs text-red-500 mt-2 font-mono">
          Zero in structural dimension produces zero density
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
  const [invariants, setInvariants] = useState<Invariants>({
    phi: 0.85,
    tau: 0.8,
    rho: 0.7,
    H: 0.35,
    kappa: 0.7,
  });
  
  const [activePreset, setActivePreset] = useState<string | null>("Human (Baseline Awake)");
  const [selectedCategory, setSelectedCategory] = useState<Preset['category'] | 'all'>('all');
  
  const result = useMemo(() => calculateDensity(invariants), [invariants]);
  
  const hasStructuralZero = invariants.phi === 0 || invariants.tau === 0 || invariants.rho === 0;
  
  const updateInvariant = (key: keyof Invariants, value: number) => {
    setInvariants(prev => ({ ...prev, [key]: value }));
    setActivePreset(null); // Clear active preset when manually adjusting
  };
  
  const loadPreset = (preset: Preset) => {
    setInvariants(preset.invariants);
    setActivePreset(preset.name);
  };
  
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
    <div className="max-w-4xl mx-auto">
      <div className="grid md:grid-cols-2 gap-8">
        {/* Sliders */}
        <div>
          <h3 className="text-xs font-mono text-neutral-500 mb-4 uppercase tracking-wide">Parameters</h3>
          <div className="p-4 border border-neutral-800">
            <Slider
              label="Integration"
              symbol="φ"
              value={invariants.phi}
              onChange={(v) => updateInvariant('phi', v)}
            />
            <Slider
              label="Temporal Depth"
              symbol="τ"
              value={invariants.tau}
              onChange={(v) => updateInvariant('tau', v)}
            />
            <Slider
              label="Binding"
              symbol="ρ"
              value={invariants.rho}
              onChange={(v) => updateInvariant('rho', v)}
            />
            <Slider
              label="Entropy"
              symbol="H"
              value={invariants.H}
              onChange={(v) => updateInvariant('H', v)}
            />
            <Slider
              label="Coherence"
              symbol="κ"
              value={invariants.kappa}
              onChange={(v) => updateInvariant('kappa', v)}
            />
          </div>
        </div>
        
        {/* Results */}
        <div>
          <h3 className="text-xs font-mono text-neutral-500 mb-4 uppercase tracking-wide">Output</h3>
          <DensityDisplay value={result.D} isZero={hasStructuralZero} />
          
          {/* Closest Match */}
          <ClosestMatch invariants={invariants} activePreset={activePreset} />
          
          {/* Breakdown */}
          <div className="mt-4 p-4 border border-neutral-800 font-mono text-sm">
            <div className="flex justify-between text-neutral-500 mb-1">
              <span>φ × τ × ρ</span>
              <span>{result.structuralBase.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-neutral-500 mb-1">
              <span>1 - √H</span>
              <span>{result.entropyPenalty.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-neutral-500 mb-1">
              <span>H × κ</span>
              <span>{result.coherenceRecovery.toFixed(4)}</span>
            </div>
            <div className="flex justify-between text-neutral-400 pt-2 border-t border-neutral-800">
              <span>Modulator</span>
              <span>{result.entropyModulator.toFixed(4)}</span>
            </div>
          </div>
          
          {/* Interpretation */}
          <div className="mt-4 p-4 border border-neutral-800">
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
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-2 max-h-96 overflow-y-auto">
          {filteredPresets.map(preset => {
            const d = calculateDensity(preset.invariants).D;
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
                <div className="text-xs text-neutral-400 truncate">{preset.name}</div>
                <div className="font-mono text-sm mt-1">{d.toFixed(3)}</div>
              </button>
            );
          })}
        </div>
        
        {activePreset && (
          <div className="mt-4 p-4 border border-neutral-800">
            <p className="text-sm text-neutral-500">
              {presets.find(p => p.name === activePreset)?.description}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
