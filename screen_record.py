import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt,QPoint
import threading
import time
from PyQt5.QtGui import  QIcon
import cv2
import pyautogui
import numpy as np 
import os 

class ScreenRecorder:
    def __init__(self,filename=None,filePath=None):
        self.is_recording = False
        self.fileName = filename
        self.filePath = filePath
        
        
    def start_recording(self):
        self.is_recording = True
        threading.Thread(target=self._record).start()

    def stop_recording(self):
        self.is_recording = False

    def _record(self):
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
        if self.fileName is None : 
            file_path = './screen_record.avi'
        else:
            if self.filePath is not None : 
                file_path = os.path.join(self.filePath,self.fileName)
            else:
                file_path = self.fileName
                
        out = cv2.VideoWriter(file_path, fourcc, 20.0, (1920, 1080))
        
        while self.is_recording:
            # Capture the screen
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)

            # Convert RGB to BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Write the frame to the video file
            out.write(frame)

        # Release the VideoWriter object
        out.release()
        
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Screen Recorder')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Remove title bar and stay on top
        self.setGeometry(800, 500, 100, 50)
        self.setStyleSheet("""
        background-color: rgba(1, 0, 0, 100);
        color: white;
        
  
    """)
        self.label = QLabel('00:00:00')
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.start_button = QPushButton()
        self.start_button.clicked.connect(self.start_recording)

        self.stop_button = QPushButton()
        self.stop_button.clicked.connect(self.close_win)
        # self.stop_button.setEnabled(False)

        layout = QHBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)
    
        self.screen_recorder = ScreenRecorder()
        self.seconds_elapsed = 0
        self.dragging = False
        self.offset = QPoint()
        
        
        # ------ setting icon to the buttons --------
        start_icon = QIcon('Icons/pauseIcon.png')  # Replace 'start_icon.png' with your icon file path
        self.start_button.setIcon(start_icon)
        
        stop_icon = QIcon('Icons/startIcon.png')  # Replace 'stop_icon.png' with your icon file path
        self.stop_button.setIcon(stop_icon)
        
        self.is_timer_active = False 
        
        

        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
    
    def start_recording(self):
        if not self.is_timer_active:
            self.is_timer_active = True 
            self.changeIcon('Icons/playIcon.png')   
            self.init_recording()         
        else : 
            self.is_timer_active = False
            self.stop_recording()
            self.changeIcon('Icons/pauseIcon.png')

    def changeIcon(self,icon_name):
        start_icon = QIcon(icon_name)  # Replace 'start_icon.png' with your icon file path
        self.start_button.setIcon(start_icon)
        
    def init_recording(self):
        self.seconds_elapsed = 0
        self.update_timer_display()
        self.timer.start(1000)
        self.screen_recorder.start_recording()
        
    def stop_recording(self):
        # self.start_button.setEnabled(True)
        # self.stop_button.setEnabled(False)
        self.timer.stop()
        self.screen_recorder.stop_recording()
        
    def close_win(self):
        self.stop_recording()
        self.close()
        
    def update_timer(self):
        self.seconds_elapsed += 1
        self.update_timer_display()

    def update_timer_display(self):
        hours = self.seconds_elapsed // 3600
        minutes = (self.seconds_elapsed % 3600) // 60
        seconds = self.seconds_elapsed % 60
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.label.setText(time_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
