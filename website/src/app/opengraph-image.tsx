import { ImageResponse } from 'next/og';

export const alt = 'Conduit Monism: A Mathematical Theory of Consciousness';
export const size = { width: 1200, height: 630 };
export const contentType = 'image/png';

export default function Image() {
  return new ImageResponse(
    (
      <div
        style={{
          height: '100%',
          width: '100%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: '#0a0a0a',
          fontFamily: 'monospace',
        }}
      >
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '24px',
          }}
        >
          <div style={{ fontSize: 56, color: '#e5e5e5', letterSpacing: '-1px' }}>
            Conduit Monism
          </div>
          <div style={{ fontSize: 28, color: '#737373' }}>
            D = phi * tau * rho * [(1 - sqrt(H)) + (H * kappa)]
          </div>
          <div style={{ fontSize: 18, color: '#525252', marginTop: '16px' }}>
            A mathematical theory of consciousness
          </div>
        </div>
      </div>
    ),
    { ...size },
  );
}
