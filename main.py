import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from logic.logic import ButtonHandler
from ui.ui import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Настройка интерфейса
        self.setFixedSize(self.size())
        self.logic = ButtonHandler(self.ui)


    def keyPressEvent(self, event):
        self.logic.handle_key_event(event)
        super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())

