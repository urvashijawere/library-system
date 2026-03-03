const BASE_URL = "http://127.0.0.1:8000/api/v1";

import toast from "react-hot-toast";

export async function apiRequest(
  endpoint: string,
  method: string = "GET",
  body?: any
) {
    try{
        const res = await fetch(`${BASE_URL}${endpoint}`, {
        method,
        headers: {
          "Content-Type": "application/json",
        },
        body: body ? JSON.stringify(body) : undefined,
      });

      const data = await res.json();

      // Handle 204 No Content (DELETE)
      if (res.status === 204) {
        return null;
      }

      if (!res.ok) {
          const errorMessage = parseErrorMessage(data);
          toast.error(errorMessage);
          throw new Error(errorMessage);
      }
      return data;

    } catch (error: any) {
        throw error;
    }
}

function parseErrorMessage(data: any): string {
      // Case 1: Standard DRF detail error
      if (data?.detail) {
        return data.detail;
      }

      // Case 2: Field validation errors
      if (typeof data === "object") {
        const messages: string[] = [];

        for (const key in data) {
          if (Array.isArray(data[key])) {
            messages.push(`${key}: ${data[key].join(", ")}`);
          }
        }

        if (messages.length > 0) {
          return messages.join(" | ");
        }
      }

      return "Something went wrong";
}