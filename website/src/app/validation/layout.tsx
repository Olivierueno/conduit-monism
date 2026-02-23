import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Validation',
  description: 'All 23 experiments testing Conduit Monism, including AI consciousness probes, psychedelic state predictions, and three falsified predictions.',
  alternates: { canonical: '/validation' },
};

export default function ValidationLayout({ children }: { children: React.ReactNode }) {
  return children;
}
