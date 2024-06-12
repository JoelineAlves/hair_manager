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


@app.route("/")
@app.route("/get_hairs")
def get_hairs():
    """
    Connects to the hair collection in MongoDB, retrieves all records,
    and returns them to the hairs.html template.
    """
    hairs = list(mongo.db.hairs.find())
    return render_template("hairs.html", hairs=hairs)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Receives a search query from a form submitted via POST,
    performs a textual search on the MongoDB hair collection,
    and renders the hairs.html template with the search results.
    """
    query = request.form.get("query")
    hairs = list(mongo.db.hairs.find({"$text": {"$search": query}}))
    return render_template("hairs.html", hairs=hairs)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registers new users if they do not already exist in the database.
    After successful registration, redirects to the user profile.
    """
    if request.method == "POST":
        # Check if username already exists in db
        user_exist = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user_exist:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into the session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles user login authentication. If successful,
    adds the username to the session cookie and redirects
    to the user profile. Otherwise, displays an error message
    and redirects back to the login page.
    """
    if request.method == "POST":
        # Check if username exists in db
        user_exist = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exist:
            # Ensure hashed password matches user input
            if check_password_hash(
                    user_exist["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Displays the user profile and associated data.
    """
    # Ensure the session user is the profile owner
    if "user" in session and session["user"].lower() == username.lower():
        # Find the session user record
        user = mongo.db.users.find_one({"username": username})
        # Grab only the hairs by this session user
        hairs = list(mongo.db.hairs.find({"created_by": username}))
        return render_template(
            "profile.html", user=user, hairs=hairs)
    flash("You are not authorized to view this profile.")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Logs out the current user by removing the session cookie.
    """
    flash("You have been logged out")
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/add_hairstyle", methods=["GET", "POST"])
def add_hairstyle():
    """
    Handles adding a new hairstyle to the database.
    """
    if request.method == "POST":
        hair = {
            "category_name": request.form.get("category_name"),
            "hair_name": request.form.get("hair_name"),
            "common_name": request.form.get("common_name"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "hair_care": request.form.get("hair_care"),
            "date": request.form.get("date"),
            "created_by": session["user"]
        }
        mongo.db.hairs.insert_one(hair)
        flash("Hairstyle Successfully Added")
        return redirect(url_for("get_hairs"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_hairstyle.html", categories=categories)


@app.route("/edit_hairstyle/<hair_id>", methods=["GET", "POST"])
def edit_hairstyle(hair_id):
    """
    Handles editing an existing hairstyle.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "hair_name": request.form.get("hair_name"),
            "common_name": request.form.get("common_name"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "hair_care": request.form.get("hair_care"),
            "date": request.form.get("date"),
            "created_by": session["user"]
        }
        mongo.db.hairs.replace_one({"_id": ObjectId(hair_id)}, submit)
        flash("Hairstyle Successfully Updated")
        return redirect(url_for("get_hairs"))

    hair = mongo.db.hairs.find_one({"_id": ObjectId(hair_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_hairstyle.html", hair=hair, categories=categories
    )


@app.route("/delete_hairstyle/<hair_id>")
def delete_hairstyle(hair_id):
    """
    Handles deleting a hairstyle from the database.
    """
    mongo.db.hairs.delete_one({"_id": ObjectId(hair_id)})
    flash("Hairstyle Successfully Deleted")
    return redirect(url_for("get_hairs"))


@app.route("/get_categories")
def get_categories():
    """
    Retrieves and displays all categories.
    """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Handles adding a new category.
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Handles editing an existing category.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.replace_one({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Handles deleting a category from the database.
    """
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
    