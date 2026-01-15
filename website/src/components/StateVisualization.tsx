'use client';

import { useMemo } from 'react';
import { Invariants, calculateDensity } from '@/lib/engine';

interface StateVisualizationProps {
  invariants: Invariants;
}

export default function StateVisualization({ invariants }: StateVisualizationProps) {
  const result = useMemo(() => calculateDensity(invariants), [invariants]);
  const { phi, tau, rho, H, kappa } = invariants;
  
  // Calculate visual properties
  const hasStructuralZero = phi === 0 || tau === 0 || rho === 0;
  const density = result.D;
  
  // Brightness based on density
  const brightness = Math.max(0.1, density);
  
  // Stability based on binding (rho)
  // Low rho = flickering, unstable
  const flickerIntensity = rho < 0.2 ? (0.2 - rho) * 5 : 0;
  
  // Size based on integration (phi) - larger for center display
  const size = 60 + (phi * 80);
  
  // Blur based on entropy without coherence
  const effectiveNoise = H * (1 - kappa);
  const blur = effectiveNoise * 20;
  
  // Color based on coherence within entropy
  // High H + High kappa = vibrant (psychedelic)
  // High H + Low kappa = grey (seizure)
  // Low H = white/blue (clarity)
  const hue = H > 0.5 && kappa > 0.5 ? 280 : 200; // Purple for structured chaos, blue for clarity
  const saturation = H > 0.5 ? (kappa * 100) : 20;
  
  // Animation for flicker effect
  const flickerAnimation = flickerIntensity > 0 
    ? `flicker ${0.1 + (1 - flickerIntensity) * 0.4}s infinite`
    : 'none';
  
  // Pulse animation based on temporal depth
  const pulseScale = tau > 0.5 ? 1 + (tau - 0.5) * 0.1 : 1;
  
  return (
    <div className="relative border border-neutral-800">
      {/* State visualization - taller for prominence */}
      <div className="h-64 bg-black flex items-center justify-center overflow-hidden relative">
        {/* Background grid for depth perception */}
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
              {rho === 0 ? 'No binding — no self-reference' : 
               phi === 0 ? 'No integration — fragmented' : 
               'No temporal depth — no continuity'}
            </div>
            <div className="text-xs font-mono text-neutral-700 mt-3 border-t border-neutral-800 pt-3 mx-8">
              Perspective collapsed
            </div>
          </div>
        ) : (
          // Active state with multiple layers for depth
          <div className="relative z-10">
            {/* Outer glow */}
            <div 
              className="absolute rounded-full transition-all duration-500"
              style={{
                width: `${size * 1.5}px`,
                height: `${size * 1.5}px`,
                left: `${-size * 0.25}px`,
                top: `${-size * 0.25}px`,
                backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.2})`,
                filter: `blur(${20 + blur}px)`,
              }}
            />
            {/* Main sphere */}
            <div 
              className="rounded-full transition-all duration-300 relative"
              style={{
                width: `${size}px`,
                height: `${size}px`,
                backgroundColor: `hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness})`,
                boxShadow: `
                  0 0 ${20 + density * 40}px ${10 + density * 20}px hsla(${hue}, ${saturation}%, ${50 + brightness * 30}%, ${brightness * 0.5}),
                  inset 0 0 ${size * 0.3}px hsla(${hue}, ${saturation}%, ${70}%, ${brightness * 0.3})
                `,
                filter: `blur(${blur}px)`,
                animation: flickerAnimation,
                transform: `scale(${pulseScale})`,
              }}
            />
          </div>
        )}
      </div>
      
      {/* Legend - compact grid */}
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
      
      {/* CSS for flicker animation */}
      <style jsx>{`
        @keyframes flicker {
          0%, 100% { opacity: 1; }
          50% { opacity: ${1 - flickerIntensity}; }
        }
      `}</style>
    </div>
  );
}
