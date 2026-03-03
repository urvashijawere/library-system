"use client";

import { useState } from "react";
import { issueBook } from "../services/issueApi";

export default function IssueBookModal({ onClose, onSuccess }) {
  const [formData, setFormData] = useState({
    barcode: "",
    membership_id: "",
    due_date: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await issueBook(formData);
    onSuccess();
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black/30 flex justify-center items-center">
      <div className="bg-white p-6 rounded-xl w-96 shadow-lg">
        <h2 className="text-lg font-semibold mb-4">Issue Book</h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            placeholder="Book Barcode"
            className="w-full border p-2 rounded"
            onChange={(e) =>
              setFormData({ ...formData, barcode: e.target.value })
            }
          />

          <input
            placeholder="Membership ID"
            className="w-full border p-2 rounded"
            onChange={(e) =>
              setFormData({ ...formData, membership_id: e.target.value })
            }
          />

          <input
            type="datetime-local"
            className="w-full border p-2 rounded"
            onChange={(e) =>
              setFormData({ ...formData, due_date: e.target.value })
            }
          />

          <div className="flex justify-end gap-3">
            <button type="button" className="px-4 py-2 border rounded" onClick={onClose}>
              Cancel
            </button>
            <button className="button-primary">
              Issue
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}