'use client';

import { useMemo, useState, useEffect } from 'react';
import { Invariants, calculateDensity } from '@/lib/engine';

interface StateVisualizationProps {
  invariants: Invariants;
  isAnimating?: boolean;
}

export default function StateVisualization({ invariants, isAnimating = true }: StateVisualizationProps) {
  const [time, setTime] = useState(0);
  
  // Animation loop for breathing effect only
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
  
  const result = useMemo(() => calculateDensity(invariants), [invariants]);
  const { phi, tau, rho, H, kappa } = invariants;
  
  // Calculate visual properties
  const hasStructuralZero = phi === 0 || tau === 0 || rho === 0;
  const density = result.D;
  
  // Brightness based on density
  const brightness = Math.max(0.1, density);
  
  // Size based on integration (phi)
  const size = 60 + (phi * 80);
  
  // Blur based on entropy without coherence
  const effectiveNoise = H * (1 - kappa);
  const blur = effectiveNoise * 20;
  
  // Color
  const hue = H > 0.5 && kappa > 0.5 ? 280 : 200;
  const saturation = H > 0.5 ? (kappa * 100) : 20;
  
  // Subtle breathing - very slow, barely perceptible
  const breathe = isAnimating ? 1 + Math.sin(time * 0.4) * 0.015 : 1;
  
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
              {rho === 0 ? 'ρ = 0' : phi === 0 ? 'φ = 0' : 'τ = 0'}
            </div>
            <div className="text-xs font-mono text-neutral-600 mt-1">
              {rho === 0 ? 'No binding' : 
               phi === 0 ? 'No integration' : 
               'No temporal depth'}
            </div>
            <div className="text-xs font-mono text-neutral-700 mt-3 border-t border-neutral-800 pt-3 mx-8">
              Perspective collapsed
            </div>
          </div>
        ) : (
          // Active state - subtle, living movement
          <div className="relative z-10">
            {/* Outer glow */}
            <div 
              className="absolute rounded-full"
              style={{
                width: `${size * 1.5}px`,
                height: `${size * 1.5}px`,
                left: `${-size * 0.25}px`,
                top: `${-size * 0.25}px`,
                backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.2})`,
                filter: `blur(${20 + blur}px)`,
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
                  0 0 ${20 + density * 40}px ${10 + density * 20}px hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.5}),
                  inset 0 0 ${size * 0.3}px hsla(${hue}, ${saturation}%, ${70}%, ${brightness * 0.3})
                `,
                filter: `blur(${blur}px)`,
                transform: `scale(${breathe})`,
              }}
            />
          </div>
        )}
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
            <span>Glow</span>
            <span className="text-neutral-500">ρ</span>
          </div>
          <div className="flex justify-between text-neutral-600">
            <span>Blur</span>
            <span className="text-neutral-500">H(1-κ)</span>
          </div>
        </div>
      </div>
    </div>
  );
}
