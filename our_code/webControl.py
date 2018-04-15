import os, os.path
import cherrypy
import subprocess

class Shades(object):
    current = 0
    max = 80
    @cherrypy.expose
    def index(self):
        return open('index.html')

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
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './Desktop/throwing-shade/our_code/css'
        }
    }
    cherrypy.quickstart(Shades(), '/', conf)
