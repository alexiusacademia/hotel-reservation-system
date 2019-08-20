from app import app, request, jsonify, db
from app.models import Room


@app.route('/book')
def book():
    if 'room_id' not in request.args:
        return jsonify({'success': False, 'message': 'room_id must be in the args.'})

    room_id = request.args['room_id']

    try:
        room_id = int(room_id)
    except Exception as e:
        print(e)

    room = Room.query.get(room_id)
    available_rooms = room.available_rooms

    if available_rooms == 0:
        return jsonify({
            'success': False,
            'available_rooms': 0,
            'message': 'There are no rooms available'
        })

    room.available_rooms = available_rooms - 1
    db.session.commit()

    return jsonify({
        'success': True,
        'available_rooms': room.available_rooms
    })
