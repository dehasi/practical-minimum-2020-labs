#!/usr/bin/env python3

import json
import os

import pymongo
import redis
from flask import Flask
from flask import json
from flask import request

from lec10.solution.ntier.repository import MongoRepository
from lec10.solution.ntier.repository import RedisRepository
from lec10.solution.ntier.service import Service

app = Flask(__name__)
logfile = open("/var/log/server.log", "w")
def log(message):
    logfile.write(message + '\n')
    logfile.flush()


service = None

### Contoller VVVV
@app.route('/storage/<key>', methods=['GET'])
def get_value(key):
    log(f'GET {key}')
    res = service.get(key)
    if res is None:
        return '', 404
    return json.loads(res)


@app.route('/storage/<key>', methods=['PUT'])
def add_value(key):
    log(f'PUT {key}')
    if not request.is_json:
        return '', 400
    content = request.get_json()
    service.put(key, json.dumps(content))
    return '', 201


@app.route('/storage/<key>', methods=['DELETE'])
def delete_value(key):
    log(f'DELETE {key}')
    service.delete(key)
    return '', 204


if __name__ == '__main__':
    #### init
    redis_host = os.getenv('REDIS_HOST')
    redis_port = int(os.getenv('REDIS_PORT'))
    redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
    cache = RedisRepository(redis_client)

    mongo_host = os.getenv('MONGO_HOST')
    mongo_port = int(os.getenv('MONGO_PORT'))
    mongo_client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
    mongo_table = mongo_client['hw9']['storage']
    database = MongoRepository(mongo_table)
    Service(cache, database)

    app.run(host='0.0.0.0', port=8080)
