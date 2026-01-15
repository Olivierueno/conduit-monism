import type { Metadata } from "next";
import Navigation from "@/components/Navigation";
import "./globals.css";

export const metadata: Metadata = {
  title: "Conduit Monism",
  description: "A structural theory of consciousness. Framework, computational engine, and experimental validation.",
  keywords: ["consciousness", "philosophy of mind", "AI", "binding", "perspectival density"],
  authors: [{ name: "Olivier Ueno" }],
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
