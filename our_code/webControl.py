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
    count = 0
    @cherrypy.expose
    def index(self):
        return control_text.format("")

    @cherrypy.expose
    def up(self):
        #command = "python2 -c 'import control_shades; control_shades.move_up()'"
        command = "python2 -c 'import control_shades; control_shades.move_up(40)'"
        Shades.count = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        return "Current state:" + str(Shades.count)

    @cherrypy.expose
    def down(self):
        #command = "python2 -c 'import control_shades; control_shades.move_down()'"
        command = "python2 -c 'import control_shades; control_shades.move_down(40)'"
        Shades.count = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        return "Current state:" + str(Shades.count)

if __name__=='__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8181})
    cherrypy.quickstart(Shades())
