"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";
import BooksTable from "./components/BooksTable";
import AddBookModal from "./components/AddBookModal";

export default function BooksPage() {
  const [books, setBooks] = useState<any[]>([]);
  const [search, setSearch] = useState("");
  const [genre, setGenre] = useState("");
  const [loading, setLoading] = useState(true);

  const [showModal, setShowModal] = useState(false);
  const [editingBook, setEditingBook] = useState<any | null>(null);

  useEffect(() => {
    fetchBooks();
  }, [search, genre]);

  const fetchBooks = async () => {
    setLoading(true);

    let query = `/books/?`;
    if (search) query += `search=${search}&`;
    if (genre) query += `genre=${genre}&`;

    try {
      const data = await apiRequest(query);
      setBooks(data.results || data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const openAddModal = () => {
    setEditingBook(null);
    setShowModal(true);
  };

  const openEditModal = (book: any) => {
    setEditingBook(book);
    setShowModal(true);
  };

  const handleDelete = async (bookId: number) => {
      const confirmed = window.confirm("Are you sure you want to delete this book?");
      if (!confirmed) return;

      try {
        await apiRequest(`/books/${bookId}/`, "DELETE");
        fetchBooks();
      } catch (err) {
        console.error(err);
      }
  };

  const handleSuccess = () => {
    setShowModal(false);
    fetchBooks();
  };

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-semibold">Books</h1>

      {/* Search + Filter + Add */}
      <div className="flex gap-4 items-center">
        <input
          type="text"
          placeholder="Search by title or author..."
          className="border p-2 rounded w-1/2"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          className="border p-2 rounded"
          value={genre}
          onChange={(e) => setGenre(e.target.value)}
        >
          <option value="">All Genres</option>
          <option value="FICTION">Fiction</option>
          <option value="NON_FICTION">Non-Fiction</option>
          <option value="MYSTERY">Mystery</option>
          <option value="FANTASY">Fantasy</option>
          <option value="SCIENCE_FICTION">Science Fiction</option>
          <option value="BIOGRAPHY">Biography</option>
          <option value="HISTORY">History</option>
          <option value="ROMANCE">Romance</option>
          <option value="HORROR">Horror</option>
          <option value="SELF_HELP">Self Help</option>
        </select>

        <button onClick={openAddModal} className="button-primary">
          Add Book
        </button>
      </div>

      <BooksTable
        books={books}
        loading={loading}
        onEdit={openEditModal}
        onDelete={handleDelete}
      />

      {showModal && (
        <AddBookModal
          book={editingBook}
          onClose={() => setShowModal(false)}
          onSuccess={handleSuccess}
        />
      )}
    </div>
  );
}