from app import app, socketio
from config import Config
import webbrowser
from dotenv import load_dotenv
import socket


def define_port(start_port):
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                print(port)
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                port += 1


if __name__ == "__main__":
    load_dotenv()
    port = define_port(Config.PORT)
    url = "http://127.0.0.1:" + str(port)
    if Config.DEBUG == False:
        webbrowser.open(url)
    socketio.run(app, port=port)
