from redis import Redis
from rq import Queue

from module import count_worlds_at_url

from config import Config

redis_conn = Redis(host=Config.redis_db.get("host"),
                   port=Config.redis_db.get("port"))

q = Queue(connection=redis_conn)

for row in range(100):

    job = q.enqueue(count_worlds_at_url, 'http://www.'+str(row)+'.com')
    print job.result



