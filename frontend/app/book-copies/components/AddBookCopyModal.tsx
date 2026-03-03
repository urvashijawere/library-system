"use client";

import { useState } from "react";
import { apiRequest } from "@/lib/api";

export default function AddBookCopiesModal({ onClose, onSuccess }) {
  const [isbn, setIsbn] = useState("");
  const [copies, setCopies] = useState([{ barcode: "" }]);
  const [loading, setLoading] = useState(false);

  const handleCopyChange = (index: number, value: string) => {
    const updated = [...copies];
    updated[index].barcode = value;
    setCopies(updated);
  };

  const addCopyField = () => {
    setCopies([...copies, { barcode: "" }]);
  };

  const removeCopyField = (index: number) => {
    const updated = copies.filter((_, i) => i !== index);
    setCopies(updated);
  };

  const handleSubmit = async () => {
    if (!isbn) {
      alert("ISBN is required");
      return;
    }

    const validCopies = copies.filter((c) => c.barcode !== "");

    if (validCopies.length === 0) {
      alert("At least one barcode is required");
      return;
    }

    setLoading(true);

    try {
      await apiRequest("/books/copies/", "POST", {
        isbn,
        copies: validCopies,
      });

      onSuccess();
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex justify-center items-center z-50">
      <div className="bg-white rounded-xl shadow-sm w-full max-w-lg p-6">
        <h2 className="text-xl font-semibold mb-6">
          Add Book Copies
        </h2>

        <div className="space-y-4">
          {/* ISBN */}
          <div>
            <label className="block text-sm font-medium mb-1">
              ISBN
            </label>
            <input
              type="text"
              value={isbn}
              onChange={(e) => setIsbn(e.target.value)}
              placeholder="Enter Book ISBN"
              className="w-full border p-2 rounded-md"
            />
          </div>

          {/* Copies */}
          <div>
            <h3 className="font-medium text-gray-700 mb-2">
              Barcodes
            </h3>

            {copies.map((copy, index) => (
              <div key={index} className="flex gap-2 mb-2">
                <input
                  type="text"
                  placeholder="Barcode"
                  value={copy.barcode}
                  onChange={(e) =>
                    handleCopyChange(index, e.target.value)
                  }
                  className="flex-1 border p-2 rounded-md"
                />

                {copies.length > 1 && (
                  <button
                    onClick={() => removeCopyField(index)}
                    className="text-red-600 px-2"
                  >
                    ✕
                  </button>
                )}
              </div>
            ))}

            <button
              onClick={addCopyField}
              className="text-rose-300 text-sm mt-2"
            >
              + Add Another Copy
            </button>
          </div>
        </div>

        <div className="flex justify-end gap-3 mt-6">
          <button
            onClick={onClose}
            className="px-4 py-2 border rounded-md text-gray-600"
          >
            Cancel
          </button>

          <button
            onClick={handleSubmit}
            disabled={loading}
            className="button-primary"
          >
            {loading ? "Saving..." : "Save"}
          </button>
        </div>
      </div>
    </div>
  );
}