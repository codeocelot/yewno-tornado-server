from tornado.web import RequestHandler
import redis_lib

class RequestHandler(RequestHandler):
  def prepare(self):
    # Log all requests
    ip = self.request.remote_ip
    path = self.request.path
    redis_lib.log(path,ip)
    # Set ACAO
    self.set_header("Access-Control-Allow-Origin",'*')
