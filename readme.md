# Hotel Reservation System (Back End)
### SyncSoft Solutions (c) 2019

---
This app contains backend API for managing and using hotel reservation by both 
customer and hotel reservation administrator. The app is created using 
the Python programming language with the **Flask** web framework.

Base URL
---
This will now be referred to as ```<base-url>```
```
API Base URL = https://syncsoft-hotel-reserve-backend.herokuapp.com
```

Signing In
---
To sign in and get a json web token, pass in a basic authentication 
with parameters ```username``` and ```password``` wherein the username is
the registered email of the user.

(Note that at the moment, the sign in has no effect as the routes are not yet restricted to use the tokens.)

#### Sign-In URL
```
https://syncsoft-hotel-reserve-backend.herokuapp.com/login
```

Show All Rooms
---
Using the ```<base-url>``` this should be ```https://syncsoft-hotel-reserve-backend.herokuapp.com/rooms```
```python
<base-url>/rooms
```
This will query and list all rooms in json format like:
```json
[
  - {
        available: true,
        id: 1,
        price: 1000,
        room_number: "101",
        type: "Deluxe"
      },
  - {
        available: false,
        id: 2,
        price: 1000,
        room_number: "102",
        type: "Deluxe"
    },
...
]
```

Book a Room
---
Here, book_id is required for booking a room.
```python
<base-url>/book?room_id=1
```
After executing this request, the database will be updated and the column ```available``` of the ```room``` table will 
be set to false. Giving an id that is not in the database will generate and error and the resulting json has a 
property called ```success``` which will be equal to ```false```. Otherwise, ```true```.

Checkout from Room
---
To checkout a room and make it available for booking,
```python
<base-url>/checout?room_id=1
```
This will undo the action done by booking a room.

View Room Details
---
To view all room details:
```python
<base-url>/room/1
```
Here, 1 is the room_id and must be specified. Neglecting it results to an error which will also be displayed.