from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from config import Config
from .controllers.app_init import app_init

app_init()
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
socketio = SocketIO(app, cors_allowed_origins="*")


from app.routes import main_routes
from app import routes
