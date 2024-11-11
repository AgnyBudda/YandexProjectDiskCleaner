import sys
from functions import *
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class DiskCleaner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'forms\mainform.ui', self)  # Загружаем дизайн
        self.ScanButton.clicked.connect(self.update_drives)

    def update_drives(self):
        try:
            self.ScanList.clear()
            self.ScanList.addItems(scan_disks())
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DiskCleaner()
    ex.show()
    sys.exit(app.exec())