#ui.py
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QLayout

from logic.logic import handle_input


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('calcu')
        self.resize(400, 300)
        #imports
        layout = QVBoxLayout()
        #seeting
        self.input_f = QLineEdit()
        self.button = QPushButton('=')

        #
        layout.addWidget(self.input_f)
        layout.addWidget(self.button)
        self.setLayout(layout)

        #Connecting

        def current_text():
            text = self.input_f.text()
            handle_input(text)

        self.button.clicked.connect(current_text)