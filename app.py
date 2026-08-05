import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            flash("Must provide username.")
            return render_template("register.html")
        elif not password:
            flash("Must provide password.")
            return render_template("register.html")
        elif password != confirmation:
            flash("Passwords must match.")
            return render_template("register.html")

        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(existing_user) > 0:
            flash("Username is already taken.")
            return render_template("register.html")

        hashed_password = generate_password_hash(password)

        new_user_id = db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", 
            username, 
            hashed_password
        )

        session["user_id"] = new_user_id
        flash("Registration successful!")
        
        return redirect("/dashboard")

    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            flash("Must provide username.")
            return render_template("login.html")
        elif not password:
            flash("Must provide password.")
            return render_template("login.html")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username and/or password.")
            return render_template("login.html")

        session["user_id"] = rows[0]["id"]
        flash("Logged in successfully!")

        return redirect("/dashboard")

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    # Query the database for the logged-in user's appointments
    # We use a JOIN to get the username of the provider/instructor
    appointments = db.execute("""
        SELECT appointments.date, appointments.time, users.username AS instructor 
        FROM appointments 
        JOIN users ON appointments.provider_id = users.id 
        WHERE appointments.client_id = ? 
        ORDER BY appointments.date, appointments.time
    """, session["user_id"])
    
    return render_template("dashboard.html", appointments=appointments)

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        provider_id = request.form.get("provider_id")
        date = request.form.get("date")
        time = request.form.get("time")

        if not provider_id or not date or not time:
            flash("Must provide all booking details.")
            return redirect("/book")

        db.execute(
            "INSERT INTO appointments (provider_id, client_id, date, time, status) VALUES (?, ?, ?, ?, 'booked')",
            provider_id, session["user_id"], date, time
        )
        
        flash("Instruction session booked successfully!")
        return redirect("/dashboard")

    else:
        instructors = db.execute("SELECT id, username FROM users WHERE id != ?", session["user_id"])
        return render_template("book.html", instructors=instructors)

@app.route("/resources", methods=["GET", "POST"])
def resources():
    if request.method == "POST":
        pass
    else:
        return render_template("resources.html")