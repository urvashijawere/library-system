"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";

export default function BooksPage() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    apiRequest("/books/")
      .then(setBooks)
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>Books</h1>
      {books.map((book: any) => (
        <div key={book.id}>
          {book.title} - {book.author}
        </div>
      ))}
    </div>
  );
}