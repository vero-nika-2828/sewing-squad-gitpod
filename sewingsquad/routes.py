# Imports
from flask import render_template
from sewingsquad import app, db
from sewingsquad.models import Users, SewingWorks


@app.route("/")
def landing_page():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")
