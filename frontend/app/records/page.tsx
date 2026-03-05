"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";
import RecordsTable from "./components/RecordsTable";
import IssueBookModal from "./components/IssueBookModal";
import ReturnBookModal from "./components/ReturnBookModal";

export default function RecordsPage() {
  const [records, setRecords] = useState<any[]>([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  const [showIssueModal, setShowIssueModal] = useState(false);
  const [returnRecord, setReturnRecord] = useState<any | null>(null);

  useEffect(() => {
    fetchRecords();
  }, [search]);

  const fetchRecords = async () => {
    setLoading(true);

    let query = `/records/?`;
    if (search) query += `search=${search}&`;

    try {
      const data = await apiRequest(query);
      setRecords(data.results || data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSuccess = () => {
    fetchRecords();
  };

  return (
    <div className="space-y-6">
      {/* Same Heading Style */}
      <h1 className="text-3xl font-semibold">Issue Records</h1>

      {/* Same Search + Button Layout */}
      <div className="flex gap-4 items-center">
        <input
          type="text"
          placeholder="Search by status or issue date / due date (YYYY-MM-DD)"
          className="border p-2 rounded w-1/2"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <button
          onClick={() => setShowIssueModal(true)}
          className="button-primary"
        >
          Issue Book
        </button>
      </div>

      {/* Table */}
      <RecordsTable
        records={records}
        loading={loading}
        onReturn={(record) => setReturnRecord(record)}
      />

      {/* Issue Modal */}
      {showIssueModal && (
        <IssueBookModal
          onClose={() => setShowIssueModal(false)}
          onSuccess={handleSuccess}
        />
      )}

      {/* Return Modal */}
      {returnRecord && (
        <ReturnBookModal
          record={returnRecord}
          onClose={() => setReturnRecord(null)}
          onSuccess={() => {
            setReturnRecord(null);
            fetchRecords();
          }}
        />
      )}
    </div>
  );
}