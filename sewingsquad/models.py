from sewingsquad import db


class Users(db.Model):
    # schema for the Users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(72), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    users_works = db.relationship(
        "SewingWorks", backref="users", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.username


class SewingWorks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(
        db.String(60), unique=True, nullable=False)
    category = db.Column(
        db.String(15), nullable=False)
    fabric_type = db.Column(
        db.String(15), nullable=False)
    fabric_quantity = db.Column(
        db.Integer, nullable=False)
    other_materials = db.Column(
        db.String(15), nullable=False)
    sewing_time = db.Column(
        db.Integer, nullable=False)
    sewing_tip = db.Column(
        db.Text, nullable=False)
    photo_URL = db.Column(
        db.String(250), nullable=False)
    users_id = db.Column(
        db.Integer, db.ForeignKey(
            "users.id"), nullable=False)

    def __repr__(self):
        return self
        print("SewingWorks database is pulled")
