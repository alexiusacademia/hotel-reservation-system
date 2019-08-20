from app import app, request, jsonify


@app.route('/book')
def book():
    if 'room_id' not in request.args:
        return jsonify({'success': False, 'message': 'room_id must be in the args.'})

    room_id = request.args['room_id']

    print(room_id)

    return jsonify({'success': True})
