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
def index():
    return render_template("index.html")


# About page
@app.route("/about")
def about():
    return render_template("about.html")


# Recipes page
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("_id", -1))
    return render_template("recipes/recipes.html", recipes=recipes)


# Single recipe page
@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipes/single_recipe.html", recipe=recipe)


# Search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes/recipes.html", recipes=recipes)


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username is not available!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have successfully been registered with MAMAMAKI!")
        return redirect(url_for("personal", username=session["user"]))
    return render_template("user/register.html")


# Log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "personal", username=session["user"]))
            else:
                flash("Sorry, this Username and/or Password is incorrect")
                return redirect(url_for("login"))

        else:
            flash("Sorry, this Username and/or Password is incorrect")
            return redirect(url_for("login"))

    return render_template("user/login.html")


# Personal recipe page
@app.route("/personal/<username>", methods=["GET", "POST"])
def personal(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find().sort("_id", -1))

    if session["user"]:
        return render_template(
            "user/personal.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


# Log out
@app.route("/logout")
def logout():
    flash("Goodbye / Sayōnara, you have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe_is_vegetarian = "on" if request.form.get(
            "recipe_is_vegetarian") else "off"
        recipe = {
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
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe is added successfully")
        return redirect(url_for("personal", username=session["user"]))

    return render_template("recipes/add_recipe.html")


# Edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    if request.method == "POST":
        recipe_is_vegetarian = "on" if request.form.get(
            "recipe_is_vegetarian") else "off"
        save = {
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
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, save)
        flash("Your recipe is updated successfully")
        return redirect(url_for("personal", username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipes/edit_recipe.html", recipe=recipe)


# Delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe is deleted successfully")
    return redirect(url_for("get_recipes"))


# Error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
