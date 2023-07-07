from sewingsquad import db


class Users(db.Model):
    # schema for the Users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(260), unique=True, nullable=False)
    email = db.Column(db.String(260), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    users_works = db.relationship(
        "SewingWorks", backref="users", cascade="all, delete", lazy=True)
    users_comments = db.relationship(
        "Comments", backref="users", cascade="all, delete", lazy=True)
  
    def __repr__(self):
        return self.username


class SewingWorks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(
        db.String(260), unique=True, nullable=False)
    category = db.Column(
        db.String(260), nullable=False)
    fabric_type = db.Column(
        db.String(260), nullable=False)
    fabric_quantity = db.Column(
        db.Integer, nullable=False)
    other_materials = db.Column(
        db.String(260), nullable=False)
    sewing_time = db.Column(
        db.Integer, nullable=False)
    sewing_tip = db.Column(
        db.Text, nullable=False)
    instructions = db.Column(
        db.Text, nullable=False)    
    photo_URL = db.Column(
        db.String(260), nullable=False)
    secondaryphoto_URL = db.Column(
        db.String(260))
    users_id = db.Column(
        db.Integer, db.ForeignKey(
            "users.id"), nullable=False)
    works_comments = db.relationship(
        "Comments", backref="sewing_works", cascade="all, delete", lazy=True)  

    def __repr__(self):
        return self.project_name
        

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(
        db.Text, nullable=False)
    comment_userid = db.Column(
        db.Integer, db.ForeignKey(
            "users.id"), nullable=False)
    comment_worksid = db.Column(
        db.Integer, db.ForeignKey(
            "sewing_works.id"), nullable=False) 

    def __repr__(self):
        return self.comment


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(260), unique=True, nullable=False)

    def __repr__(self):
        return self.category