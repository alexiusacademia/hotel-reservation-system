from app import app, db, jsonify, request


@app.route('/checkout')
def checkout():
    if 'room_id' not in request.args:
        return jsonify({
            'success': False,
            'message': 'room_id must be specified in the args.'
        })

    room_id = request.args['room_id']

    return jsonify({})
