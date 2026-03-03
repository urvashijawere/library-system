"use client";

export default function BooksTable({ books, loading, onEdit, onDelete}: any) {
  return (
    <div className="overflow-x-auto border rounded-lg">
      <table className="min-w-full text-sm text-left">
        <thead className="bg-gray-100 text-gray-700 uppercase text-xs">
          <tr>
            <th className="px-4 py-3">ISBN</th>
            <th className="px-4 py-3">Title</th>
            <th className="px-4 py-3">Author</th>
            <th className="px-4 py-3">Genre</th>
            <th className="px-4 py-3">Update</th>
            <th className="px-4 py-3">Remove</th>
          </tr>
        </thead>

        <tbody>
          {loading ? (
            <tr>
              <td colSpan={5} className="text-center py-6">
                Loading...
              </td>
            </tr>
          ) : books.length === 0 ? (
            <tr>
              <td colSpan={5} className="text-center py-6">
                No Books Found
              </td>
            </tr>
          ) : (
            books.map((book: any) => (
              <tr
                key={book.id}
                className="border-t hover:bg-gray-50 transition"
              >
                <td className="px-4 py-3">{book.isbn}</td>
                <td className="px-4 py-3 font-medium">{book.title}</td>
                <td className="px-4 py-3">{book.author}</td>
                <td className="px-4 py-3">{book.genre}</td>
                <td className="px-4 py-3">
                  <button
                    onClick={() => onEdit(book)}
                    className="text-rose-400 hover:underline"
                  >
                    Edit
                  </button>
                </td>
                <td className="px-4 py-3">
                  <button
                    onClick={() => onDelete(book.id)}
                    className="text-rose-400 hover:underline"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}