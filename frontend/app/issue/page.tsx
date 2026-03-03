"use client";

import { useState } from "react";
import { apiRequest } from "@/lib/api";

export default function IssuePage() {
  const [bookCopy, setBookCopy] = useState("");
  const [member, setMember] = useState("");
  const [dueDate, setDueDate] = useState("");

  const handleIssue = async () => {
    await apiRequest("/records/issue/", "POST", {
      book_copy: bookCopy,
      member: member,
      due_date: dueDate,
    });

    alert("Book Issued!");
  };

  return (
    <div>
      <h1>Issue Book</h1>

      <input
        placeholder="Book Copy ID"
        onChange={(e) => setBookCopy(e.target.value)}
      />
      <input
        placeholder="Member ID"
        onChange={(e) => setMember(e.target.value)}
      />
      <input
        type="datetime-local"
        onChange={(e) => setDueDate(e.target.value)}
      />

      <button onClick={handleIssue}>Issue</button>
    </div>
  );
}