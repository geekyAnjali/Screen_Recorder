import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QIcon, QMouseEvent
import src.icons_rc


class MainWindowUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Screen Recorder')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800, 500, 100, 50)
        self.setStyleSheet("""
        background-color: rgba(1, 0, 0, 100);
        color: white;
    """)

        self.label = QLabel('00:00:00')
    

        self.toggle_rcrd_bttn = QPushButton()
        

        self.stop_button = QPushButton()
        

        layout = QHBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.toggle_rcrd_bttn)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

        start_icon = QIcon(':/icons/Icons/play-button.png')
        self.toggle_rcrd_bttn.setIcon(start_icon)
        stop_icon = QIcon(':/icons/Icons/stop-button.png')
        self.stop_button.setIcon(stop_icon)
        self.stop_button.setCursor(Qt.PointingHandCursor)
        self.toggle_rcrd_bttn.setCursor(Qt.PointingHandCursor)

        self.stop_button.setToolTip("Stop Recording")
        self.toggle_rcrd_bttn.setToolTip("Pause/Resume Recording")

        self.stop_button.setStyleSheet("QToolTip { color: black; }")
        self.toggle_rcrd_bttn.setStyleSheet("QToolTip { color:black;}")
  


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            self.draggable = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.draggable = False
            self.offset = None
            self.setCursor(Qt.ArrowCursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_ui = MainWindowUI()
    window_ui.show()
    sys.exit(app.exec_())
