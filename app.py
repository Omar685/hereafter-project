from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from models import (SQLite3Executor, MySQLExecutor)
from random_generator import generator_random_string
import pymysql

import os

app = Flask(__name__)
app.secret_key = open("secret.key", 'r').read()

executor = MySQLExecutor("localhost", "root", "123456789987654321mM.", "akhirah", port=9500)
executor.connect()


@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["mailInput"]
    password = request.form["passInput"]
 
    user = executor.fetchone(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
    if user:
      print(f"ID: '{user[0]}' - Name: '{user[1]}' Username: '{user[2]}' - Email: '{user[3]}' - Password: '{user[4]}' - Logo path: '{user[5]} - Age: '{user[6]} - Location: '{user[7]}")
      session['email'] = user[3]
      session['password'] = user[4]
      # Set cookies and redirect to index
      resp = make_response(redirect(url_for("index")))
      resp.set_cookie("email", email, max_age=60*60*24*30)
      resp.set_cookie("password", password, max_age=60*60*24*30)
      return resp
    
    else:
      flash("Invalid credentials", 'danger')
      return redirect(url_for("login"))
  
  return render_template("login.html")

@app.route("/test")
def test():
  user = executor.fetchone(f"SELECT * FROM users WHERE id=1;")
  # return f"ID: '{user[0]}' - Name: '{user[1]}' Username: '{user[2]}' - Email: '{user[3]}' - Password: '{user[4]}' - Logo path: '{user[5]} - Age: '{user[6]} - Location: '{user[7]}"
  return f'<img src="{user[5]}">'

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["passwd"]

    while True:
      generate_username = generator_random_string()
      check_username = executor.fetchone(f"SELECT * FROM users WHERE username='{generate_username}';")
      if check_username:
        continue
      else:
        username = generate_username
        try:
          executor.execute(f"INSERT INTO users(name, username, email, password) VALUES('{name}', '{username}', '{email}', '{password}')")
          flash("Registration seccessful", 'success')
          os.mkdir(os.path.join("data/users/") + username)
          return redirect(url_for("login"))
        
        except pymysql.IntegrityError:
          flash("Email already exists", 'danger')
          return redirect(url_for("register"))
  return render_template("register.html")

@app.route("/")
def index():
  user = request.cookies.get("email")
  if user:
    return f"Welcome {user}"
  else:
    return redirect(url_for('login'))

@app.route("/profile")
def profile():
  # return f"ID: '{user[0]}' - Name: '{user[1]}' Username: '{user[2]}' - Email: '{user[3]}' - Password: '{user[4]}' - Logo path: '{user[5]} - Age: '{user[6]} - Location: '{user[7]}"
  email = request.cookies.get("email")
  password = request.cookies.get("password")
  user =  executor.fetchone(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
  
  # name=user[1]
  # followers=user[8]
  # following=user[9]
  
  if user:
    return "Profile"
    # return render_template("profile.html")
  else:
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('email', None)
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('email', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")