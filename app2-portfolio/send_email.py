import smtplib
import ssl
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'peychev.vn@gmail.com'
    password = os.getenv('PASSWORD')


    receiver = 'peychev.vn@gmail.com'
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        server.set_debuglevel(1)



# server = smtplib.SMTP_SSL(host)
# server.login(username, password)
# server.sendmail(username, receiver, message)