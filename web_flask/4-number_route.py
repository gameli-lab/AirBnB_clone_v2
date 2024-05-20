#!/usr/bin/python3
"""
This is a falsk hello module
"""

from flask import Flask, request
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
