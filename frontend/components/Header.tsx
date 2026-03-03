export default function Header() {
  return (
    <header className="px-10 py-5 border-b border-[#f5d7c8] bg-[#fff1e6]/70 backdrop-blur-md">
      <div className="flex items-center gap-3">
        <img src="/file.svg" alt="Library Logo" className="h-8 w-8" />
        <h1 className="text-2xl font-bold">Library Management</h1>
      </div>
    </header>
  );
}