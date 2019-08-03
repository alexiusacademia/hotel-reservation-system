from app import db, ma


# Room Table
class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    qty = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    available_rooms = db.Column(db.Integer)

    def __repr__(self):
        return f"Room(Name:{self.name}, Qty:{self.qty}, Price:{self.price}, Available:{self.available_rooms})"


# Room Schema
class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'qty', 'price', 'available_rooms')


# Initialize schema
room_schema = RoomSchema(strict=True)
rooms_schema = RoomSchema(many=True, strict=True)
