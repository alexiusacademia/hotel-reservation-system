from app import app, token_required, jsonify
from app.models import Room, room_schema, RoomType


@app.route('/room/<int:id>')
# @token_required
def room(id):
    room = Room.query.get(id)

    if not room:
        return jsonify({
            'success': False,
            'message': f'Room with the id {id} dows not exist.'
        })

    _room = {}
    _room['success'] = True
    _room['id'] = room.id
    _room['available'] = room.available
    _room['room_number'] = room.room_number
    _room['price'] = room.type.price
    _room['type'] = room.type.name

    return jsonify(_room)
