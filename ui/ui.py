from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
path_to_background = BASE_DIR / "background.png"
path_str = path_to_background.as_posix()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 522)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.gridGroupBox.setGeometry(QtCore.QRect(10, 200, 371, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridGroupBox.sizePolicy().hasHeightForWidth())
        self.gridGroupBox.setSizePolicy(sizePolicy)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.minus_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)








        sizePolicy.setHeightForWidth(self.minus_button.sizePolicy().hasHeightForWidth())
        #BUTTON 7
        self.minus_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.minus_button.setFont(font)
        self.minus_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 102, 102, 0.60); /* лёгкая прозрачность */\n"
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
        self.minus_button.setObjectName("-")
        self.gridLayout_5.addWidget(self.minus_button, 0, 1, 1, 1)
        self.seven_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven_button.sizePolicy().hasHeightForWidth())
        self.seven_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.seven_button.setFont(font)
        self.seven_button.setStyleSheet("QPushButton {\n"
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
        self.seven_button.setObjectName("7")
        self.gridLayout_5.addWidget(self.seven_button, 2, 1, 1, 1)
        self.one_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one_button.sizePolicy().hasHeightForWidth())
        self.one_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.one_button.setFont(font)
        self.one_button.setStyleSheet("QPushButton {\n"
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
        self.one_button.setObjectName("1")
        self.gridLayout_5.addWidget(self.one_button, 4, 1, 1, 1)
        self.divide_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide_button.sizePolicy().hasHeightForWidth())
        self.divide_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.divide_button.setFont(font)
        self.divide_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,153, 0, 0.60); /* лёгкая прозрачность */\n"
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
        self.divide_button.setObjectName("/")
        self.gridLayout_5.addWidget(self.divide_button, 0, 3, 1, 1)
        self.six_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six_button.sizePolicy().hasHeightForWidth())
        self.six_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.six_button.setFont(font)
        self.six_button.setStyleSheet("QPushButton {\n"
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
        self.six_button.setObjectName("6")
        self.gridLayout_5.addWidget(self.six_button, 3, 3, 1, 1)
        self.nine_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine_button.sizePolicy().hasHeightForWidth())
        self.nine_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.nine_button.setFont(font)
        self.nine_button.setStyleSheet("QPushButton {\n"
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
        self.nine_button.setObjectName("9")
        self.gridLayout_5.addWidget(self.nine_button, 2, 3, 1, 1)
        self.multiply_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiply_button.sizePolicy().hasHeightForWidth())
        self.multiply_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(63)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.multiply_button.setFont(font)
        self.multiply_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 123, 231, 0.60); /* лёгкая прозрачность */\n"
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
        self.multiply_button.setObjectName("*")
        self.gridLayout_5.addWidget(self.multiply_button, 0, 4, 1, 1)
        self.clear_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet("QPushButton {\n"
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
        self.clear_button.setObjectName("C")
        self.gridLayout_5.addWidget(self.clear_button, 5, 3, 1, 1)
        self.four_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four_button.sizePolicy().hasHeightForWidth())
        self.four_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.four_button.setFont(font)
        self.four_button.setStyleSheet("QPushButton {\n"
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
        self.four_button.setObjectName("4")
        self.gridLayout_5.addWidget(self.four_button, 3, 1, 1, 1)
        self.zero_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        self.zero_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_button.sizePolicy().hasHeightForWidth())
        self.zero_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.zero_button.setFont(font)
        self.zero_button.setStyleSheet("QPushButton {\n"
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
        self.zero_button.setObjectName("0")
        self.gridLayout_5.addWidget(self.zero_button, 5, 1, 1, 2)
        self.eighth_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eighth_button.sizePolicy().hasHeightForWidth())
        self.eighth_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.eighth_button.setFont(font)
        self.eighth_button.setStyleSheet("QPushButton {\n"
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
        self.eighth_button.setObjectName("8")
        self.gridLayout_5.addWidget(self.eighth_button, 2, 2, 1, 1)
        self.two_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_button.sizePolicy().hasHeightForWidth())
        self.two_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.two_button.setFont(font)
        self.two_button.setStyleSheet("QPushButton {\n"
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
        self.two_button.setObjectName("2")
        self.gridLayout_5.addWidget(self.two_button, 4, 2, 1, 1)
        self.plus_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus_button.sizePolicy().hasHeightForWidth())
        self.plus_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.plus_button.setFont(font)
        self.plus_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(160, 255, 255, 0.60); /* лёгкая прозрачность */\n"
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
        self.plus_button.setObjectName("+")
        self.gridLayout_5.addWidget(self.plus_button, 0, 2, 1, 1)
        self.five_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five_button.sizePolicy().hasHeightForWidth())
        self.five_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.five_button.setFont(font)
        self.five_button.setStyleSheet("QPushButton {\n"
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
        self.five_button.setObjectName("5")
        self.gridLayout_5.addWidget(self.five_button, 3, 2, 1, 1)
        self.three_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three_button.sizePolicy().hasHeightForWidth())
        self.three_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.three_button.setFont(font)
        self.three_button.setStyleSheet("QPushButton {\n"
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
        self.three_button.setObjectName("3")
        self.gridLayout_5.addWidget(self.three_button, 4, 3, 1, 1)
        self.erase_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.erase_button.sizePolicy().hasHeightForWidth())
        self.erase_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setWeight(63)
        self.erase_button.setFont(font)
        self.erase_button.setStyleSheet("QPushButton {\n"
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
        self.erase_button.setObjectName("erase")
        self.gridLayout_5.addWidget(self.erase_button, 2, 4, 1, 1)
        self.equal_button = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal_button.sizePolicy().hasHeightForWidth())
        self.equal_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(63)
        self.equal_button.setFont(font)
        self.equal_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 160, 0.60); /* лёгкая прозрачность */\n"
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

        self.equal_button.setObjectName("=")
        self.gridLayout_5.addWidget(self.equal_button, 3, 4, 3, 1)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setEnabled(False)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 521))
        self.widget.setStyleSheet(f"""
            QWidget {{
                background-image: url({path_str});
                background-repeat: no-repeat;
                background-position: center;
                border-radius: 20px;
            }}
        """)

        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 371, 181))
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.4); /* Прозрачный белый фон */
                color: orange;                               /* Цвет текста */
                font-size: 30pt;                            /* Размер шрифта */
                font-family: 'Segoe UI';                    /* Шрифт (можно заменить на любимый) */
                font-weight: bold;                          /* Жирный текст */
                border: 2px solid rgba(255, 255, 255, 0.6);  /* Полупрозрачная рамка */
                border-radius: 6px;                         /* Скругление углов */
                padding: 5px;                               /* Отступ внутри */
                padding-top: 110px; 
            }
        """)
        self.lineEdit.setObjectName("KAKASHkA")
        self.widget.raise_()
        self.gridGroupBox.raise_()
        self.lineEdit.raise_()
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        MainWindow.setCentralWidget(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.multiply_button.setText(_translate("MainWindow", "*"))
        self.clear_button.setText(_translate("MainWindow", "С"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.eighth_button.setText(_translate("MainWindow", "8"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.erase_button.setText(_translate("MainWindow", "<-"))
        self.equal_button.setText(_translate("MainWindow", "="))

        self.one_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.two_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.three_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.four_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.five_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.six_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.seven_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.eighth_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.nine_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.clear_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.divide_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.plus_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.minus_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.multiply_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.clear_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.erase_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.equal_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gridGroupBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
