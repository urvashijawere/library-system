"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";

export default function BookCopiesPage() {
  const [copies, setCopies] = useState([]);

  useEffect(() => {
    apiRequest("books/book-copies/")
      .then(setCopies)
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>Book Copies</h1>
      {copies.map((copy: any) => (
        <div key={copy.id}>
          Copy ID: {copy.id} | Status: {copy.status}
        </div>
      ))}
    </div>
  );
}