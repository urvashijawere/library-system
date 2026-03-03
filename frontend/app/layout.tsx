import "./globals.css";
import Header from "../components/Header";
import Sidebar from "../components/Sidebar";

export const metadata = {
  title: "Library Dashboard",
  description: "Library Management System",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Header />
        <div className="flex">
          <Sidebar />
          <main className="flex-1 p-10">{children}</main>
        </div>
      </body>
    </html>
  );
}