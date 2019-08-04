from app import app


@app.route('/')
def home():
    return 'Welcome to SyncSoft Solutions\' Hotel Reservation Backend System.'
