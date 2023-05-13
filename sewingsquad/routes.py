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
                # id = db.Column(db.Integer, primary_key=True)
                project_name=request.form.get("projectname"),
                category=request.form.get("category"),
                fabric_type=request.form.get("fabrictype"),
                fabric_quantity=request.form.get("fabricquantity"),
                other_materials=request.form.get("othermaterials"),
                sewing_time=request.form.get("sewingtime"),
                sewing_tip=request.form.get("sewingtip"),
                photo_URL=request.form.get("photourl"),
                users_id=user.id,
            )
        db.session.add(project)
        db.session.commit()
        flash('Project Added Successfully!')
        return redirect(url_for("my_projects"))

    return render_template("add_project.html")


