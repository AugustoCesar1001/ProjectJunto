import sys
sys.path.append('/home/ag/Área de Trabalho/Project Junto/')
from flask import Flask, jsonify


app = Flask(__name__)
app.config.from_object('config')

from .routes import routes
