# -------- Imports and configuration --------
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
if os.path.exists("env.py"):
    import env  # noqa: F401


app = Flask(__name__)

# Setup MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
mongo = client.mamamaki


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# --------- Login required security ---------
# Requires that a user is logged in for certain pages,
# otherwise directs to login page
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "user" in session:
            return f(*args, **kwargs)
        else:
            flash("You must be logged in for this part of the site!")
            return redirect(url_for("login"))
    return wrap


# ------------ Index / homepage -------------
@app.route("/")
def index():
    return render_template("index.html")


# --------------- About page ----------------
@app.route("/about")
def about():
    return render_template("about.html")


# -------------- Recipes page ---------------
@app.route("/recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("_id", -1))
    return render_template("recipes/recipes.html", recipes=recipes)


# ----------- Single recipe page ------------
@app.route("/recipe/<recipe_id>")
def single_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipes/single_recipe.html", recipe=recipe)


# ------------------ Search -----------------
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    print(f"Search query: {query}")  # Voeg logging toe om de query te controleren
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    print(f"Search results: {recipes}")  # Voeg logging toe om de resultaten te controleren
    return render_template("recipes/recipes.html", recipes=recipes)


# ------ User and password validation -------
# Reusable function for registration and login part
def existing_user():
    return mongo.db.users.find_one({"username": request.form.get("username").lower()})


def password_is_valid(existing_user):
    return check_password_hash(
        existing_user["password"], request.form.get("password"))


# -------------- Registration ---------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if existing_user():
            flash("This username is not available!")
            return redirect(url_for("register"))

        username = request.form.get("username")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        register = {
            "username": username.lower(),
            "password": hashed_password
        }
        mongo.db.users.insert_one(register)

        session["user"] = username.lower()
        flash("You have successfully been registered with MAMAMAKI!")
        return redirect(url_for("personal", username=session["user"]))

    return render_template("user/register.html")


# ------------------ Log in ------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = existing_user()

        if user:
            if password_is_valid(user):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(request.form.get("username")))
                return redirect(url_for("personal", username=session["user"]))

            flash("Sorry, this Username and/or Password is incorrect")
            return redirect(url_for("login"))

        flash("Sorry, this Username and/or Password is incorrect")
        return redirect(url_for("login"))

    return render_template("user/login.html")


# ---------- Personal recipe page -----------
@app.route("/user/<username>", methods=["GET", "POST"])
@login_required
def personal(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session.get("user"):
        recipes = list(mongo.db.recipes.find().sort("_id", -1))
        return render_template(
            "user/personal.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


# ----------------- Log out -----------------
@app.route("/logout")
@login_required
def logout():
    flash("Goodbye / Sayōnara, you have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------------- Display recipes -------------
# Reusable function for displaying recipes
def display_recipes(request):
    recipe_is_vegetarian = "on" if request.form.get(
            "recipe_is_vegetarian") else "off"
    return {
            "japanese_recipe_name": request.form.get("japanese_recipe_name"),
            "english_recipe_name": request.form.get("english_recipe_name"),
            "recipe_introduction": request.form.get("recipe_introduction"),
            "recipe_preparation_time": request.form.get(
                "recipe_preparation_time"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_instruction": request.form.getlist("recipe_instruction"),
            "recipe_remarks": request.form.get("recipe_remarks"),
            "recipe_image_1": request.form.get("recipe_image_1"),
            "recipe_image_2": request.form.get("recipe_image_2"),
            "recipe_image_3": request.form.get("recipe_image_3"),
            "recipe_image_4": request.form.get("recipe_image_4"),
            "recipe_additional_notes": request.form.get(
                "recipe_additional_notes"),
            "recipe_is_vegetarian": recipe_is_vegetarian,
            "recipe_created_by": session["user"]
        }


# --------------- Add recipe ----------------
@app.route("/recipe/add", methods=["GET", "POST"])
@login_required
def add_recipe():
    if request.method == "POST":
        recipe = display_recipes(request)
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe is added successfully")
        return redirect(url_for("personal", username=session["user"]))
    return render_template("recipes/add_recipe.html")


# --------------- Edit recipe ---------------
@app.route("/recipe/update/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    if "user" in session:
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

        if recipe is None:
            flash("Recipe not found", "error")
            return redirect(url_for("index"))

        if session["user"] == 'admin' or session["user"].lower() == recipe["recipe_created_by"].lower():
            if request.method == "POST":
                save = display_recipes(request)
                mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": save})
                flash("Your recipe is updated successfully")
                return redirect(url_for("personal", username=session["user"]))
            return render_template("recipes/edit_recipe.html", recipe=recipe)

        flash("Access denied. You can't edit other user's recipes.")
        return redirect(url_for("index"))

    flash("Access denied. You can't edit recipes without logging in.")
    return redirect(url_for("index"))


# -------------- Delete recipe --------------
@app.route("/recipe/delete/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    if "user" in session:
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

        if session["user"] == 'admin' or session["user"].lower() == recipe["recipe_created_by"].lower():
            mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
            flash("Your recipe is deleted successfully")
            return redirect(url_for("get_recipes"))

        flash("Access denied. You can't delete other user's recipes.")
        return redirect(url_for("index"))

    flash("Access denied. You can't delete recipes without logging in.")
    return redirect(url_for("index"))


# -------------- Error handling -------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
