from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QSize

class standar_buttons(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        # 🧬 Общие характеристики
        self.setFont(QFont("Google Sans", 14, weight=QFont.Weight.Medium))
        self.setFixedSize(QSize(64, 64))  # или динамически
        self.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.60); /* лёгкая прозрачность */\n"
"    border-radius: 24px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.4);\n"
"    color: #3c4043;\n"
"    font-family: \"Google Sans\", Roboto, Arial, sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    padding: 6px 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(246, 249, 254, 0.3);\n"
"    color: #174ea6;\n"
"    border: 1px solid rgba(23, 78, 166, 0.5);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(224, 224, 224, 0.4);\n"
"    border: 1px solid rgba(60, 64, 67, 0.5);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 2px solid #4285f4;\n"
"    outline: none;\n"
"}\n"
"")
