"use client";
import { useEffect, useState } from "react";
import Card from "../components/Card";

export default function Home() {
    const [stats, setStats] = useState({
        total_books: 0,
        active_members: 0,
        books_issued: 0,
        });
    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/v1/dashboard/")
          .then((res) => res.json())
          .then((data) => setStats(data))
          .catch((err) => console.error(err));
      }, []);

    return (
        <div className="space-y-8">
          <h2 className="text-3xl font-semibold">Dashboard Overview</h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card>
              <p className="text-gray-500 text-sm">Total Books</p>
              <h3 className="text-2xl font-bold mt-2">{stats.total_books}</h3>
            </Card>

            <Card>
              <p className="text-gray-500 text-sm">Active Members</p>
              <h3 className="text-2xl font-bold mt-2">{stats.active_members}</h3>
            </Card>

            <Card>
              <p className="text-gray-500 text-sm">Books Issued</p>
              <h3 className="text-2xl font-bold mt-2">{stats.books_issued}</h3>
            </Card>
          </div>

          <Card>
            <h3 className="text-xl font-semibold mb-4">Recent Activity</h3>
            <ul className="space-y-2 text-gray-600">
              <li>• John issued "Atomic Habits"</li>
              <li>• Sarah returned "Deep Work"</li>
              <li>• New member registered: Alex</li>
            </ul>
          </Card>

        </div>
      );
    }