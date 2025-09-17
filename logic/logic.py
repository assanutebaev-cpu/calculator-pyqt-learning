# logic.py
# button_logic.py

from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QLineEdit

class ButtonHandler(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.connect_signals()
        self.editor = QLineEdit()
    def connect_signals(self):
        self.ui.minus_button.clicked.connect(self.on_button_click)
        self.ui.seven_button.clicked.connect(self.on_button_click)
        self.ui.divide_button.clicked.connect(self.on_button_click)
        self.ui.nine_button.clicked.connect(self.on_button_click)
        self.ui.multiply_button.clicked.connect(self.on_button_click)
        self.ui.clear_button.clicked.connect(self.clear)
        self.ui.four_button.clicked.connect(self.on_button_click)
        self.ui.zero_button.clicked.connect(self.on_button_click)
        self.ui.eighth_button.clicked.connect(self.on_button_click)
        self.ui.two_button.clicked.connect(self.on_button_click)
        self.ui.plus_button.clicked.connect(self.on_button_click)
        self.ui.five_button.clicked.connect(self.on_button_click)
        self.ui.three_button.clicked.connect(self.on_button_click)
        self.ui.percent_button.clicked.connect(self.on_button_click)
        self.ui.equal_button.clicked.connect(self.equal)
        self.ui.six_button.clicked.connect(self.on_button_click)
        self.ui.one_button.clicked.connect(self.on_button_click)


    def on_button_click(self):
        sender = self.sender()
        current_text = self.ui.lineEdit.text()
        text = current_text + str(sender.objectName())
        self.ui.lineEdit.setText(text)

    def clear(self):
        self.ui.lineEdit.setText('')

    def equal(self):
        result = eval(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(str(result))
