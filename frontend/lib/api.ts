const BASE_URL = "http://127.0.0.1:8000/api/v1";

export async function apiRequest(
  endpoint: string,
  method: string = "GET",
  body?: any
) {
  const res = await fetch(`${BASE_URL}${endpoint}`, {
    method,
    headers: {
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!res.ok) {
    throw new Error(`API Error: ${res.status}`);
  }

  // Handle 204 No Content (DELETE)
  if (res.status === 204) {
    return null;
  }

  return res.json();
}