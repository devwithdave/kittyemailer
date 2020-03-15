
import cherrypy
from emailer import send_email, server_login
import os

class Emailkitties(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
          <p>
          Enter your email if you're tired of COVID-19 emails in your inbox.
          <p>
            <form method="get" action="confirmation">
              <input type="text" value="Enter Your Email" name="email" />
              <button type="submit">Click For Kitties!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def confirmation(self, email):
        password = os.environ.get('GMAIL')
        send_email(server_login('kittyemailer@gmail.com',password), email)
        return f"Kitties are on their way to {email}!"


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })
    cherrypy.quickstart(Emailkitties())
