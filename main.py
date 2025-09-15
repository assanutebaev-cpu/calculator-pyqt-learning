#main.py

import sys
from PyQt6.QtWidgets import QApplication
from ui.ui import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()