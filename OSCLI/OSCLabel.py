from PyQt6 import QtWidgets, QtCore, QtGui
from pythonosc import udp_client, dispatcher, osc_server
import threading # for multithreaded handling of messages
import Config
import sys 
class OSCLabel(QtWidgets.QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self._defaults = Config.loadConfig()
        self._receivePort = self._defaults['receive_port']
        self._receiveIP = self._defaults['receive_ip']
        self.setText("")
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/eos/out/cmd", self.outputHandler)

        self.server = osc_server.ThreadingOSCUDPServer((self._receiveIP, 3032), self.dispatcher)
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
    
    def outputHandler(self, address, *args):
        self.setText(args[0])