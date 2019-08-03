from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


base_dir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + base_dir + 'db.sqlite'

db = SQLAlchemy(app)