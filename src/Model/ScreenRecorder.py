
import cv2
import os
import platform
import pyautogui
import numpy as np
import threading
import datetime 

class ScreenRecorder:
    def __init__(self,fileName = None, filePath=None):
        self.is_recording = False
        self.is_paused = False
        self.fileName = fileName
        self.filePath = filePath

    def start_recording(self):
        self.is_recording = True
        self.RecTh = threading.Thread(target=self._record)
        self.RecTh.start()

    def stop_recording(self):
        self.is_recording = False

    def pause_recording(self):
        self.is_paused = True

    def resume_recording(self):
        self.is_paused = False

    def _record(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.get_output_file_path(), fourcc, 20.0, (1920, 1080))

        while self.is_recording:
            if not self.is_paused:
                screenshot = pyautogui.screenshot()
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                out.write(frame)

        out.release()

    def get_output_file_path(self):
        if self.fileName is None : 
            current_datetime = datetime.datetime.now()
            self.fileName = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") + ".avi"
            
        if platform.system() == 'Linux':
            default_folder = os.path.join(os.path.expanduser('~'), 'Videos')
        else:
            default_folder = os.path.join(os.environ.get('USERPROFILE'), 'Videos')

        if self.filePath is None : 
            self.filePath = default_folder

        return os.path.join(self.filePath, self.fileName)

