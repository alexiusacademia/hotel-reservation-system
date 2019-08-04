from app import app, bcrypt, request, jsonify, make_response
from app.models import User, user_schema
import jwt
import datetime


@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    email = auth['email']
    password = auth['password']

    # Check if user exist
    user = User.query.filter_by(email=email).first()

    authenticated = False

    if user:
        authenticated = bcrypt.check_password_hash(user.password, password)

        if authenticated:

            token = jwt.encode({'user_email': email,
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                               str(app.config['SECRET_KEY']))
            print(app.config['SECRET_KEY'])
            # Decode to regular string
            token = token.decode('utf-8')

            return jsonify({'token': token})

    return make_response('Authentication failed', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})