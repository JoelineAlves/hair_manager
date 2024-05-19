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
    hairs = mongo.db.hairs.find()
    return render_template("hairs.html", hairs=hairs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # see if username already exists in db
        user_exist = mongo.db.users.find_one(
            {"username" : request.form.get("username").lower()})

        if user_exist:
            flash("Username exists")
            return redirect(url_for("register"))

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register
            # insert the user ina 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Sucessful")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  
             