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

    if not room:
        return jsonify({
            'success': False,
            'message': f'The room with id {room_id} does not exist.'
        })

    isavailable = room.available

    if not isavailable:
        return jsonify({
            'success': False,
            'available': False,
            'message': 'Room is not available'
        })

    room.available = False
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Room has been booked.'
    })
