import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        accent: "var(--accent)",
        primary: "var(--primary)",
        secondary: "var(--secondary)",
        card: "var(--card-bg)",
      },
    },
  },
  plugins: [],
};

export default config;