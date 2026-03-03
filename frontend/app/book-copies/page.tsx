"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";
import BooksCopyTable from "./components/BooksCopyTable";
import AddBookCopyModal from "./components/AddBookCopyModal";

export default function BookCopiesPage() {
  const [copies, setCopies] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetchCopies();
  }, [search]);

  const fetchCopies = async () => {
    setLoading(true);
    try {
      const query = search ? `?search=${search}` : "";
      const data = await apiRequest(`/books/book-copies/${query}`);
      setCopies(data.results || data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSuccess = () => {
    setShowModal(false);
    fetchCopies();
  };

  const handleDelete = async (bookCopyId: number) => {
      const confirmed = window.confirm("Are you sure you want to delete this book?");
      if (!confirmed) return;

      try {
        await apiRequest(`/books/book-copies/${bookCopyId}/`, "DELETE");
        fetchCopies();
      } catch (err) {
        console.error(err);
      }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-semibold">Book Copies</h1>

      {/* Top Bar */}
      <div className="flex gap-4 items-center">
        <input
          type="text"
          placeholder="Search by barcode, status..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="border p-2 rounded w-1/2"
        />

        <button
          onClick={() => setShowModal(true)}
          className="button-primary"
        >
          Add Book Copies
        </button>
      </div>

      <BooksCopyTable copies={copies} loading={loading} onDelete={handleDelete}/>

      {showModal && (
        <AddBookCopyModal
          onClose={() => setShowModal(false)}
          onSuccess={handleSuccess}
        />
      )}
    </div>
  );
}