import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QIcon
# import icons_rc


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

        start_icon = QIcon(':/icons/Icons/pause-button.png')
        self.toggle_rcrd_bttn.setIcon(start_icon)
        stop_icon = QIcon(':/icons/Icons/stop-button.png')
        self.stop_button.setIcon(stop_icon)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_ui = MainWindowUI()
    window_ui.show()
    sys.exit(app.exec_())
