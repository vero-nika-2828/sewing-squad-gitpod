# Imports
from flask import render_template, request, flash, session, redirect, url_for
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from sewingsquad import app, db
from sewingsquad.models import Users, SewingWorks, Comments, Category


@app.route("/")
def home():
    all_projects = list(SewingWorks.query.all())
    all_users = list(Users.query.all())
    return render_template(
        "index.html", all_projects=all_projects,
        all_users=all_users)


@app.route("/admin")
def admin():
    username = session["user"]
    user = Users.query.filter_by(username=username).first()

    if user.id == 1:
        flash("You are an admin")
        return render_template("admin.html")
    return render_template("index.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.all())

    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    categories = list(Category.query.all())

    if request.method == "POST":
        if session["user"] == "admin":
            new_category = Category(
                category=request.form.get("category").lower(),
                )
            db.session.add(new_category)
            db.session.commit()
            flash("The category has been added successfully")
            return redirect("categories")
        else:
            flash("Only admin can add categories")
            return render_template("categories.html", categories=categories)

    return render_template("categories.html", categories=categories)


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)

    if request.method == "POST":
        category.category = request.form.get("category").lower(),
        db.session.commit()
        flash("The category has been edited successfully.")
        return redirect(url_for("categories"))

    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>", methods=["GET", "POST"])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)

    db.session.delete(category)       
    db.session.commit()
    flash("The category has been deleted successfully")
    return redirect(url_for("categories"))   
  

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query").lower()
    all_projects = list(
        SewingWorks.query.filter(
            or_(
                SewingWorks.project_name.like(
                    '%{}%'.format(query)), SewingWorks.category.like(
                        '%{}%'.format(query)), SewingWorks.fabric_type.like(
                            '%{}%'.format(query)))).all())
            
    results = len(all_projects)

    if results > 0:
        flash("No. of results found for '{}': {}".format(query, results))
        return render_template(
            "index.html", all_projects=all_projects, results=results)     
    else:
        flash("Sorry! No results for '{}'".format(query))
        flash("Please try another search.")
        return render_template(
            "index.html", all_projects=all_projects, results=results)  


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        # If username already exists - notifly user with flash message
        if existing_user:
            flash("This username already exists.") 
            flash("Please choose another username or log in")
            return redirect(url_for("register"))

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
            # ensure hashed pasword matches user input
            if check_password_hash(
                    existing_user[0].password,
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(
                    request.form.get("username").title()))
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


@app.route("/project/<int:sewingwork_id>")
def project(sewingwork_id):
    if "user" in session:
        project_db = SewingWorks.query.get_or_404(sewingwork_id)

        return render_template("project.html", this_project=project_db)
    else:
        flash("You must be logged in to view this project")
        return redirect(url_for("home"))


@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    categories = Category.query.all()

    if request.method == "POST":
        # check if project name exists
        existing_project = SewingWorks.query.filter(
            SewingWorks.project_name == request.form.get(
                "projectname").lower()).all()

        # If project name already existist - notifly user with flash message
        if existing_project:
            flash("Sorry! This project already exist")
            flash("Check Home page or use another project name")

            return redirect(url_for("add_project"))

        # Get the session user name 
        # Filter for the session username in database
        # Get user id for user_id 
        username = session["user"]
        user = Users.query.filter_by(username=username).first()

        if user:
            project = SewingWorks(
                project_name=request.form.get("projectname").lower(),
                category=request.form.get("category").lower(),
                fabric_type=request.form.get("fabrictype"),
                fabric_quantity=request.form.get("fabricquantity"),
                other_materials=request.form.get("othermaterials").lower(),
                sewing_time=request.form.get("sewingtime"),
                sewing_tip=request.form.get("sewingtip").lower(),
                instructions=request.form.get("instructions").lower(),
                photo_URL=request.form.get("photourl"),
                secondaryphoto_URL=request.form.get("secondaryphotourl"),
                users_id=user.id,
            )
        db.session.add(project)
        db.session.commit()
        flash('Project has been added successfully!')
        return redirect(url_for("my_projects"))

    return render_template("add_project.html", categories=categories)


