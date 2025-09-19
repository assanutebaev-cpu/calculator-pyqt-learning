from PyQt6.QtCore import Qt, QObject, QTimer
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
        self.ui.erase_button.clicked.connect(self.erase)
        self.ui.equal_button.clicked.connect(self.equal)
        self.ui.six_button.clicked.connect(self.on_button_click)
        self.ui.one_button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        sender = self.sender()
        current_text = self.ui.lineEdit.text()
        text = current_text + str(sender.objectName())
        self.ui.lineEdit.setText(text)

    def erase(self):
        current_text = self.ui.lineEdit.text()
        text = current_text[:-1]
        self.ui.lineEdit.setText(text)

    def clear(self):
        self.ui.lineEdit.setText('')


    # def equal(self):
    #     try:
    #         result = eval(self.ui.lineEdit.text())
    #         self.ui.lineEdit.setText(str(result))
    #     except Exception:
    #         self.ui.lineEdit.setText(str("Ошибка"))
    #

    def equal(self):
        try:
            result = eval(self.ui.lineEdit.text())
            if len(str(result)) < 14 :
                self.ui.lineEdit.setText(str(result))
            else:
                self.ui.lineEdit.setText('A lot')
        except Exception:
            self.ui.lineEdit.setText(str("Ошибка"))

    def handle_key_event(self, event):


        if event.key() == Qt.Key.Key_1 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.one_button.click()
        if event.key() == Qt.Key.Key_2 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.two_button.click()
        if event.key() == Qt.Key.Key_3 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.three_button.click()
        if event.key() == Qt.Key.Key_4 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.four_button.click()
        if event.key() == Qt.Key.Key_5 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.five_button.click()
        if event.key() == Qt.Key.Key_6 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.six_button.click()
        if event.key() == Qt.Key.Key_7 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.seven_button.click()
        if event.key() == Qt.Key.Key_8 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.eighth_button.click()
        if event.key() == Qt.Key.Key_9 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.nine_button.click()
        if event.key() == Qt.Key.Key_0 and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.zero_button.click()
        if event.key() == Qt.Key.Key_Plus and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.plus_button.click()
        if event.key() == Qt.Key.Key_Minus and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.minus_button.click()
        if event.key() == Qt.Key.Key_Enter:
            self.ui.equal_button.click()
        if event.key() == Qt.Key.Key_Equal:
            self.ui.equal_button.click()
        if event.key() == Qt.Key.Key_Slash and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.divide_button.click()
        if event.key() == Qt.Key.Key_Asterisk and event.modifiers() == Qt.KeyboardModifier.KeypadModifier:
            self.ui.multiply_button.click()
        if event.key() == Qt.Key.Key_Backspace:
            self.ui.erase_button.click()
        if event.key() == Qt.Key.Key_C:
            self.ui.clear_button.click()
