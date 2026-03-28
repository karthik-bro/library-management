from flask import Flask, render_template, request, redirect
from datetime import datetime
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("library.db")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                       (username, password))
        user = cursor.fetchone()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Credentials "

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO books(title, author) VALUES(?, ?)", (title, author))
        conn.commit()

        return redirect("/books")

    return render_template("add_book.html")

@app.route("/books")
def view_books():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    return render_template("books.html", books=books)

@app.route("/issue/<int:book_id>")
def issue_book(book_id):
    conn = get_db()
    cursor = conn.cursor()

    # mark book as issued
    cursor.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))

    # insert issue record
    cursor.execute("""
    INSERT INTO issued_books(book_id, user_id, issue_date)
    VALUES(?, ?, ?)
    """, (book_id, 1, datetime.now().strftime("%Y-%m-%d")))

    conn.commit()

    return redirect("/books")

@app.route("/return/<int:book_id>")
def return_book(book_id):
    conn = get_db()
    cursor = conn.cursor()

    # mark book as available
    cursor.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))

    # update return date
    cursor.execute("""
    UPDATE issued_books
    SET return_date=?
    WHERE book_id=? AND return_date IS NULL
    """, (datetime.now().strftime("%Y-%m-%d"), book_id))

    conn.commit()

    return redirect("/books")

if __name__ == "__main__":
    app.run(debug=True)
