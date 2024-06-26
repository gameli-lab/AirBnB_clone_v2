#!/usr/bin/python3
"""
This is a falsk hello module
"""

from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    spaces = text.replace('_', ' ')
    return f'C {escape(spaces)}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    space = text.replace('_', ' ')
    return f'Python {escape(space)}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n}'


@app.route('/number_template/', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html')


@app.route('/number_odd_or_even/', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    is_even = n % 2 == 0
    return render_template('6-number_odd_or_even.html', n=n, is_even=is_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
