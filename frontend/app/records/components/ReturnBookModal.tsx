"use client";

import { returnBook } from "../services/issueApi";

export default function ReturnBookModal({ record, onClose, onSuccess }) {
  const handleReturn = async () => {
    await returnBook({
      book_copy_id: record.book_copy.id,
      member_id: record.member.id,
    });

    onSuccess();
    onClose();
  };

  return (
      <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex justify-center items-center z-50">
          <div className="bg-white rounded-xl shadow-sm w-full max-w-md p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-2">
              Return Book
            </h2>

            <p className="text-gray-600 mb-6">
              Are you sure you want to return{" "}
              <span className="font-medium text-gray-900">
                {record.book_copy.book.title}
              </span>
              ?
            </p>

            <div className="flex justify-end gap-3">
              <button
                onClick={onClose}
                className="px-4 py-2 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-100 transition"
              >
                Cancel
              </button>

              <button
                onClick={handleReturn}
                className="px-4 py-2 rounded-md bg-green-600 text-white hover:bg-green-700 transition font-medium"
              >
                Confirm Return
              </button>
            </div>

          </div>
      </div>
  );
}