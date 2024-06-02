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
    hairs = list(mongo.db.hairs.find())
    return render_template("hairs.html", hairs=hairs)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    hairs = list(mongo.db.hairs.find(
                        {"$text": {"$search": query}}))
    return render_template("hairs.html", hairs=hairs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
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

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        user_exist = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exist:
            # ensure hashed password matches user input
            if check_password_hash(
                    user_exist["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab only the session["user"] profile
    if session["user"].lower() == username.lower():
        # find the session["user"] record
        user = mongo.db.users.find_one({"username": username})
        # grab only the houseplants by this session["user"]
        hairs = list(mongo.db.hairs.find({"created_by": username}))
        return render_template(
                "profile.html", user=user, hairs=hairs)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_hairstyle", methods=["GET", "POST"])
def add_hairstyle():
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
            mongo.db.hairs.replace_one(
                                {"_id": ObjectId(hair_id)}, submit)
            flash("Hairstyle Successfully Updated")

        hair = mongo.db.hairs.find_one({"_id": ObjectId(hair_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template(
                            "edit_hairstyle.html", hair=hair,
                            categories=categories)   


@app.route("/delete_hairstyle/<hair_id>")
def delete_hairstyle(hair_id):
    mongo.db.hairs.remove({"_id": ObjectId(hair_id)})
    flash("Hairstyle Successfully Deleted")
    return redirect(url_for("get_hairs"))                              



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
             