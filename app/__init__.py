from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import os


# base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.abspath(os.getcwd())

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Initialize db
db = SQLAlchemy(app)

# Initialize ma
ma = Marshmallow(app)

# Initialize bcrypt
bcrypt = Bcrypt(app)

# Initialize Mail
mail = Mail(app)