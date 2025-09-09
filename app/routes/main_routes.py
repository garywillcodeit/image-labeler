from app import app, socketio
from ..controllers.load_init_data import load_init_data
from .home_route import home_route
from .images_routes import images_bp
from .labels_routes import labels_bp
from .export_route import export_bp
from ..controllers.database.get_training_data_ctrl import get_training_data_ctrl


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


@app.route("/", methods=["GET"])
def home():
    return home_route()


@app.route("/get-init-data", methods=["GET"])
def init_data():
    return load_init_data()


@app.route("/get-training-data", methods=["GET"])
def get_training_data():
    return get_training_data_ctrl()


app.register_blueprint(images_bp, url_prefix="/images")
app.register_blueprint(labels_bp, url_prefix="/labels")
app.register_blueprint(export_bp, url_prefix="/export")
