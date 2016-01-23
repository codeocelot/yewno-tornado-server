# import tornado.ioloop
# import tornado.web
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

import redis
import json

import redis_lib
# keys = redis_lib.keys()
# print keys

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

class HelloWorldHandler(RequestHandler):
    def get(self):
        self.write('hiiiii')

class LogsHandler(RequestHandler):
    def get(self):
        # response = { 'id': 23, 'load':'nothing'}
        # r = redis.StrictRedis(host='localhost', port=6379, db=0)
        #
        # keys = r.keys('*')
        # print keys
        #
        # response = r.hgetall('path:/v1/logs')
        # logs = [json.loads(x) for x in response.values()]
        #
        # print logs

        keys = redis_lib.keys()
        logs = [json.loads(redis_lib.getHash(k)) for k in keys]
        print logs

        self.write({'logset':logs})

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
