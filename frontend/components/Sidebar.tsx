import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 p-6 border-r border-[#f5d7c8] bg-white/70 backdrop-blur-md">
      <nav className="space-y-4 text-gray-700">

        <Link
          href="/"
          className="block hover:text-[#ffbfae] transition-colors duration-200"
        >
          Dashboard
        </Link>

        <Link
          href="/books"
          className="block hover:text-[#ffbfae] transition-colors duration-200"
        >
          Books
        </Link>

        <Link
          href="/book-copies"
          className="block hover:text-[#ffbfae] transition-colors duration-200"
        >
          Inventory
        </Link>

        <Link
          href="/members"
          className="block hover:text-[#ffbfae] transition-colors duration-200"
        >
          Members
        </Link>

        <Link
          href="/records"
          className="block hover:text-[#ffbfae] transition-colors duration-200"
        >
          Transactions
        </Link>

      </nav>
    </aside>
  );
}