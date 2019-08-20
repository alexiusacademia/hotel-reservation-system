from app import app, request, jsonify


@app.route('/book')
def book():
    room_id = request.args['room_id']

    print(room_id)

    return jsonify(request.args)