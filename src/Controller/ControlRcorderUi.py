import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
import datetime
from src.View.ScreenRecorder_ui import MainWindowUI
from src.Model.ScreenRecorder import ScreenRecorder

class MainWindowUI(MainWindowUI):
    def __init__(self,filePath = None, fileName=None):
        super().__init__()
        self.fileName = fileName
        self.filePath = filePath

        self.init_recording_ui()
        self.start_recording()

    def init_recording_ui(self):
        self.start_time = datetime.datetime.now()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.toggle_rcrd_bttn.clicked.connect(self.toggle_recording)
        self.stop_button.clicked.connect(self.close_win)
        self.is_recording = False

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.resume_recording()
        else:
            self.is_recording = False
            self.pause_recording()

    def start_recording(self):
        self.Rec = ScreenRecorder(self.filePath,self.fileName)
        self.Rec.start_recording()
        self.timer.start(1000)
        self.toggle_recording()

    def resume_recording(self):
        self.Rec.resume_recording()
        self.timer.start(1000)
        self.changeIcon(':/icons/Icons/pause-button.png')

    def pause_recording(self): 
        self.Rec.pause_recording()
        self.timer.stop()
        self.changeIcon(':/icons/Icons/play-button.png')

    def changeIcon(self, icon_name):
        start_icon = QIcon(icon_name)
        self.toggle_rcrd_bttn.setIcon(start_icon)

    def close_win(self):
        self.Rec.stop_recording()
        self.timer.stop() 
        self.close()

    def update_timer(self):
        elapsed_time = datetime.datetime.now() - self.start_time
        time_str = str(elapsed_time).split('.')[0]  # Format elapsed time as HH:MM:SS
        self.label.setText(time_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowUI()
    window.show()
    sys.exit(app.exec_())
