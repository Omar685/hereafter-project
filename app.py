from config import executor
from random_generator import generator_random_string

from flask import Flask, render_template, request, redirect, url_for, make_response, flash, jsonify, send_from_directory
import pymysql
import time
import os
import re

app = Flask(__name__)
app.secret_key = open("secret.key", 'r').read()


@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["mailInput"]
    password = request.form["passInput"]
 
    user = executor.fetchone(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
    if user:
      # Set cookies and redirect to index
      resp = make_response(redirect(url_for("index")))
      resp.set_cookie("email", email, max_age=60*60*24*30)
      resp.set_cookie("password", password, max_age=60*60*24*30)
      return resp
    
    else:
      flash("Invalid credentials", 'danger')
      return redirect(url_for("login"))
  
  return render_template("login.html")

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
          date = time.strftime('%m-%d')
          executor.execute(
            f"INSERT INTO users(name, username, email, password) VALUES('{name}', '{username}', '{email}', '{password}')"
            )
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
    return f'Welcome {user} -> <a href="/profile">Profile</a>'
  else:
    return redirect(url_for('login'))

@app.route("/profile", methods=["GET"])
def profile():
  email = request.cookies.get("email")
  password = request.cookies.get("password")
  user =  executor.fetchone(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
  
  if user:
      
    id=user[0]
    posts = executor.fetch_query(f"SELECT * FROM posts WHERE user_id={id};")
    name = user[1]
    username = user[2]
    logo=user[5]
    cover=user[6]
    age=user[7]
    location=user[8]
    followers=user[9]
    following=user[10]
    # ------------- cmments -------------
    comments = executor.fetch_query(f"SELECT * FROM posts WHERE user_id={id};")

    # --------------- end ---------------
    return render_template("profile.html", 
        name=name, username=username, logo=logo, cover=cover,
        age=age, location=location, followers=followers, following=following, posts=posts)
  else:
    return redirect(url_for('login'))
  
@app.route('/api/send-post', methods=['POST'])
def api_send_post(): 
  data = request.get_json()
  email = request.cookies.get("email")
  password = request.cookies.get("password")
  user =  executor.fetchone(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
  
  id=user[0]
  content = data.get('content')
  executor.execute(f"INSERT INTO posts(user_id, content) VALUES({id}, '{content}');")
  
  return jsonify({"status": "success", 'message': "data received"}), 200

@app.route('/api/send-comment', methods=['POST'])
def api_send_comment(): 
  data = request.get_json()
  email = request.cookies.get("email")
  password = request.cookies.get("password")
  user =  executor.fetchone(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
  
  id=user[0]
  content = data.get('content')
  post_id = data.get('post_id')
  # select * from posts;
  executor.execute(f"INSERT INTO comments(post_id, user_id, content) VALUES({post_id}, {id}, '{content}');")
  
  return jsonify({"status": "success", 'message': "data received"}), 200

@app.route("/post.js")
def api_postjs():
  return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'apis/dist/post.js')

@app.route("/comment.js")
def api_commentjs():
  return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'apis/dist/comment.js')

@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('email', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")