from app import app, mail, Message
import sendgrid
import os
from sendgrid.helpers.mail import *


@app.route('/send_mail')
def send_mail():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email('syncsoftsolutions.software@gmail.com')
    subject = 'Test Subject using Sendgrid'
    to_email = Email('alexius.academia@gmail.com')
    content = Content('text/plain', 'Hello! This is a test mail using sendgrid.')
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    '''
    msg = Message(subject='Test Subject',
                  recipients=['alexius.academia@gmail.com'],
                  body='This is a test message 2',
                  sender='syncsoftsolutions.software@gmail.com')
    mail.send(msg)
    '''
    return 'Email sent!'
