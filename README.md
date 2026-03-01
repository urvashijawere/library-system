# Library System

A simple library management system with a Django REST API backend and a Next.js frontend, all containerized with Docker.

## About the Project
- **Backend:** Django REST API for managing books, users, and records.
- **Frontend:** Next.js app for user interaction.

## Main APIs
- `/api/books/` — List, add, update, or delete books
- `/api/users/` — Manage library users
- `/api/records/` — Borrow/return records

## Docker Setup & Starting the System

1. **Install Docker:**
   - Download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop/).
   - Make sure Docker is running on your machine.

2. **Build and Start the System:**
   - Open a terminal in the project root directory.
   - Run:
     ```bash
     docker-compose up --build
     ```
   - This will build the images and start both backend and frontend containers.

3. **Access the Application:**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend: [http://localhost:8000](http://localhost:8000)

4. **Stop the System:**
   - Press `Ctrl+C` in the terminal, then run:
     ```bash
     docker-compose down
     ```

---
For more, see `frontend/README.md` and Django docs in `library_core/`.
