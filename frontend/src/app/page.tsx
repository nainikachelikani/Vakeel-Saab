import { Button } from '@/components/common/buttons/Button';
import { Card } from '@/components/common/cards/Card';
import { Sparkles, ShieldCheck, Scale, Users } from 'lucide-react';
import Link from 'next/link';
import { APP_ROUTES } from '@/constants/ui';

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-[#F8FAFC] flex flex-col">
      {/* Navbar */}
      <header className="max-w-7xl mx-auto w-full px-6 h-20 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-[#1E293B] flex items-center justify-center text-white font-extrabold text-lg">VS</div>
          <div className="flex flex-col text-left">
            <span className="font-bold font-serif text-[#1E293B] text-lg leading-tight">Vakeel Saab</span>
            <span className="text-[10px] text-gray-500 font-bold uppercase tracking-widest mt-0.5">AI Legal Intelligence</span>
          </div>
        </div>
        <div className="flex items-center gap-4">
          <Link href={APP_ROUTES.LOGIN}>
            <Button variant="ghost" size="sm">Sign In</Button>
          </Link>
          <Link href={APP_ROUTES.SIGNUP}>
            <Button size="sm">Get Started</Button>
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="flex-1 flex flex-col items-center justify-center text-center max-w-4xl mx-auto px-6 py-20">
        <div className="inline-flex items-center gap-2 px-3 py-1 bg-emerald-50 text-[#059669] rounded-full text-xs font-bold uppercase tracking-wider mb-6 border border-emerald-100">
          <ShieldCheck className="w-3.5 h-3.5" />
          Systems Fully Operational
        </div>

        <h1 className="text-5xl font-black font-serif text-[#1E293B] tracking-tight leading-tight sm:text-6xl">
          AI Powered Multi-Agent <br />
          <span className="text-[#D97706]">
            Legal Intelligence Platform
          </span>
        </h1>

        <p className="text-gray-500 text-base mt-6 max-w-2xl leading-relaxed">
          One unified AI operating system that democratizes justice and scales legal operations. Intelligently adapts to your needs, whether you are seeking help or analyzing complex contracts.
        </p>

        <div className="mt-10">
          <Link href={APP_ROUTES.SIGNUP}>
            <Button size="lg" className="px-8 text-base shadow-sm">Enter Vakeel Saab Workspace</Button>
          </Link>
        </div>

        {/* Value Prop Cards */}
        <div className="grid sm:grid-cols-2 gap-6 w-full mt-20 max-w-3xl">
          <Card className="text-left p-6 border border-gray-100 rounded-2xl bg-white shadow-sm">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-lg bg-gray-50 text-gray-700 flex items-center justify-center">
                <Users className="w-5 h-5" />
              </div>
              <h3 className="font-bold text-gray-900">For Citizens</h3>
            </div>
            <p className="text-xs text-gray-500 leading-relaxed">
              Navigate the legal system with ease. Generate complaints, understand your rights regarding labor or leases, and find local legal aid.
            </p>
          </Card>

          <Card className="text-left p-6 border border-gray-100 rounded-2xl bg-white shadow-sm">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-lg bg-[#1E293B]/5 text-[#1E293B] flex items-center justify-center">
                <Scale className="w-5 h-5" />
              </div>
              <h3 className="font-bold text-gray-900">For Legal Professionals</h3>
            </div>
            <p className="text-xs text-gray-500 leading-relaxed">
              Scale your practice with precision. Upload contracts to our dedicated workspace for automated risk analysis, clause extraction, and semantic search.
            </p>
          </Card>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-100 bg-white py-8 text-center text-xs text-gray-500">
        <div className="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row justify-between items-center gap-4">
          <span>&copy; {new Date().getFullYear()} Vakeel Saab. All rights reserved. Secure Enterprise Encryption.</span>
          <div className="flex gap-4">
            <Link href="#" className="hover:text-gray-900">Privacy Policy</Link>
            <Link href="#" className="hover:text-gray-900">Terms of Service</Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
