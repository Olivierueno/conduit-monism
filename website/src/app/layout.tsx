import type { Metadata } from "next";
import Navigation from "@/components/Navigation";
import "./globals.css";

const siteUrl = "https://www.conduitmonism.org";

export const metadata: Metadata = {
  title: {
    default: "Conduit Monism",
    template: "%s | Conduit Monism",
  },
  description: "A structural theory of consciousness. Perspectival density as a function of integration, temporal depth, and re-entrant binding.",
  keywords: [
    "consciousness",
    "philosophy of mind",
    "perspectival density",
    "integrated information theory",
    "binding problem",
    "hard problem of consciousness",
    "AI consciousness",
    "RWKV",
    "phenomenology",
  ],
  authors: [{ name: "Olivier Ueno" }],
  creator: "Olivier Ueno",
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
    description: "A structural theory of consciousness. Perspectival density as a function of integration, temporal depth, and re-entrant binding.",
  },
  twitter: {
    card: "summary_large_image",
    title: "Conduit Monism",
    description: "A structural theory of consciousness. Perspectival density as a function of integration, temporal depth, and re-entrant binding.",
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

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased min-h-screen">
        <Navigation />
        {children}
      </body>
    </html>
  );
}
