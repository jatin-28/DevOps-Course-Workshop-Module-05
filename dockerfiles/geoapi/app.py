from flask import Flask
import redis

import os

app = Flask(__name__)

_redis_host = os.getenv('REDIS_HOST')
_redis_port = os.getenv('REDIS_PORT')

r = redis.Redis(host=_redis_host, port=_redis_port, db=0)


@app.route('/api/<dataset>')
def api(dataset):
    return r.get(dataset)


if __name__ == '__main__':
    app.run()
