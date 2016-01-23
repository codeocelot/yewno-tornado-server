import json
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from redis_lib import getValue,log,getKeys

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

class HelloWorldHandler(RequestHandler):
    def get(self):
        path = self.request.path
        ip = self.request.remote_ip
        log(path,ip)
        self.write(path+ip)

class LogsHandler(RequestHandler):
    def get(self):
        keys = getKeys()
        logs = [{k[6:]:getValue(k)} for k in keys]
        # ohhh how I missed list comprehensions.
        self.write({'logset':logs,'keys':keys})

def make_app():
    return Application([
    (r"/", MainHandler),
    (r"/hello-world",HelloWorldHandler),
    (r"/v1/logs",LogsHandler)
    ],debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(3000)
    IOLoop.current().start()
