from app import app, db, jsonify, request
from app.models import Room


@app.route('/checkout')
def checkout():
    if 'room_id' not in request.args:
        return jsonify({
            'success': False,
            'message': 'room_id must be specified in the args.'
        })

    room_id = request.args['room_id']

    room = Room.query.get(room_id)

    if not room:
        return jsonify({
            'success': False,
            'message': f'Room with id {room_id} does not exist.'
        })

    available = room.available

    if available:
        return jsonify({
            'success': False,
            'message': 'You are trying to checkout a room that hasn\'t been booked yet.'
        })

    return jsonify({})
