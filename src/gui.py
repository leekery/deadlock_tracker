from PyQt5 import QtWidgets
from app_logic import AppLogic

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.logic = AppLogic()
        self.init_ui()

    def init_ui(self):
        btn1 = QtWidgets.QPushButton('Открыть изображение и выбрать первую область', self)
        btn2 = QtWidgets.QPushButton('Выбрать вторую область', self)
        btn3 = QtWidgets.QPushButton('Запуск программы', self)
        btn4 = QtWidgets.QPushButton('Выделить область для кружка', self)

        btn1.clicked.connect(self.logic.select_first_area)
        btn2.clicked.connect(self.logic.select_second_area)
        btn3.clicked.connect(self.logic.start_program)
        btn4.clicked.connect(self.logic.select_circle_area)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn4)
        vbox.addWidget(btn3)
        self.setLayout(vbox)

        self.setWindowTitle('Сравнение чисел')
        self.show()
