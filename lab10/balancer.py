#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import json
import requests

app = Flask(__name__)

HOSTS = ['http://localhost:8080/storage/','http://localhost:8081/storage/']
def host(key):
    return HOSTS[len(key) % 2]


@app.route('/<key>', methods=['GET'])
def get_value(key):
    response = requests.get(host(key) + key)
    return response.content, response.status_code


if __name__ == '__main__':
    app.run(port=8082)

