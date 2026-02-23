import type { Metadata } from "next";
import Navigation from "@/components/Navigation";
import CopyOnClick from "@/components/CopyOnClick";
import { Analytics } from "@vercel/analytics/next";
import "./globals.css";

const siteUrl = "https://www.conduitmonism.org";
const description =
  "When does a physical system become conscious? A mathematical framework proposing five structural conditions for experience, tested against neuroscience data and AI systems.";

export const metadata: Metadata = {
  title: {
    default: "Conduit Monism",
    template: "%s | Conduit Monism",
  },
  description,
  keywords: [
    "consciousness",
    "theory of consciousness",
    "philosophy of mind",
    "perspectival density",
    "consciousness formula",
    "consciousness calculator",
    "integrated information theory",
    "binding problem",
    "hard problem of consciousness",
    "AI consciousness",
    "animal consciousness",
    "psychedelic consciousness",
    "neural correlates of consciousness",
    "RWKV",
    "phenomenology",
  ],
  authors: [{ name: "O.U." }],
  creator: "O.U.",
  metadataBase: new URL(siteUrl),
  alternates: {
    canonical: "/",
  },
  openGraph: {
    type: "website",
    locale: "en_US",
    url: siteUrl,
    siteName: "Conduit Monism",
    title: "Conduit Monism",
    description,
  },
  twitter: {
    card: "summary_large_image",
    title: "Conduit Monism",
    description,
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
};

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  name: "Conduit Monism",
  url: siteUrl,
  description,
  author: {
    "@type": "Person",
    name: "O.U.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased min-h-screen">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
        <Navigation />
        <CopyOnClick>{children}</CopyOnClick>
        <Analytics />
      </body>
    </html>
  );
}
