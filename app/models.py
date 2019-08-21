from app import db, ma


# Room Table
class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
    room_number = db.Column(db.String(15), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('room_type.id'), nullable=False, default=1)
    type = db.relationship('RoomType', backref='room_type', lazy=True)

    def __init__(self, *args, **kwargs):
        self.room_number = kwargs['room_number']
        self.price = kwargs['price']
        self.type_id = kwargs['type']

    def __repr__(self):
        return f"Room(Name:{self.room_number}, Price:{self.type.price}, Available:{self.available})"


# Room Schema
class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'qty', 'price', 'available_rooms')


class RoomType(db.Model):
    __tablename__ = 'room_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"RoomType(Name:{self.name}, Price:{self.price})"


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
