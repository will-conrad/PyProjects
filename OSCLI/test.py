from PyQt6 import QtWidgets, QtCore, QtGui
import sys

class EOSBar(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: black;
                border: 2px solid orange;
            }
            QLabel {
                color: orange;
                font-family: Consolas, monospace;
                font-size: 16px;
            }
            QPushButton {
                background-color: black;
                border: none;
            }
        """)
        self.setFixedHeight(40)
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Status label
        self.statusLabel = QtWidgets.QLabel("LIVE: Cue 1 :  Chan 1 @ Full")
        layout.addWidget(self.statusLabel, stretch=1)

        # Search/magnifier button
        self.searchButton = QtWidgets.QPushButton()
        search_icon = QtGui.QIcon.fromTheme("edit-find")  # or load your own .png/.svg
        self.searchButton.setIcon(search_icon)
        self.searchButton.setIconSize(QtCore.QSize(20, 20))
        layout.addWidget(self.searchButton)

        self.setLayout(layout)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EOS Bar UI")
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        main_layout = QtWidgets.QVBoxLayout(central)
        eos_bar = EOSBar()
        main_layout.addWidget(eos_bar)
        main_layout.addStretch()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())