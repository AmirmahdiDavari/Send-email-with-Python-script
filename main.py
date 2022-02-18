import smtplib
from email.message import EmailMessage

# Script send email whit python
try:
    msg = EmailMessage()
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT_SSL = 465
    EMAIL_HOST_USER = 'your email address'
    EMAIL_HOST_PASSWORD = 'Your email password or your  smtp email key'

    msg['Subject'] = 'send_message(msg)'
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = 'The email address you want to send'
    msg.set_content("The text of your email")

    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully")

except:
    print("There is a problem. Email was not sent")
