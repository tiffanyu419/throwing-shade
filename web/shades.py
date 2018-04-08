import cherrypy
import subprocess
text = """
<html><body>
<form method="get" action="up">
<button type="submit">up</button>
</form></body>
</html>
"""

class Shades(object):
    @cherrypy.expose
    def index(self):
        return text.format("")
    
    @cherrypy.expose
    def up(self):
        command = "python2 -c 'import control_shades; control_shades.move_shades('up',0,50)'"
        
        return ''.join(random.sample(string.hexdigits, int(length)))
    
if __name__=='__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8181})
    cherrypy.quickstart(StringGenerator())