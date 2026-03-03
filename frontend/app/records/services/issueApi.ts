import { apiRequest } from "@/lib/api";

export const getIssues = () => apiRequest("/records/");

export const issueBook = (data) =>
  apiRequest("/records/issue/", "POST", data);

export const returnBook = (data: {
      book_copy_id: number;
      member_id: number;
    }) => apiRequest("/records/return/", "POST", data);