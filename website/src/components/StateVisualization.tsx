'use client';

import { useMemo, useState, useEffect, useCallback } from 'react';
import { Invariants, calculateDensity } from '@/lib/engine';

interface StateVisualizationProps {
  invariants: Invariants;
}

// Smooth noise function for organic movement
function smoothNoise(t: number, seed: number): number {
  const x = Math.sin(t * 0.7 + seed) * 0.5 + 
            Math.sin(t * 1.3 + seed * 2) * 0.3 + 
            Math.sin(t * 2.1 + seed * 3) * 0.2;
  return x;
}

export default function StateVisualization({ invariants }: StateVisualizationProps) {
  const [isAnimating, setIsAnimating] = useState(true);
  const [time, setTime] = useState(0);
  const [burst, setBurst] = useState(0); // 0-1, decays over time
  
  // Animation loop
  useEffect(() => {
    if (!isAnimating) return;
    
    let animationId: number;
    let lastTime = performance.now();
    
    const animate = (currentTime: number) => {
      const delta = (currentTime - lastTime) / 1000; // seconds
      lastTime = currentTime;
      
      setTime(t => t + delta);
      setBurst(b => Math.max(0, b - delta * 0.5)); // Decay burst over 2 seconds
      
      animationId = requestAnimationFrame(animate);
    };
    
    animationId = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(animationId);
  }, [isAnimating]);
  
  // Random bursts of "consciousness"
  useEffect(() => {
    if (!isAnimating) return;
    
    const triggerBurst = () => {
      // Random interval between 3-8 seconds
      const nextBurst = 3000 + Math.random() * 5000;
      
      const timeout = setTimeout(() => {
        setBurst(0.3 + Math.random() * 0.7); // Random intensity 0.3-1.0
        triggerBurst();
      }, nextBurst);
      
      return () => clearTimeout(timeout);
    };
    
    const cleanup = triggerBurst();
    return cleanup;
  }, [isAnimating]);
  
  // Calculate modulated invariants (subtle drift around base values)
  const modulatedInvariants = useMemo(() => {
    const driftAmount = 0.03; // Max 3% drift
    const burstBoost = burst * 0.1; // Burst adds up to 10%
    
    return {
      phi: Math.min(1, Math.max(0, invariants.phi + smoothNoise(time, 1) * driftAmount + burstBoost)),
      tau: Math.min(1, Math.max(0, invariants.tau + smoothNoise(time, 2) * driftAmount + burstBoost * 0.5)),
      rho: Math.min(1, Math.max(0, invariants.rho + smoothNoise(time, 3) * driftAmount * 0.5)), // Less drift on binding
      H: Math.min(1, Math.max(0, invariants.H + smoothNoise(time, 4) * driftAmount * 2)), // More drift on entropy
      kappa: Math.min(1, Math.max(0, invariants.kappa + smoothNoise(time, 5) * driftAmount)),
    };
  }, [invariants, time, burst]);
  
  const result = useMemo(() => calculateDensity(modulatedInvariants), [modulatedInvariants]);
  const baseResult = useMemo(() => calculateDensity(invariants), [invariants]);
  const { phi, tau, rho, H, kappa } = modulatedInvariants;
  
  // Calculate visual properties
  const hasStructuralZero = invariants.phi === 0 || invariants.tau === 0 || invariants.rho === 0;
  const density = result.D;
  
  // Brightness based on density
  const brightness = Math.max(0.1, density);
  
  // Stability based on binding (rho)
  const flickerIntensity = rho < 0.2 ? (0.2 - rho) * 5 : 0;
  
  // Size based on integration (phi)
  const size = 60 + (phi * 80);
  
  // Blur based on entropy without coherence
  const effectiveNoise = H * (1 - kappa);
  const blur = effectiveNoise * 20;
  
  // Color
  const hue = H > 0.5 && kappa > 0.5 ? 280 : 200;
  const saturation = H > 0.5 ? (kappa * 100) : 20;
  
  // Burst visual effect
  const burstGlow = burst * 30;
  const burstScale = 1 + burst * 0.15;
  
  // Pulse animation based on temporal depth
  const pulseScale = tau > 0.5 ? 1 + (tau - 0.5) * 0.1 : 1;
  
  // Combined scale
  const totalScale = pulseScale * burstScale;
  
  // Breathing animation
  const breathe = 1 + Math.sin(time * 0.5) * 0.02;
  
  const toggleAnimation = useCallback(() => {
    setIsAnimating(prev => !prev);
  }, []);
  
  return (
    <div className="relative border border-neutral-800">
      {/* State visualization */}
      <div className="h-64 bg-black flex items-center justify-center overflow-hidden relative">
        {/* Background */}
        <div 
          className="absolute inset-0 opacity-10"
          style={{
            backgroundImage: 'radial-gradient(circle at center, transparent 0%, black 70%)',
          }}
        />
        
        {hasStructuralZero ? (
          // Zero state - collapsed
          <div className="text-center z-10">
            <div 
              className="w-3 h-3 rounded-full bg-neutral-800 mx-auto mb-4 animate-pulse"
              style={{ opacity: 0.3 }}
            />
            <div className="text-sm font-mono text-red-500/70">
              {invariants.rho === 0 ? 'ρ = 0' : invariants.phi === 0 ? 'φ = 0' : 'τ = 0'}
            </div>
            <div className="text-xs font-mono text-neutral-600 mt-1">
              {invariants.rho === 0 ? 'No binding' : 
               invariants.phi === 0 ? 'No integration' : 
               'No temporal depth'}
            </div>
            <div className="text-xs font-mono text-neutral-700 mt-3 border-t border-neutral-800 pt-3 mx-8">
              Perspective collapsed
            </div>
          </div>
        ) : (
          // Active state with animation
          <div className="relative z-10">
            {/* Burst ring effect */}
            {burst > 0.1 && (
              <div 
                className="absolute rounded-full"
                style={{
                  width: `${size * 2}px`,
                  height: `${size * 2}px`,
                  left: `${-size * 0.5}px`,
                  top: `${-size * 0.5}px`,
                  border: `2px solid hsla(${hue}, ${saturation}%, 70%, ${burst * 0.5})`,
                  transform: `scale(${1 + burst})`,
                  opacity: burst,
                }}
              />
            )}
            
            {/* Outer glow */}
            <div 
              className="absolute rounded-full"
              style={{
                width: `${size * 1.5}px`,
                height: `${size * 1.5}px`,
                left: `${-size * 0.25}px`,
                top: `${-size * 0.25}px`,
                backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.2})`,
                filter: `blur(${20 + blur + burstGlow}px)`,
                transform: `scale(${breathe})`,
              }}
            />
            
            {/* Main sphere */}
            <div 
              className="rounded-full relative"
              style={{
                width: `${size}px`,
                height: `${size}px`,
                backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness})`,
                boxShadow: `
                  0 0 ${20 + density * 40 + burstGlow}px ${10 + density * 20}px hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.5}),
                  inset 0 0 ${size * 0.3}px hsla(${hue}, ${saturation}%, ${70}%, ${brightness * 0.3})
                `,
                filter: `blur(${blur}px)`,
                transform: `scale(${totalScale * breathe})`,
                transition: 'background-color 0.3s, box-shadow 0.3s',
              }}
            />
          </div>
        )}
        
        {/* Animation toggle */}
        <button
          onClick={toggleAnimation}
          className="absolute bottom-2 right-2 text-xs font-mono text-neutral-600 hover:text-neutral-400 transition-colors z-20"
        >
          {isAnimating ? '◉ live' : '○ paused'}
        </button>
      </div>
      
      {/* Live density readout */}
      <div className="px-3 py-2 border-t border-neutral-800 bg-neutral-950 flex items-center justify-between">
        <div className="text-xs font-mono text-neutral-600">
          D = <span className="text-neutral-400">{density.toFixed(4)}</span>
        </div>
        <div className="text-xs font-mono text-neutral-700">
          base: {baseResult.D.toFixed(4)}
        </div>
      </div>
      
      {/* Legend */}
      <div className="p-3 border-t border-neutral-800 bg-neutral-950">
        <div className="grid grid-cols-2 gap-x-4 gap-y-1 text-xs font-mono">
          <div className="flex justify-between text-neutral-600">
            <span>Size</span>
            <span className="text-neutral-500">φ</span>
          </div>
          <div className="flex justify-between text-neutral-600">
            <span>Brightness</span>
            <span className="text-neutral-500">D</span>
          </div>
          <div className="flex justify-between text-neutral-600">
            <span>Stability</span>
            <span className="text-neutral-500">ρ</span>
          </div>
          <div className="flex justify-between text-neutral-600">
            <span>Blur</span>
            <span className="text-neutral-500">H(1-κ)</span>
          </div>
        </div>
      </div>
      
      {/* Interpretation */}
      <div className="p-3 border-t border-neutral-800 bg-neutral-900/50">
        <div className="text-sm text-neutral-400">
          {hasStructuralZero ? (
            'Zero in any structural dimension produces zero perspective.'
          ) : burst > 0.5 ? (
            'Moment of heightened awareness. A thought, a sensation, a flash of presence.'
          ) : density < 0.1 ? (
            'Dim, unstable. Approaching the threshold of non-experience.'
          ) : density < 0.3 ? (
            'Faint presence. Fragmentary awareness.'
          ) : density < 0.5 ? (
            'Moderate presence. Functional awareness.'
          ) : density < 0.7 ? (
            'Clear, stable. Coherent experience.'
          ) : (
            'Vivid, intensely present. Peak awareness.'
          )}
        </div>
      </div>
    </div>
  );
}
