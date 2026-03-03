"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";
import MembersTable from "./components/MembersTable";
import AddMemberModal from "./components/AddMemberModal";

export default function MembersPage() {
  const [members, setMembers] = useState<any[]>([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  const [showModal, setShowModal] = useState(false);
  const [editingMember, setEditingMember] = useState<any | null>(null);

  useEffect(() => {
    fetchMembers();
  }, [search]);

  const fetchMembers = async () => {
    setLoading(true);

    let query = `/users/members/?`;
    if (search) query += `search=${search}&`;

    try {
      const data = await apiRequest(query);
      setMembers(data.results || data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const openAddModal = () => {
    setEditingMember(null);
    setShowModal(true);
  };

  const openEditModal = (member: any) => {
    setEditingMember(member);
    setShowModal(true);
  };

  const handleDelete = async (id: number) => {
    const confirmed = window.confirm("Delete this member?");
    if (!confirmed) return;

    try {
      await apiRequest(`/users/members/${id}/`, "DELETE");
      fetchMembers();
    } catch (err) {
      console.error(err);
    }
  };

  const handleSuccess = () => {
    setShowModal(false);
    fetchMembers();
  };

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-semibold">Members</h1>

      <div className="flex gap-4 items-center">
        <input
          type="text"
          placeholder="Search by username or email..."
          className="border p-2 rounded w-1/2"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <button onClick={openAddModal} className="button-primary">
          Add Member
        </button>
      </div>

      <MembersTable
        members={members}
        loading={loading}
        onEdit={openEditModal}
        onDelete={handleDelete}
      />

      {showModal && (
        <AddMemberModal
          member={editingMember}
          onClose={() => setShowModal(false)}
          onSuccess={handleSuccess}
        />
      )}
    </div>
  );
}