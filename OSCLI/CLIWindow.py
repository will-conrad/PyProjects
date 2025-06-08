from PyQt6 import QtWidgets, QtCore, QtGui
from OSCLabel import OSCLabel
from OSCLabel import OSCLabel
import sys

class CLIWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        w = 800
        h = 50
        pad = 5
        
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint
        )
        
        self.setStyleSheet("background-color: black;")
        self.setFixedSize(w, h)

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        frameLayout = QtWidgets.QHBoxLayout(centralWidget)
        frameLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        frameLayout.setContentsMargins(0,0,0,0)
       
        self.frame = QtWidgets.QFrame()
        self.frame.setFixedSize(w - 2 * pad, h - 2 * pad)
        self.frame.setStyleSheet("""
            QFrame {
                border: 2px solid #D28800;
                background-color: transparent;
            }
        """)
        frameLayout.addWidget(self.frame)



        overlayWidget = QtWidgets.QWidget(centralWidget)
        overlayWidget.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        overlayWidget.setStyleSheet("background-color: transparent;")
        overlayWidget.setGeometry(self.rect())

        overlayLayout = QtWidgets.QHBoxLayout(overlayWidget)

        self.label = OSCLabel()
        self.label.setMinimumWidth(300)

        self.label.setStyleSheet("padding: 0px; margin: 0px; color: #FFDA8B; font-family: Hack; font-size: 20pt")
        
        overlayLayout.addWidget(self.label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        overlayLayout.addStretch()


        overlayWidget.setLayout(overlayLayout)

        self._offset = None  # to store click offset

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            # clicked_child = self.childAt(event.position().toPoint())
            self._offset = event.position().toPoint()
    
    def mouseMoveEvent(self, event):
        if self._offset is not None and event.buttons() & QtCore.Qt.MouseButton.LeftButton:
            delta = event.position().toPoint() - self._offset
            self.move(self.pos() + delta)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CLIWindow()
    window.show()
    sys.exit(app.exec())