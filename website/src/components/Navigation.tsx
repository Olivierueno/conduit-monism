'use client';

import { useState, useRef, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const primaryLinks = [
  { href: '/', label: 'Home' },
  { href: '/framework', label: 'Framework' },
  { href: '/implications', label: 'Implications' },
];

const technicalLinks = [
  { href: '/engine', label: 'Engine' },
  { href: '/calibration', label: 'Calibration' },
  { href: '/validation', label: 'Validation' },
  { href: '/technical', label: 'Technical' },
  { href: '/about', label: 'About' },
];

const allLinks = [...primaryLinks, ...technicalLinks];

export default function Navigation() {
  const pathname = usePathname();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const isTechnicalActive = technicalLinks.some(l => l.href === pathname);

  // Close dropdown on click outside
  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setDropdownOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  function handleMouseEnter() {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
    setDropdownOpen(true);
  }

  function handleMouseLeave() {
    timeoutRef.current = setTimeout(() => setDropdownOpen(false), 150);
  }

  return (
    <nav className="border-b border-neutral-800 bg-neutral-950/80 backdrop-blur-sm sticky top-0 z-50">
      <div className="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
        <Link href="/" className="font-mono text-sm hover:text-white transition-colors">
          CONDUIT MONISM
        </Link>

        {/* Desktop navigation */}
        <div className="hidden md:flex items-center gap-6">
          {primaryLinks.filter(l => l.href !== '/').map(link => (
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

          {/* Technical dropdown */}
          <div
            ref={dropdownRef}
            className="relative"
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
          >
            <button
              onClick={() => setDropdownOpen(prev => !prev)}
              className={`text-xs uppercase tracking-wide transition-colors flex items-center gap-1 ${
                isTechnicalActive ? 'text-white' : 'text-neutral-500 hover:text-neutral-300'
              }`}
            >
              More
              <svg width="10" height="10" viewBox="0 0 10 10" fill="none" className={`transition-transform ${dropdownOpen ? 'rotate-180' : ''}`}>
                <path d="M2 4L5 7L8 4" stroke="currentColor" strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </button>

            {dropdownOpen && (
              <div className="absolute right-0 top-full mt-2 py-1 bg-neutral-900 border border-neutral-800 min-w-[160px] z-50">
                {technicalLinks.map(link => (
                  <Link
                    key={link.href}
                    href={link.href}
                    onClick={() => setDropdownOpen(false)}
                    className={`block px-4 py-2 text-xs uppercase tracking-wide transition-colors ${
                      pathname === link.href
                        ? 'text-white bg-neutral-800'
                        : 'text-neutral-500 hover:text-neutral-300 hover:bg-neutral-800/50'
                    }`}
                  >
                    {link.label}
                  </Link>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Mobile hamburger button */}
        <button
          className="md:hidden p-2 -mr-2"
          onClick={() => setMobileOpen(!mobileOpen)}
          aria-label="Toggle menu"
        >
          <svg
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            className="text-neutral-400"
          >
            {mobileOpen ? (
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
      {mobileOpen && (
        <div className="md:hidden border-t border-neutral-800 bg-neutral-950">
          <div className="px-4 py-2">
            {primaryLinks.map(link => (
              <Link
                key={link.href}
                href={link.href}
                onClick={() => setMobileOpen(false)}
                className={`block py-3 text-sm uppercase tracking-wide transition-colors border-b border-neutral-900 ${
                  pathname === link.href
                    ? 'text-white'
                    : 'text-neutral-500'
                }`}
              >
                {link.label}
              </Link>
            ))}
            <div className="border-b border-neutral-700 my-1" />
            {technicalLinks.map((link, i) => (
              <Link
                key={link.href}
                href={link.href}
                onClick={() => setMobileOpen(false)}
                className={`block py-3 text-sm uppercase tracking-wide transition-colors ${
                  i < technicalLinks.length - 1 ? 'border-b border-neutral-900' : ''
                } ${
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
