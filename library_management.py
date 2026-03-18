import sqlite3

# connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

conn.commit()

# functions
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter year: "))

    cursor.execute("INSERT INTO books(title,author,year) VALUES(?,?,?)",
                   (title,author,year))
    conn.commit()
    print("✅ Book added successfully")


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n📚 Library Books:")
    for book in books:
        print(book)


def delete_book():
    book_id = int(input("Enter Book ID to delete: "))

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()

    print("🗑 Book deleted successfully")


def update_book():
    book_id = int(input("Enter Book ID to update: "))
    new_title = input("Enter new title: ")

    cursor.execute("UPDATE books SET title=? WHERE id=?",
                   (new_title, book_id))
    conn.commit()

    print("✏ Book updated successfully")


# menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Update Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        delete_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

conn.close()