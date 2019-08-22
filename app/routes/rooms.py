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


@app.route('/rooms/<int:type_id>')
def rooms_category(type_id):
    try:
        room_type_id = int(type_id)
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Room type id must be an integer.'
        })

    room_type = RoomType.query.get(room_type_id)

    if not room_type:
        return jsonify({
            'success': False,
            'message': f'Room type with id {room_type_id} does not exist.'
        })

    rooms = Room.query.filter_by(type_id=room_type_id).all()

    _rooms = []
    for room in rooms:
        _room = {}
        _room['id'] = room.id
        _room['available'] = room.available
        _room['room_number'] = room.room_number
        _room['price'] = room.type.price
        _room['type'] = room.type.name
        _rooms.append(_room)

    obj = {}

    obj['success'] = True
    obj['rooms'] = _rooms

    return jsonify(obj)
