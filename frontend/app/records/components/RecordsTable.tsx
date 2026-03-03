"use client";

export default function RecordsTable({ records, onReturn }) {
  return (
    <div className="overflow-x-auto border rounded-lg">
      <table className="min-w-full text-sm text-left">
        <thead className="bg-gray-100 text-gray-700 uppercase text-xs">
          <tr>
            <th className="px-4 py-3">Member Id</th>
            <th className="px-4 py-3">Title</th>
            <th className="px-4 py-3">Item Code</th>
            <th className="px-4 py-3">Issued At</th>
            <th className="px-4 py-3">Due Date</th>
            <th className="px-4 py-3">Status</th>
            <th className="px-4 py-3">Fine</th>
            <th className="px-4 py-3 text-right">Action</th>
          </tr>
        </thead>

        <tbody className="divide-y divide-gray-100">
          {records.length === 0 ? (
            <tr>
              <td
                colSpan={8}
                className="px-6 py-6 text-center text-gray-500"
              >
                No records found.
              </td>
            </tr>
          ) : (
            records.map((record) => (
              <tr
                key={record.id}
                className="border-t hover:bg-gray-50 transition"
              >
                <td className="px-4 py-3">
                  {record.member.membership_id}
                </td>

                <td className="px-4 py-3">
                  {record.book_copy.book.title}
                </td>

                <td className="px-4 py-3 text-gray-600">
                  {record.book_copy.barcode}
                </td>

                <td className="px-4 py-3 text-gray-600">
                  {new Date(record.issued_at).toLocaleDateString()}
                </td>

                <td className="px-4 py-3 text-gray-600">
                  {new Date(record.due_date).toLocaleDateString()}
                </td>

                <td className="px-4 py-3">
                  {record.status}
                </td>

                <td className="px-4 py-3 font-medium">
                  ₹{record.fine_amount}
                </td>

                <td className="px-4 py-3 text-right">
                  {record.status === "ACTIVE" && (
                    <button
                      onClick={() => onReturn(record)}
                      className="text-green-600 hover:underline font-medium"
                    >
                      Return
                    </button>
                  )}
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}