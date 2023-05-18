# Imports
from flask import render_template, request, flash, session, redirect, url_for
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from sewingsquad import app, db
from sewingsquad.models import Users, SewingWorks


@app.route("/")
def landing_page():
    all_projects = list(SewingWorks.query.all())
    return render_template("index.html", all_projects=all_projects)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query").lower()
    all_projects = list(
        SewingWorks.query.filter(
            or_(
                SewingWorks.project_name.like(
                    '%{}%'.format(query)), SewingWorks.category.like(
                        '%{}%'.format(query)))).all())
    return render_template("index.html", all_projects=all_projects)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        # If username already exists - flash messages
        if existing_user:
            flash("This username already exists.") 
            flash("Please choose another unsername")
            return redirect(url_for("template.register"))

        newuser = Users(
            # firstname=request.form.get("firstname").lower(),
            username=request.form.get("username").lower(),
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password")),
        )

        # Add to database
        db.session.add(newuser)
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
                    request.form.get("username").capitalize()))
                return redirect(
                    url_for(
                        "my_projects",
                        username=session["user"]))

            else:
                flash("Incorrect Username and/or Password") 
                return redirect(url_for("login"))   

        else:
            flash("Incorrect Username and/or Password")       

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/my_projects")
def my_projects():
    if "user" in session:
        username = session["user"]
        user = Users.query.filter_by(username=username).first()
        my_projects = list(SewingWorks.query.filter_by(users_id=user.id).all())
       
    return render_template("my_projects.html", my_projects=my_projects)


@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        username = session["user"]

        user = Users.query.filter_by(username=username).first()

        if user:
            project = SewingWorks(
                project_name=request.form.get("projectname").lower(),
                category=request.form.get("category").lower(),
                fabric_type=request.form.get("fabrictype").lower(),
                fabric_quantity=request.form.get("fabricquantity"),
                other_materials=request.form.get("othermaterials").lower(),
                sewing_time=request.form.get("sewingtime"),
                sewing_tip=request.form.get("sewingtip").lower(),
                photo_URL=request.form.get("photourl"),
                users_id=user.id,
            )
        db.session.add(project)
        db.session.commit()
        flash('Project Added Successfully!')
        return redirect(url_for("my_projects"))

    return render_template("add_project.html")


@app.route("/edit_project/<int:sewingwork_id>", methods=["GET", "POST"])
def edit_project(sewingwork_id):
    sewingwork = SewingWorks.query.get_or_404(sewingwork_id)

    if request.method == "POST":
        username = session["user"]

        user = Users.query.filter_by(username=username).first()

        sewingwork.project_name = request.form.get("projectname").lower(),
        sewingwork.category = request.form.get("category").lower(),
        sewingwork.fabric_type = request.form.get("fabrictype").lower(),
        sewingwork.fabric_quantity = request.form.get("fabricquantity"),
        sewingwork.other_materials = request.form.get(
            "othermaterials").lower(),
        sewingwork.sewing_time = request.form.get("sewingtime"),
        sewingwork.sewing_tip = request.form.get("sewingtip").lower(),
        sewingwork.photo_URL = request.form.get("photourl"),
        sewingwork.users_id = user.id,
        db.session.commit()
        flash(
            "Your project has been successfully edited."
            )
    return render_template("edit_project.html", project=sewingwork)


@app.route("/delete_project/<int:sewingwork_id>")
def delete_project(sewingwork_id):
    sewingwork = SewingWorks.query.get_or_404(sewingwork_id)
    db.session.delete(sewingwork)       
    db.session.commit()
    return redirect(url_for("my_projects"))
