from app import app, jsonify
from app.models import Room, rooms_schema


@app.route('/rooms')
def rooms():
    rooms = Room.query.all()

    result = rooms_schema.dump(rooms)

    return jsonify(result.data)