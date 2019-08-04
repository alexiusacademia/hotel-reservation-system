from flask import Flask, request, jsonify
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
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'syncsoftsolutions.software'
app.config['MAIL_PASSWORD'] = 'M@y31l9BB'
app.config.from_envvar('EMAIL_PASSWORD')
app.config['SECRET_KEY'] = ''

# Initialize db
db = SQLAlchemy(app)

# Initialize ma
ma = Marshmallow(app)

# Initialize bcrypt
bcrypt = Bcrypt(app)

# Initialize Mail
mail = Mail(app)