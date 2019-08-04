from app import app, jsonify
import sendgrid
import os
from sendgrid.helpers.mail import *


@app.route('/send_mail')
def send_mail():
    api_key = os.environ.get('SENDGRID_API_KEY')

    from_email = From('syncsoftsolutions.software@gmail.com')
    subject = Subject('Test Subject using Sendgrid')
    to_email = To('alexius.academia@gmail.com')
    content = Content('text/plain', 'Hello! This is a test mail using sendgrid.')
    mail = Mail(from_email,
                to_email,
                subject,
                content)

    try:
        sg = sendgrid.SendGridAPIClient(api_key=api_key)
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

    return jsonify({'message': 'Email has been sent!'})