@app.route("/edit_project/<int:sewingwork_id>", methods=["GET", "POST"])
def edit_project(sewingwork_id):
    sewingwork = SewingWorks.query.get_or_404(sewingwork_id)
    categories = Category.query.all()

    try:
        if request.method == "POST":
            username = session["user"]

            user = Users.query.filter_by(username=username).first()

            sewingwork.project_name = request.form.get("projectname").lower(),
            sewingwork.category = request.form.get("category"),
            sewingwork.fabric_type = request.form.get("fabrictype").lower(),
            sewingwork.fabric_quantity = request.form.get(
                "fabricquantity").lower(),
            sewingwork.other_materials = request.form.get(
                "othermaterials").lower(),
            sewingwork.sewing_time = request.form.get("sewingtime"),
            sewingwork.sewing_tip = request.form.get("sewingtip").lower(),
            sewingwork.instructions = request.form.get("instructions").lower(),
            sewingwork.photo_URL = request.form.get("photourl"),
            sewingwork.secondaryphoto_URL = request.form.get(
                "secondaryphotourl"),
            sewingwork.users_id = user.id,
            db.session.commit()
            flash(
                "Your project has been edited successfully ."
                )
            return redirect(url_for("my_projects"))
        
        username = session["user"]

        user = Users.query.filter_by(username=username).first()

        if user.id == sewingwork.users_id or user.id == 1:
            return render_template(
                "edit_project.html", project=sewingwork, categories=categories)
        else:
            flash("Only an admin or the owner of the post can edit it")
            return redirect(url_for("home"))
    except KeyError:
        flash("You must be logged in to edit posts")
        return redirect(url_for("login"))

        
@app.route("/delete_project/<int:sewingwork_id>")
def delete_project(sewingwork_id): 
    sewingwork = SewingWorks.query.get_or_404(sewingwork_id)
        
    db.session.delete(sewingwork)       
    db.session.commit()
    flash("The post has been deleted successfully")
    return redirect(url_for("my_projects"))

   
@app.route("/add_comment/<int:sewingwork_id>", methods=["POST"])
def add_comment(sewingwork_id):
    if request.method == "POST":
        username = session["user"]
      
        user = Users.query.filter_by(username=username).first()
        sewingwork = SewingWorks.query.get_or_404(sewingwork_id)
        comments = list(Comments.query.all())
        
        if user:
            comment = Comments(
                comment=request.form.get("comment"),
                comment_userid=user.id,
                comment_worksid=sewingwork.id,
            )
        db.session.add(comment)
        db.session.commit()
        flash('Comment added successfully!')
        return render_template(
            "project.html", this_project=sewingwork, comments=comments)


@app.route("/edit_comment/<int:comment_id>", methods=["GET", "POST"])
def edit_comment(comment_id):
    comment = Comments.query.get_or_404(comment_id)
    commented_sewingwork = comment.comment_worksid
        
    if request.method == "POST":
        comment.comment = request.form.get("comment").lower(),

        db.session.commit()
        flash("The comment has been edited successfully")
        return redirect(url_for("project", sewingwork_id=commented_sewingwork))


@app.route("/delete_comment/<int:comment_id>", methods=["GET", "POST"])
def delete_comment(comment_id):
    comment = Comments.query.get_or_404(comment_id)
    commented_sewingwork = comment.comment_worksid

    db.session.delete(comment)       
    db.session.commit()
    flash("The comment has been deleted successfully")
    return redirect(url_for("project", sewingwork_id=commented_sewingwork))


@app.errorhandler(404)
def handle_404(error):
    # 404 error handler
    return render_template(
        '404.html'), 404


@app.errorhandler(500)
def handle_500(error):
    # 500 error handler
    return render_template(
        '500.html'), 404