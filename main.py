import sys
from PyQt5.QtWidgets import QApplication
from src.Controller.ControlRcorderUi import MainWindowUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Check if a file path is provided as a command-line argument
    filePath = None
    fileName = None
    if len(sys.argv) > 1:
        filePath = sys.argv[1]  # The first command-line argument after the script name
        fileName = sys.argv[2]
        
    window = MainWindowUI(filePath=filePath, fileName=fileName)
    window.show()
    sys.exit(app.exec_())

