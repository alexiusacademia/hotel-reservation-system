from app import app, jsonify, token_required
from app.models import Room, RoomType, rooms_schema


@app.route('/rooms')
# @token_required
def rooms():
    rooms = Room.query.all()

    _rooms_list = []

    for room in rooms:
        _room = {}
        _room['id'] = room.id
        _room['available'] = room.available
        _room['room_number'] = room.room_number
        _room['price'] = room.type.price
        _room['type'] = room.type.name

        _rooms_list.append(_room)
        
    return jsonify(_rooms_list)
