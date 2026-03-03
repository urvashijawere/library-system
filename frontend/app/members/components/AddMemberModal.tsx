"use client";

import { useState, useEffect } from "react";
import { apiRequest } from "@/lib/api";

export default function AddMemberModal({
  member,
  onClose,
  onSuccess,
}: any) {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    email: "",
    membership_id: "",
    id_proof_type: "",
    id_proof_number: "",
  });

  useEffect(() => {
    if (member) {
      setFormData({
        ...formData,
        ...member,
        username: member.user.username,
        email: member.user.email,
        password: "", // don't prefill password
      });
    }
  }, [member]);

  const handleChange = (e: any) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    try {
      if (member) {
        await apiRequest(
          `/users/members/${member.id}/`,
          "PUT",
          formData
        );
      } else {
        await apiRequest(
          `/users/members/`,
          "POST",
          formData
        );
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
          {member ? "Update Member" : "Add Member"}
        </h2>

        <form onSubmit={handleSubmit} className="space-y-3">
          <input
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            className="border p-2 w-full"
          />

          {!member && (
            <input
              name="password"
              type="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleChange}
              className="border p-2 w-full"
            />
          )}

          <input
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            className="border p-2 w-full"
          />

          <input
            name="membership_id"
            placeholder="Membership ID"
            value={formData.membership_id}
            onChange={handleChange}
            className="border p-2 w-full"
          />

          <input
            name="id_proof_type"
            placeholder="ID Proof Type"
            value={formData.id_proof_type}
            onChange={handleChange}
            className="border p-2 w-full"
          />

          <input
            name="id_proof_number"
            placeholder="ID Proof Number"
            value={formData.id_proof_number}
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
              {member ? "Update" : "Create"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}