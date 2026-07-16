import { Sidebar } from '@/components/layout/sidebar/Sidebar';
import { Navbar } from '@/components/layout/navbar/Navbar';

export default function DashboardRootLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen bg-[#F8FAFC] overflow-hidden">
      <Sidebar />
      <div className="flex flex-col flex-1 overflow-hidden">
        <Navbar />
        {children}
      </div>
    </div>
  );
}
