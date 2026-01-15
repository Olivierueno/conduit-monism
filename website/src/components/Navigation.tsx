'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const links = [
  { href: '/', label: 'Home' },
  { href: '/framework', label: 'Framework' },
  { href: '/engine', label: 'Engine' },
  { href: '/validation', label: 'Validation' },
  { href: '/technical', label: 'Technical' },
  { href: '/about', label: 'About' },
];

export default function Navigation() {
  const pathname = usePathname();
  
  return (
    <nav className="border-b border-neutral-800 bg-neutral-950/80 backdrop-blur-sm sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
        <Link href="/" className="font-mono text-sm hover:text-white transition-colors">
          CONDUIT MONISM
        </Link>
        <div className="flex gap-6">
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
      </div>
    </nav>
  );
}
