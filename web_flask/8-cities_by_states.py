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

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays n if n is a number"""
    n = str(n)
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """display a HTML page only if n is an integer"""
    n = str(n)
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """display a HTML page only if n is an int"""
    n = str(n)
    return render_template('6-number_odd_or_even.html', n=n)

@app.route('/states_list', strict_slashes=False)
def state_list():
    """display a HTML page: (inside the tag BODY)"""
    return render_template('7-states_list.html', states=storage.all('State'))

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a html page of city objects"""
    return render_template('8-cities_by_state.html', states=storage.all("State"))

@app.teardown_appcontext
def teardown(err):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
