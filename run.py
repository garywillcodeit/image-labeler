from app import app, socketio
from config import Config
import webbrowser
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    url = "http://127.0.0.1:" + str(Config.PORT)
    if Config.DEBUG == False:
        webbrowser.open(url)
    socketio.run(app, port=Config.PORT)
