from app import app, db, request, jsonify
from app.models import Room, room_schema


@app.route('/create_room', methods=['POST'])
def create_room():
    name = request.json['name']
    qty = request.json['qty']
    price = request.json['price']
    available_rooms = qty

    room = Room(name, qty, price, available_rooms)
    db.session.add(room)
    db.session.commit()

    return room_schema.jsonify(room)