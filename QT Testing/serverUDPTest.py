from PyQt6 import QtWidgets, QtCore
from pythonosc import udp_client, osc_server, osc_tcp_server, dispatcher
import threading

def printer(data, *args):
    print(f"{data}: {args}")

def default_handler(data, *args):
    print(f"DEFAULT {data}: {args}")


class ServerTest():
    def __init__(self):
        super().__init__()

        ip = "127.0.0.1"
        port = 1337

        self.client = udp_client.SimpleUDPClient(ip, port)
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.set_default_handler(default_handler)



        self.server = osc_server.ThreadingOSCUDPServer(("0.0.0.0", port), self.dispatcher)

        server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        server_thread.start()

if __name__ == "__main__":
    import time
    server_test = ServerTest()
    while True:
        time.sleep(1)
