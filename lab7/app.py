#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(port=8081) # по умолчанию Flask запускается на порту 5000
    # app.run(host='0.0.0.0') # а для докера возможно, вам надо будет использовать 0.0.0.0 вместо 127.0.0.1
