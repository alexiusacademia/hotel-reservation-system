from app import db, ma


# Room Table
class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    qty = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    available_rooms = db.Column(db.Integer)

    def __init__(self, name, qty, price, available_rooms):
        self.name = name
        self.qty = qty
        self.price = price
        self.available_rooms = available_rooms

    def __repr__(self):
        return f"Room(Name:{self.name}, Qty:{self.qty}, Price:{self.price}, Available:{self.available_rooms})"


# Room Schema
class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'qty', 'price', 'available_rooms')


class UserType(db.Model):
    __tablename__ = 'user_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"UserType(Id: {self.id}, Name: {self.name})"


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'), nullable=False, default=1)
    user_type = db.relationship('UserType', backref='user_type', lazy=True)
    last_login = db.Column(db.DateTime)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(Email: {self.email}, Level: {self.user_type.name})"


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'user_type_id', 'last_login')


# Initialize schemas
room_schema = RoomSchema(strict=True)
rooms_schema = RoomSchema(many=True, strict=True)
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)
