import smtplib, email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import choice


def server_login(login, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
        # If we can encrypt this session, do it
    if server.has_extn('STARTTLS'):
        server.starttls()
        server.ehlo() # re-identify ourselves over TLS connection
        server.login(login, password)
    return server


def send_email(server, receiver_email):
    notifier = "kittyemailer@gmail.com" 
    kitties = [['101020.2.jpg'], ['101656.2.jpg'], ['101900.2.jpg'], ['103349.2.jpg'], ['105841.2.jpg'], ['106122.1.jpg'], ['109978.2.jpg'], ['110417.2.jpg'], ['110904.2.jpg'], ['111058.2.jpg'], ['117911.2.jpg'], ['11832.jpg'], ['120354.2.jpg'],$
    message = MIMEMultipart("alternative")
    message["Subject"] = "Here's a kitty to brighten your day :)"
    message["From"] = notifier
    message["To"] = receiver_email

    text = """\
    You need HTML to see kitties :("""
    html = f"""\
    <html>
    <body>
        <p>Hi,<br>
        Tired of all the COVID-19 emails you've been getting?
        Here's a kitty to brighten your day :)        </p>
        <img src="http://www.randomkittengenerator.com/cats/{choice(kitties)[0]}">
    </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    server.send_message(
        message,
        notifier,
        receiver_email
    )
    server.quit()

