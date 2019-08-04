from app import app, request, bcrypt, jsonify
from app.models import User


@app.route('/register', methods=['POST'])
def register():
    info = request.json
    print(info)
    return ''
