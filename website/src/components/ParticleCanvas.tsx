'use client';

import { useEffect, useRef } from 'react';

// D = phi * tau * rho * [(1 - sqrt(H)) + (H * kappa)]
function computeD(phi: number, tau: number, rho: number, H: number, kappa: number): number {
  return phi * tau * rho * ((1 - Math.sqrt(H)) + (H * kappa));
}

interface Soul {
  x: number;
  y: number;
  vx: number;
  vy: number;
  phi: number;
  tau: number;
  rho: number;
  H: number;
  kappa: number;
  D: number;
  age: number;
  lifespan: number;
  birthLen: number;
  r: number;
  baseOpacity: number;
  turnTimer: number;
}

const SOUL_COUNT = 20;
const FADE_OUT = 60;

function createSoul(w: number, h: number): Soul {
  const phi = Math.random();
  const tau = Math.random();
  const rho = Math.random();
  const H = Math.random();
  const kappa = Math.random();
  const D = computeD(phi, tau, rho, H, kappa);

  const speed = 0.15 + H * 0.4;
  const angle = Math.random() * Math.PI * 2;

  return {
    x: Math.random() * w,
    y: Math.random() * h,
    vx: Math.cos(angle) * speed,
    vy: Math.sin(angle) * speed,
    phi, tau, rho, H, kappa, D,
    age: 0,
    lifespan: 300 + Math.random() * 300,
    birthLen: kappa > 0.5 ? 60 : 15,
    r: 2 + D * 14,
    baseOpacity: 0.03 + D * 0.15,
    turnTimer: 0,
  };
}

export default function ParticleCanvas() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationId: number;
    const dpr = window.devicePixelRatio || 1;
    let souls: Soul[] = [];
    let w = 0;
    let h = 0;

    function resize() {
      if (!canvas) return;
      const rect = canvas.getBoundingClientRect();
      w = rect.width;
      h = rect.height;
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      ctx!.scale(dpr, dpr);
    }

    function init() {
      souls = Array.from({ length: SOUL_COUNT }, () => createSoul(w, h));
      // Stagger ages so they don't all die at once
      for (const s of souls) {
        s.age = Math.random() * s.lifespan * 0.8;
      }
    }

    function draw() {
      if (!canvas || !ctx) return;
      ctx.clearRect(0, 0, w, h);

      for (let i = 0; i < souls.length; i++) {
        const s = souls[i];
        s.age++;

        // Respawn
        if (s.age >= s.lifespan) {
          souls[i] = createSoul(w, h);
          continue;
        }

        // Jitter: high entropy + low coherence = erratic
        const jitter = s.H * (1 - s.kappa) * 1.5;
        if (jitter > 0.01) {
          s.vx += (Math.random() - 0.5) * jitter;
          s.vy += (Math.random() - 0.5) * jitter;
        }

        // Direction changes: low tau = frequent turns
        s.turnTimer++;
        if (s.turnTimer > 30 + s.tau * 200) {
          const a = Math.random() * Math.PI * 2;
          const spd = 0.15 + s.H * 0.4;
          s.vx = Math.cos(a) * spd;
          s.vy = Math.sin(a) * spd;
          s.turnTimer = 0;
        }

        // Clamp speed
        const spd = Math.sqrt(s.vx * s.vx + s.vy * s.vy);
        if (spd > 0.8) {
          s.vx = (s.vx / spd) * 0.8;
          s.vy = (s.vy / spd) * 0.8;
        }

        s.x += s.vx;
        s.y += s.vy;

        // Wrap
        if (s.x < -s.r) s.x = w + s.r;
        if (s.x > w + s.r) s.x = -s.r;
        if (s.y < -s.r) s.y = h + s.r;
        if (s.y > h + s.r) s.y = -s.r;

        // Lifecycle opacity
        let opacity = s.baseOpacity;
        const deathStart = s.lifespan - FADE_OUT;

        if (s.age < s.birthLen) {
          const t = s.age / s.birthLen;
          if (s.kappa > 0.5) {
            // Smooth fade in
            opacity *= t;
          } else {
            // Violent flash: 3x at birth, decay to base
            opacity *= 1 + 2 * (1 - t);
          }
        } else if (s.age > deathStart) {
          opacity *= 1 - (s.age - deathStart) / FADE_OUT;
        }

        // Radius pulse on violent birth
        let r = s.r;
        if (s.age < s.birthLen && s.kappa <= 0.5) {
          r *= 1 + 0.5 * (1 - s.age / s.birthLen);
        }

        // Color: warm white for high D, cool blue-grey for low D
        const rc = Math.round(180 + s.D * 60);
        const gc = Math.round(190 + s.D * 40);
        const bc = Math.round(210 - s.D * 20);

        const grad = ctx.createRadialGradient(s.x, s.y, 0, s.x, s.y, r);
        grad.addColorStop(0, `rgba(${rc},${gc},${bc},${opacity.toFixed(3)})`);
        grad.addColorStop(1, `rgba(${rc},${gc},${bc},0)`);
        ctx.beginPath();
        ctx.arc(s.x, s.y, r, 0, Math.PI * 2);
        ctx.fillStyle = grad;
        ctx.fill();
      }

      animationId = requestAnimationFrame(draw);
    }

    resize();
    init();
    draw();

    const handleResize = () => { resize(); init(); };
    window.addEventListener('resize', handleResize);

    return () => {
      cancelAnimationFrame(animationId);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="absolute inset-0 w-full h-full pointer-events-none"
      aria-hidden="true"
    />
  );
}
