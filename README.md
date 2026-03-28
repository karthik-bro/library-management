# Library Management System (Web App)

 A full-stack Library Management System built using Python (Flask) + SQLite + HTML + Bootstrap, supporting authentication, book tracking, and real-time issue/return operations.
YOU CAN VIEW WORKING DEMO BY USING THIS BELOW LINK <br>
https://library-management-1-e809.onrender.com
---

# Features

-  User Registration & Login
-  Add & View Books (Web Interface)
-  Issue Books
-  Return Books with Date Tracking
-  Book Availability Status (Available / Issued)
-  Web-based UI using Flask
-  Responsive Design with Bootstrap

---

# System Architecture

Frontend (HTML + Bootstrap)
        ↓
Flask (Python Backend)
        ↓
SQLite Database

---
# Tech Stack

Technology| Usage
Python | Backend Logic
Flask | Web Framework
SQLite | Database
HTML| Frontend
Bootstrap | UI Styling

---

# Project Structure

library-management-system/
│
├── app.py                  # Flask backend
├── library.db              # Database
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── add_book.html
│   └── books.html
│
└── README.md

---

# Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/karthik-bro/library-management.git

2️⃣ Navigate to project folder

cd library-management

3️⃣ Install dependencies

pip install flask

4️⃣ Run the application

python app.py

---

# Usage

1. Open browser:
(with local host as)
http://127.0.0.1:5000/

2. Login with your credentials

3. Use dashboard to:
   
   - Add books
   - View books
   - Issue books
   - Return books

---

# Key Features Explained

 Authentication

- Validates user credentials from database

 Book Management

- Add books through web form
- View all books in table format

 Issue / Return System

- Issue → Marks book as unavailable
- Return → Marks book as available
- Tracks issue & return dates

---

# UI Features

- Clean dashboard
- Table-based book listing
- Status badges (Available / Issued)
- Action buttons (Issue / Return)
- Responsive layout using Bootstrap

---

# Future Enhancements

-  Password Hashing
-  Fine Calculation System
-  Search Functionality
-  Analytics Dashboard
-  Deployment (Render / Railway / Vercel)

---

# Author

Karthik 
CSE student at VTU Mysore.

---

# Support

If you like this project:

-  Star the repo
-  Fork it
-  Share it

---

 License

This project is licensed under the MIT License.
