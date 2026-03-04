"use client";

export default function MembersTable({
  members,
  loading,
  onEdit,
  onDelete,
}: any) {
  return (
    <div className="overflow-x-auto border rounded-lg">
      <table className="min-w-full text-sm text-left">
        <thead className="bg-gray-100 text-gray-700 uppercase text-xs">
          <tr>
            <th className="px-4 py-3">Username</th>
            <th className="px-4 py-3">Email</th>
            <th className="px-4 py-3">Phone number</th>
            <th className="px-4 py-3">Membership ID</th>
            <th className="px-4 py-3">ID Proof Type</th>
            <th className="px-4 py-3">ID Proof Number</th>
            <th className="px-4 py-3">Actions</th>
          </tr>
        </thead>

        <tbody>
          {loading ? (
            <tr>
              <td colSpan={6} className="text-center py-6">
                Loading...
              </td>
            </tr>
          ) : members.length === 0 ? (
            <tr>
              <td colSpan={6} className="text-center py-6">
                No Members Found
              </td>
            </tr>
          ) : (
            members.map((member: any) => (
              <tr
                key={member.id}
                className="border-t hover:bg-gray-50 transition"
              >
                <td className="px-4 py-3">{member.user.username}</td>
                <td className="px-4 py-3">{member.user.email}</td>
                <td className="px-4 py-3">{member.user.phone_number}</td>
                <td className="px-4 py-3">{member.membership_id}</td>
                <td className="px-4 py-3">{member.id_proof_type}</td>
                <td className="px-4 py-3">{member.id_proof_number}</td>
                <td className="px-4 py-3">
                  <div className="flex gap-3">
                    <button
                      onClick={() => onEdit(member)}
                      className="text-blue-600 hover:underline"
                    >
                      Edit
                    </button>

                    <button
                      onClick={() => onDelete(member.id)}
                      className="text-red-600 hover:underline"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}