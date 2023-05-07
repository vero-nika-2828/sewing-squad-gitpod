# Imports
from flask import render_template, request, flash, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from sewingsquad import app, db
from sewingsquad.models import Users, SewingWorks


@app.route("/")
def landing_page():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        # If username already exists - flash messages
        if existing_user:
            flash("This username already exists."), 
            flash("Please choose another unsername")
            return redirect(url_for("template.register"))

        newuser = Users(
            firstname=request.form.get("firstname").lower(),
            username=request.form.get("username").lower(),
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password")),
        )

        # Add to database
        db.sessionadd(newuser)
        db.session.commit()

        flash("Registration successful")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # check if username exists in database
    if request.method == "POST":
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()
    
        if existing_user:
            # ensure hashed pasword matches use input
            if check_password_hash(
                    existing_user[0].password,
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back,{}".format(
                    request.form.get("firstname").capitalize()))
                return redirect(
                    url_for(
                        "my_work",
                        username=session["user"]))

            else:
                flash("Incorrect Username and/or Password") 
                return redirect(url_for("login"))   

        else:
            flash("Incorrect Username and/or Password")       

    return render_template("login.html")
