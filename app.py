import os
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
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
