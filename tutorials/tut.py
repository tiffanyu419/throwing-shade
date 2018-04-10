import random
import string

import cherrypy


class StringGenerator(object):
    count = 0
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session[StringGenerator.count] = some_string
        StringGenerator.count += 1
        return some_string

    @cherrypy.expose
    def display(self):
        for i in range(StringGenerator.count):
            return cherrypy.session[i]



if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8181})
    cherrypy.quickstart(StringGenerator(), '/', conf)
