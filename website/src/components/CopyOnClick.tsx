'use client';

import { useEffect, useCallback } from 'react';

export default function CopyOnClick({ children }: { children: React.ReactNode }) {
  const handleClick = useCallback((e: MouseEvent) => {
    const target = (e.target as HTMLElement).closest('code');
    if (!target) return;

    // Skip if user has text selected
    const selection = window.getSelection();
    if (selection && selection.toString().length > 0) return;

    const text = target.textContent;
    if (!text) return;

    navigator.clipboard.writeText(text).then(() => {
      const rect = target.getBoundingClientRect();
      const tooltip = document.createElement('div');
      tooltip.textContent = 'Copied';
      tooltip.style.cssText = `
        position: fixed;
        top: ${rect.top - 32}px;
        left: ${rect.left + rect.width / 2}px;
        transform: translateX(-50%);
        background: #e5e5e5;
        color: #0a0a0a;
        padding: 2px 8px;
        font-size: 11px;
        font-family: 'SF Mono', 'Fira Code', monospace;
        z-index: 9999;
        pointer-events: none;
        transition: opacity 0.3s;
      `;
      document.body.appendChild(tooltip);
      setTimeout(() => {
        tooltip.style.opacity = '0';
      }, 1200);
      setTimeout(() => {
        tooltip.remove();
      }, 1500);
    });
  }, []);

  useEffect(() => {
    document.addEventListener('click', handleClick);
    return () => document.removeEventListener('click', handleClick);
  }, [handleClick]);

  return <>{children}</>;
}
