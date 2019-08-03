from app import app
from app.models import User, user_schema


@app.route('/add_user', methods=['POST'])
def add_user():
    pass
