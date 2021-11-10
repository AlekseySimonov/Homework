import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QMessageBox
from PyQt5.QtMultimedia import QMediaObject, QMediaPlayer, QMediaContent, QVideoSurfaceFormat
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.MainMenu()
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

    def MainMenu(self):

        self.setGeometry(300, 300, 300, 220)
        self.resize(850, 550)
        self.move(250, 100)
        self.setWindowTitle('Simple window')

        menu = self.menuBar()

        fileMenu = menu.addMenu('&File')
        editMenu = menu.addMenu('&Edit')
        helpMenu = menu.addMenu('&Help')

        fileMenu.addAction('Open', self.ActionClick)
        fileMenu.addAction('Exit', self.ActionClick)


    def ActionClick(self):

        action = self.sender()
        if action.text() == 'Open':
            try:
                findFile = QFileDialog.getOpenFileName(self)[0]
                if findFile != '':
                    self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(findFile))) # Считывание видео
                else:
                    return
            except:
                return

        elif action.text() == 'Exit':
            reply = QMessageBox.question(self, 'Exit', "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                sys.exit()
            else:
                return


# Запуск программы
def application():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())

application()
