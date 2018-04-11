import os, os.path
import cherrypy
import subprocess

control_text = """
<html>
<head>
<link href="/static/style.css" rel="stylesheet">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<html>
</head>
<body>
<form method="get" class="btn btn-default" action="allUp">
<button type="submit"><span class="glyphicon glyphicon-triangle-top" aria-hidden="true"></span></button>
</form>
<form method="get" class="btn btn-default" action="up">
<button type="submit"><span class="glyphicon glyphicon-menu-up" aria-hidden="true"></button>
</form>
<form method="get" class="btn btn-default" action="down">
<button type="submit"><span class="glyphicon glyphicon-menu-down" aria-hidden="true"></button>
</form>
<form method="get" class="btn btn-default" action="allDown">
<button type="submit"><span class="glyphicon glyphicon-triangle-bottom" aria-hidden="true"></button>
</form>
</body>
</html>
"""

class Shades(object):
    current = 0
    max = 80
    @cherrypy.expose
    def index(self):
        return control_text.format("")

    @cherrypy.expose
    def up(self):
        command = "python2 -c 'import control_shades; control_shades.move_up(" +str(Shades.current)+")'"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        ls = result.split()
        Shades.current = int(ls[4])
        return str(Shades.current)

    @cherrypy.expose
    def down(self):
        var = [str(Shades.current), str(Shades.max)]
        command = "python2 -c 'import control_shades; control_shades.move_down("+", ".join(var)+")'"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        ls = result.split()
        Shades.current = int(ls[4])
        return str(Shades.current)

    @cherrypy.expose
    def allDown(self):
        var = [str(Shades.current), str(Shades.max)]
        command = "python2 -c 'import control_shades; control_shades.allDown("+", ".join(var)+")'"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        Shades.current = Shades.max
        return str(Shades.current)

    @cherrypy.expose
    def allUp(self):
        var = [str(Shades.current), "0"]
        command = "python2 -c 'import control_shades; control_shades.allUp("+", ".join(var)+")'"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        Shades.current = 0
        return str(Shades.current)

if __name__=='__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8181})
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()) + 'Desktop/throwing-shade/our_code'
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './Desktop/throwing-shade/our_code'
        }
    }
    cherrypy.quickstart(Shades(), '/', conf)
