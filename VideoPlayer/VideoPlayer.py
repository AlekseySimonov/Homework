import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu


# Класс главного окна
class Window(QMainWindow):

    # Главное меню
    def MainMenu(self):
        menu = self.menu()
        fileMenu = QMenu('&File', self)
        menu.addMenu(fileMenu)

        editMenu = menu.addMenu('&Edit')
        helpMenu = menu.addMenu('&Help')
        

    # Создание главного окна
    def __init__(self):

        super(Window, self).__init__()

        # Настройки главного окна
        self.setGeometry(300, 300, 300, 220)
        self.resize(850, 550)
        self.move(250, 100)
        self.setWindowTitle('Simple window')



# Запуск программы
def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())


application()