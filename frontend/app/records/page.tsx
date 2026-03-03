"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";

export default function RecordsPage() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    apiRequest("/records/")
      .then(setRecords)
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>Issue Records</h1>

      {records.map((record: any) => (
        <div key={record.id}>
          Record ID: {record.id} | Copy: {record.book_copy} | Status:{" "}
          {record.status}
        </div>
      ))}
    </div>
  );
}