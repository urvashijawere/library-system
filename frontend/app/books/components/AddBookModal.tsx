"use client";

import { useState, useEffect } from "react";
import { apiRequest } from "@/lib/api";

export default function AddBookModal({ book, onClose, onSuccess }: any) {
  const [formData, setFormData] = useState({
    isbn: "",
    title: "",
    author: "",
    genre: "",
  });

  useEffect(() => {
    if (book) {
      setFormData(book);
    }
  }, [book]);

  const handleChange = (e: any) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    try {
      if (book) {
        await apiRequest(`/books/${book.id}/`, "PUT", formData);
      } else {
        await apiRequest(`/books/`, "POST", formData);
      }

      onSuccess();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/40 flex items-center justify-center">
      <div className="bg-white p-6 rounded-xl w-96 space-y-4">
        <h2 className="text-xl font-semibold">
          {book ? "Update Book" : "Add Book"}
        </h2>

        <form onSubmit={handleSubmit} className="space-y-3">
          <input
            name="isbn"
            placeholder="ISBN"
            value={formData.isbn}
            onChange={handleChange}
            className="border p-2 w-full"
          />
          <input
            name="title"
            placeholder="Title"
            value={formData.title}
            onChange={handleChange}
            className="border p-2 w-full"
          />
          <input
            name="author"
            placeholder="Author"
            value={formData.author}
            onChange={handleChange}
            className="border p-2 w-full"
          />
          <input
            name="genre"
            placeholder="Genre"
            value={formData.genre}
            onChange={handleChange}
            className="border p-2 w-full"
          />

          <div className="flex justify-end gap-3">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 border rounded"
            >
              Cancel
            </button>

            <button type="submit" className="button-primary">
              {book ? "Update" : "Create"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}