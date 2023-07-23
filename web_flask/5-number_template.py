#!/usr/bin/python3
"""minimal flask web application"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """ returns welcome msg"""
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns new msg"""
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """display “C ” followed by text input"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """displays word Python followed by text input"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def isanumber(n):
    """displays statement only if integer input received"""
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    # Change the host parameter from '127.0.0.1' to '0.0.0.0'
    app.run(host='0.0.0.0', port=5000)