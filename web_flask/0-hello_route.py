#!/usr/bin/python3
"""minimal flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ returns welcome msg"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    # Change the host parameter from '127.0.0.1' to '0.0.0.0'
    app.run(host='0.0.0.0', port=5000)
