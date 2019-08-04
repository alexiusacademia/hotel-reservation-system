from app import app, jsonify, token_required
from app.models import Room, rooms_schema


@app.route('/rooms')
@token_required
def rooms():
    rooms = Room.query.all()

    result = rooms_schema.dump(rooms)

    return jsonify(result.data)