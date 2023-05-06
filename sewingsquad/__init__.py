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
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")


# Import the instance of SQLAlchemy class and
# Assing it to a variable db
# Set to the instance of the Flask app
db = SQLAlchemy(app)

# Import routes from local sewingsquad package
from sewingsquad import routes  # noqa