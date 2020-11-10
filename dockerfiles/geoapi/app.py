from flask import Flask, make_response
import redis

import os

app = Flask(__name__)

_redis_host = os.getenv('REDIS_HOST')
_redis_port = os.getenv('REDIS_PORT')

r = redis.Redis(host=_redis_host, port=_redis_port, db=0)


@app.route('/api/<dataset>')
def api(dataset):
    data = r.get(dataset)
    #data = "hello " + dataset
    response = make_response(data, 200)
    response.mimetype = "text/plain"
    return response


if __name__ == '__main__':
    app.run()
