from app import app
from app.models import Room, room_schema


@app.route('/room/<int:id>')
def room(id):
    _room = Room.query.get(id)

    return room_schema.jsonify(_room)
