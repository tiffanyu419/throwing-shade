import cherrypy
import subprocess
control_text = """
<html><body>
<form method="get" action="up">
<button type="submit">up</button>
</form>
<form method="get" action="down">
<button type="submit">down</button>
</form></body>
</html>
"""

class Shades(object):
    @cherrypy.expose
    def index(self):
        return control_text.format("")

    @cherrypy.expose
    def up(self):
        command = "python2 -c 'import control_shades; control_shades.move_up()'"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        return

    @cherrypy.expose
    def down(self):
        command = "python2 -c 'import control_shades; control_shades.move_down()'"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        return

if __name__=='__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8181})
    cherrypy.quickstart(Shades())
