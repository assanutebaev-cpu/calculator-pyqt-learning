#ui.py
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QGridLayout
from logic.logic import handle_input
from widgets.button_class import standar_buttons

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('calcu')
        self.resize(400, 520)
        #imports
        layout = QGridLayout()
        #seeting
        self.input_f = QLineEdit()

        self.btn0 = standar_buttons('0')
        self.btn1 = standar_buttons('1')
        self.btn2 = standar_buttons('2')
        self.btn3 = standar_buttons('3')
        self.btn4 = standar_buttons('4')
        self.btn5 = standar_buttons('5')
        self.btn6 = standar_buttons('6')
        self.btn7 = standar_buttons('7')
        self.btn8 = standar_buttons('8')
        self.btn9 = standar_buttons('9')
        #
        layout.addWidget(self.input_f)
        layout.addWidget(self.btn0)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)
        layout.addWidget(self.btn6)
        layout.addWidget(self.btn7)
        layout.addWidget(self.btn8)
        layout.addWidget(self.btn9)
        self.setLayout(layout)

        #Connecting

        def current_text():
            text = self.input_f.text()
            handle_input(text)

