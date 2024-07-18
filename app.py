from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from models import (SQLite3Executor, MariaDBExecutor)
import pymysql
import os

app = Flask(__name__)
executor = MariaDBExecutor("localhost", "root", "123456789mM.", "alakhrah")
executor.connect()

app.secret_key = open("secret.key", 'r').read()
# app.config.update(
#   SESSION_COOKIE_HTTPONLY=True,
#   SESSION_COOKIE_SECURE=True,
#   SESSION_COOKIE_SAMESITE='Lax'
# )

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["mailInput"]
    password = request.form["passInput"]
 
    user = executor.fetchone(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
    if user:
      print(f"ID: '{user[0]}' - Name: '{user[1]}' - Email: '{user[2]}' Password: '{user[3]}'")
      session['email'] = user[2]
      session['password'] = user[3]
      return redirect(url_for("index"))
    else:
      print("Invalid credentials", 'error')
      return redirect(url_for("login"))
  
  return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["passwd"]
      
    try:
      executor.execute(f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}')")
      print("Registration seccessful", 'success')
      return redirect(url_for("login"))
    
    except pymysql.IntegrityError:
      print("Email already exists", 'error')
      return redirect(url_for("register"))
  
  return render_template("register.html")

@app.route("/")
def index():
  if 'email' in session:
    return f"Welcome {session['email']}"
  else:
    return redirect(url_for('login'))

@app.route("/profile")
def profile():
  return "Test"

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")