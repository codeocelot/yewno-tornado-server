import json
from tornado.web import Application
from requestHandler import RequestHandler
from tornado.ioloop import IOLoop
from redis_lib import getValue,log,getKeys

class HelloWorldHandler(RequestHandler):
    def get(self):
        self.write({'message':'hello world'})

class AllLogsHandler(RequestHandler):
    def get(self):
        keys = getKeys()
        logs = [{'endpoint':k[6:],'logs':getValue(k)} for k in keys]
        # ohhh how I missed list comprehensions.
        self.write({'logset':logs,'keys':keys})

class SingleLogHandler(RequestHandler):
    def get(self):
        self.write({'logs':getValue('path:'+self.request.path)})

def make_app():
    return Application(
        [   (r"/v1/hello-world",HelloWorldHandler),
            (r"/v1/logs",AllLogsHandler),
            (r"/.*/logs",SingleLogHandler)  ]
        , debug=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(3000)
    IOLoop.current().start()
