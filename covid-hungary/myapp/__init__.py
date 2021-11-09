from flask import Flask
from .views import pages

# Objects
app = Flask(__name__)

# Blueprints
app.register_blueprint(pages)