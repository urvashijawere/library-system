"use client";

export default function BooksCopyTable({
  copies,
  loading,
  onDelete,
}: {
  copies: any[];
  loading: boolean;
  onDelete: (id: number) => void;
}) {
  if (loading) {
    return (
      <div className="bg-white p-6 rounded-xl shadow-sm">
        <p className="text-gray-500">Loading book copies...</p>
      </div>
    );
  }

  return (
    <div className="overflow-x-auto border rounded-lg">
      <table className="min-w-full text-sm text-left">
        <thead className="bg-gray-100 text-gray-700 uppercase text-xs">
          <tr>
            <th className="px-4 py-3">ID</th>
            <th className="px-4 py-3">Barcode</th>
            <th className="px-4 py-3">Book ID</th>
            <th className="px-4 py-3">Status</th>
            <th className="px-4 py-3">Created</th>
            <th className="px-4 py-3 text-right">Action</th>
          </tr>
        </thead>

        <tbody>
          {copies.length === 0 ? (
            <tr>
              <td colSpan={6} className="px-6 py-6 text-center text-gray-500">
                No copies found.
              </td>
            </tr>
          ) : (
            copies.map((copy) => (
              <tr key={copy.id} className="border-t hover:bg-gray-50 transition">
                <td className="px-4 py-3 font-medium">{copy.id}</td>

                <td className="px-4 py-3">{copy.barcode}</td>

                <td className="px-4 py-3 text-gray-600">
                  {copy.book}
                </td>

                <td className="px-4 py-3">
                  {copy.status}
                </td>

                <td className="px-4 py-3 text-gray-600">
                  {new Date(copy.created_at).toLocaleDateString()}
                </td>

                <td className="px-4 py-3 text-right">
                  <button
                    onClick={() => onDelete(copy.id)}
                    className="text-red-600 hover:underline"
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
