from PyQt6 import QtWidgets, QtCore, QtGui

import sys

class DraggableWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint
        )

        self.setFixedSize(760,50)
        self.setStyleSheet("background-color: black; color: white;")

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Quit Button (For now)
        self.quitButton = QtWidgets.QPushButton("Quit", self)
        self.quitButton.setGeometry(0, 0, self.width(), self.height())
        self.quitButton.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border: none;
                padding: 0px;
                margin: 0px;
                font-family: monospace;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: green;
            }
        """)

        self.quitButton.clicked.connect(QtWidgets.QApplication.quit)
        self.quitButton.setMinimumHeight(self.height())
        self.quitButton.setMaximumHeight(self.height())
        layout.addWidget(self.quitButton)

        # Settings Button
        self.settingsButton = QtWidgets.QPushButton(self)
        self.settingsButton.setIcon(QtGui.QIcon("gear.png"))
        self.settingsButton.setIconSize(QtCore.QSize(18, 18))
        self.settingsButton.setFixedSize(30, 30)
        self.settingsButton.setStyleSheet("""
            QPushButton {
                background-color: red;
                border: none;
            }
            QPushButton:hover {
                background-color: #333;
                border-radius: 4px;
            }
        """)
        layout.addWidget(self.settingsButton)
        layout.setAlignment(self.settingsButton, QtCore.Qt.AlignmentFlag.AlignLeft)





        self.setLayout(layout)

        self._offset = None  # to store click offset

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            clicked_child = self.childAt(event.position().toPoint())
            if clicked_child is not self.settingsButton:
                self._offset = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self._offset is not None and event.buttons() & QtCore.Qt.MouseButton.LeftButton:
            delta = event.position().toPoint() - self._offset
            self.move(self.pos() + delta)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DraggableWindow()
    window.show()
    sys.exit(app.exec())