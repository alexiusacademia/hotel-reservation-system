from app import app, mail, Message


@app.route('/send_mail')
def send_mail():
    msg = Message(subject='Test Subject',
                  recipients=['alexius.academia@gmail.com'],
                  body='This is a test message 2',
                  sender='syncsoftsolutions.software@gmail.com')
    mail.send(msg)
    return 'Email sent!'
