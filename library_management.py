
import sqlite3
from datetime import datetime

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    available INTEGER DEFAULT 1
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    user_id INTEGER,
    issue_date TEXT,
    return_date TEXT
)
""")

conn.commit()

# ---------------- AUTH ----------------
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("INSERT INTO users(username,password) VALUES(?,?)",
                   (username,password))
    conn.commit()
    print(" Registered successfully")


def login():
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username,password))
    user = cursor.fetchone()

    if user:
        print(" Login successful")
        return user[0]
    else:
        print(" Invalid credentials")
        return None


# ---------------- BOOK ----------------
def add_book():
    title = input("Book title: ")
    author = input("Author: ")

    cursor.execute("INSERT INTO books(title,author) VALUES(?,?)",
                   (title,author))
    conn.commit()
    print(" Book added")


def view_books():
    cursor.execute("SELECT * FROM books")
    for book in cursor.fetchall():
        status = "Available" if book[3] == 1 else "Issued"
        print(book[0], book[1], "-", status)


# ---------------- ISSUE ----------------
def issue_book(user_id):
    book_id = int(input("Enter book ID: "))

    cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if book and book[0] == 1:
        cursor.execute("""
        INSERT INTO issued_books(book_id,user_id,issue_date)
        VALUES(?,?,?)
        """, (book_id, user_id, datetime.now().strftime("%Y-%m-%d")))

        cursor.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        conn.commit()
        print(" Book issued")
    else:
        print(" Book not available")


def return_book():
    book_id = int(input("Enter book ID to return: "))

    cursor.execute("""
    UPDATE issued_books
    SET return_date=?
    WHERE book_id=? AND return_date IS NULL
    """, (datetime.now().strftime("%Y-%m-%d"), book_id))

    cursor.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
    conn.commit()

    print(" Book returned")


# ---------------- MENU ----------------
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        user_id = login()
        if user_id:
            while True:
                print("\n--- DASHBOARD ---")
                print("1. Add Book")
                print("2. View Books")
                print("3. Issue Book")
                print("4. Return Book")
                print("5. Logout")

                ch = input("Choose: ")

                if ch == "1":
                    add_book()
                elif ch == "2":
                    view_books()
                elif ch == "3":
                    issue_book(user_id)
                elif ch == "4":
                    return_book()
                elif ch == "5":
                    break

    elif choice == "3":
        break