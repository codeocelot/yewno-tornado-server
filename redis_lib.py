import redis
r = redis.StrictRedis(host='redis', port=6379, db=0)
# r = redis.Redis( host='redis', port=6379, db=0)
# r.set('foo', 'bar')
# print r.get('foo')

def keys():
    return r.keys('*')

def getHash(key):
    return r.hgetall(key);

def getEndpoint(endpoint):
    logs = r.hgetall('path:/'+endpoint)
    print logs
    return logs

def log():
    pass
    print 'hi'
