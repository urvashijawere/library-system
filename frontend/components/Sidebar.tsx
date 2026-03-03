export default function Sidebar() {
  return (
    <aside className="w-64 p-6 border-r border-[#f5d7c8] bg-white/70 backdrop-blur-md">
      <nav className="space-y-4 text-gray-700">
        <div className="hover:text-[#ffbfae] cursor-pointer">Dashboard</div>
        <div className="hover:text-[#ffbfae] cursor-pointer">Books</div>
        <div className="hover:text-[#ffbfae] cursor-pointer">Members</div>
        <div className="hover:text-[#ffbfae] cursor-pointer">Transactions</div>
      </nav>
    </aside>
  );
}