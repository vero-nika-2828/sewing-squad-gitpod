# Imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

# Create and instance of the imported Flask Class
app = Flask(__name__)
# Specify app configuration variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


# Import the instance of SQLAlchemy class and
# Assing it to a variable db
# Set to the instance of the Flask app
db = SQLAlchemy(app)

# Import routes from local sewingsquad package
from sewingsquad import routes  # noqa