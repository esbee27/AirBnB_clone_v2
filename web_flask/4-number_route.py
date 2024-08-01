#!/usr/bin/python3

"""a script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Return a string"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns a string with variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Returns a string with variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Displays n if n is a number"""
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
