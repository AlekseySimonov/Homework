import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class AudioPlayer(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(400, 300)

        place = self.frameGeometry()
        centre = QDesktopWidget().availableGeometry().center()
        place.moveCenter(centre)
        self.move(place.topLeft())

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.btnplay = QPushButton(" ▶️", clicked=self.play)
        self.layout.addWidget(self.btnplay)
        self.btnplay.setFixedSize(40, 40)
        self.btnplay.setEnabled(False)


        self.btnpause = QPushButton("||", clicked=self.pause)
        self.layout.addWidget(self.btnpause)
        self.btnpause.setFixedSize(40, 40)
        self.btnpause.setEnabled(False)


        volumeControl = QHBoxLayout()
        self.layout.addLayout(volumeControl)

        btnVolumeUp = QPushButton('+', clicked=self.volumeUp)
        btnVolumeDown = QPushButton('-', clicked=self.volumeDown)
        butVolumeMute = QPushButton('Mute', clicked=self.volumeMute)
        volumeControl.addWidget(btnVolumeUp)
        volumeControl.addWidget(butVolumeMute)
        volumeControl.addWidget(btnVolumeDown)

        findAudio = QHBoxLayout()
        self.layout.addLayout(findAudio)

        btnOpenFile = QPushButton('Open', clicked=self.OpenAudioFile)
        findAudio.addWidget(btnOpenFile)

        self.videowidget = QVideoWidget()
        self.player = QMediaPlayer()


        self.player.error.connect(self._errorHandle)


    def pause(self):
        try:
            self.player.pause()
            self.btnplay.setEnabled(True)
            self.btnpause.setEnabled(False)
        except:
            return

    def play(self):
        try:
            self.player.play()
            self.btnpause.setEnabled(True)
            self.btnplay.setEnabled(False)
        except:
            return

    def volumeUp(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def OpenAudioFile(self):

        findFile = QFileDialog.getOpenFileName(self)

        if findFile != '':
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(findFile[0])))
            self.player.play()
            self.btnpause.setEnabled(True)

        else:
            return

    def _errorHandle(self, error):
        print('ERROR', error, self.player.errorString())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    App = AudioPlayer()
    App.show()
    sys.exit(app.exec_())



