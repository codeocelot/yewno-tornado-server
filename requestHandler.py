from tornado.web import RequestHandler
import redis_lib

class RequestHandler(RequestHandler):
  def prepare(self):
    ip = self.request.remote_ip
    path = self.request.path
    redis_lib.log(path,ip)
