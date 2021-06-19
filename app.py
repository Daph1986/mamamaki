import os
import re
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Index / homepage
@app.route("/") 
@app.route("/index")
def index():
    return render_template("index.html")


# About page
@app.route("/") 
@app.route("/about")
def about():
    return render_template("about.html")


# All recipes
@app.route("/")
@app.route("/get_recipes")  
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check in db if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        # when username already exists
        if existing_user:
            flash("This username is taken already!")
            return redirect(url_for("register"))

        # creating the username and password
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # place new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully been registered with MAMAMAKI!")
        return redirect(url_for("personal", username=session["user"]))
    return render_template("register.html")


# Log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check in db if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # when username already exists
        if existing_user:
            # checks if hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get(
                        "username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "personal", username=session["user"]))
            else:
                # wrong password
                flash("Sorry, this Username and/or Password is incorrect")
                return redirect(url_for("login"))

        else:
            # not an existing username
            flash("Sorry, this Username and/or Password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


# Log in
@app.route("/personal/<username>", methods=["GET", "POST"])
def personal(username):
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("personal.html", username=username)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
