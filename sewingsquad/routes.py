# Imports
from flask import render_template, request, flash, session, redirect, url_for
from sewingsquad import app, db
from sewingsquad.models import Users, SewingWorks


@app.route("/")
def landing_page():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        registered_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        # If username already exists - flash messages
        if registered_user:
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


@app.route("/login")
def login():
    return render_template("login.html")
