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
    logs = r.hgetall(key);
    # return logs
    d = []
    for k,v in r.hgetall(key).iteritems():
        j = json.loads(v)
        d.append({'ip':j['ip'],'timestamp':j['timestamp']})
    return d

def log(path,ip):
    r.hset(
        'path:'+path,
        ip+'|'+str(int(time.time())),
        json.dumps({'ip':ip,'timestamp':int(round(time.time()*1000))})
    )
