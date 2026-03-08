from flask import Blueprint, request, render_template, redirect, session
import sqlite3

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database/users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            session["user"] = user[1]
            return redirect("/")

    return render_template("login.html")