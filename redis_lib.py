# As I understand, pythonic imported values are bound to the module
# making them kinda singletons.  r is thus a single re-used connection
# within server.py

import redis
import time
import json
r = redis.Redis( host='redis', port=6379, db=0)

def getKeys():
    return r.keys('*')

def getValue(key):
    return r.hgetall(key);

def log(path,ip):
    r.hset(
        'path:'+path,
        ip+'|'+str(int(time.time())),
        json.dumps({'ip':ip,'timestamp':int(time.time())})
    )
