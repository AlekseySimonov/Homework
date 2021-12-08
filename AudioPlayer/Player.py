import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist


class AudioPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = 800
        self.window_height = 120

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        btn = QPushButton('Play', clicked=self.playAudioFile)
        self.layout.addWidget(btn)

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

        btnOpenFile = QPushButton('Open', clicked=self.playAudioFile)
        findAudio.addWidget(btnOpenFile)

        self.player = QMediaPlayer()

        self.player.error.connect(self._errorHandle)

    def volumeUp(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def playAudioFile(self):

        findFile = QFileDialog.getOpenFileName(self)

        if findFile != '':
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(findFile[0])))
            self.player.play()


        else:
            return

    def _errorHandle(selfsself,error):
        print('ERROR',error)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    App = AudioPlayer()
    App.show()
    sys.exit(app.exec_())


