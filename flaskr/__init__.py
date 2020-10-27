"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

import flaskr.views
