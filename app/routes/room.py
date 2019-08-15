from app import app, token_required
from app.models import Room, room_schema


@app.route('/room/<int:id>')
# @token_required
def room(id):
    _room = Room.query.get(id)

    return room_schema.jsonify(_room)
