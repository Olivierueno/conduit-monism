'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const links = [
  { href: '/', label: 'Home' },
  { href: '/framework', label: 'Framework' },
  { href: '/engine', label: 'Engine' },
  { href: '/calibration', label: 'Calibration' },
  { href: '/validation', label: 'Validation' },
  { href: '/technical', label: 'Technical' },
  { href: '/about', label: 'About' },
];

export default function Navigation() {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);
  
  return (
    <nav className="border-b border-neutral-800 bg-neutral-950/80 backdrop-blur-sm sticky top-0 z-50">
      <div className="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
        <Link href="/" className="font-mono text-sm hover:text-white transition-colors">
          CONDUIT MONISM
        </Link>
        
        {/* Desktop navigation */}
        <div className="hidden md:flex gap-6">
          {links.map(link => (
            <Link
              key={link.href}
              href={link.href}
              className={`text-xs uppercase tracking-wide transition-colors ${
                pathname === link.href 
                  ? 'text-white' 
                  : 'text-neutral-500 hover:text-neutral-300'
              }`}
            >
              {link.label}
            </Link>
          ))}
        </div>
        
        {/* Mobile hamburger button */}
        <button 
          className="md:hidden p-2 -mr-2"
          onClick={() => setIsOpen(!isOpen)}
          aria-label="Toggle menu"
        >
          <svg 
            width="20" 
            height="20" 
            viewBox="0 0 20 20" 
            fill="none" 
            className="text-neutral-400"
          >
            {isOpen ? (
              <path 
                d="M5 5L15 15M5 15L15 5" 
                stroke="currentColor" 
                strokeWidth="1.5" 
                strokeLinecap="round"
              />
            ) : (
              <>
                <path d="M3 5H17" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
                <path d="M3 10H17" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
                <path d="M3 15H17" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
              </>
            )}
          </svg>
        </button>
      </div>
      
      {/* Mobile menu */}
      {isOpen && (
        <div className="md:hidden border-t border-neutral-800 bg-neutral-950">
          <div className="px-4 py-2">
            {links.map(link => (
              <Link
                key={link.href}
                href={link.href}
                onClick={() => setIsOpen(false)}
                className={`block py-3 text-sm uppercase tracking-wide transition-colors border-b border-neutral-900 last:border-0 ${
                  pathname === link.href 
                    ? 'text-white' 
                    : 'text-neutral-500'
                }`}
              >
                {link.label}
              </Link>
            ))}
          </div>
        </div>
      )}
    </nav>
  );
}
