import sys
from PyQt5.QtWidgets import QApplication
from Dashboard_pannel import GamePanel


if __name__ == "__main__": 
    print("Application started...")
    app = QApplication(sys.argv)
    win = GamePanel()
    win.showMaximized()
    sys.exit(app.exec_())

