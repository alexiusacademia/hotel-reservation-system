# Hotel Reservation System (Back End)
### SyncSoft Solutions (c) 2019

---
This app contains backend API for managing and using hotel reservation by both 
customer and hotel reservation administrator. The app is created using 
the Python programming language with the **Flask** web framework.

Base URL
---
```
API Base URL = https://syncsoft-hotel-reserve-backend.herokuapp.com
```

Signing In
---
To sign in and get a json web token, pass in a basic authentication 
with parameters ```username``` and ```password``` wherein the username is
the registered email of the user.

#### Sign-In URL
```
https://syncsoft-hotel-reserve-backend.herokuapp.com/login
```