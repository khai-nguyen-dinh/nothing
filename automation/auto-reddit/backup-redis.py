import redis

r = redis.StrictRedis(host='192.241.145.184', port=6379, db=0, password='Admin@0607', decode_responses=True)
with open('redis-data.txt', 'a') as f:
    for key in r.scan_iter("user:*"):
        f.write(key + '|' + r.get(key) + '\n')
