import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

class AudioPlayer(QWidget):
    # инициализация плеера
    def __init__(self):

        # создание окна
        super().__init__()
        self.resize(300, 300)
        place = self.frameGeometry()
        centre = QDesktopWidget().availableGeometry().center()
        place.moveCenter(centre)
        self.move(place.topLeft())
        self.setWindowTitle("Audio Player")

        # вызов класса QMediaPlayer
        self.player = QMediaPlayer()

        # отображение положения объектов
        self.layout = QVBoxLayout()
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        # время продолжительности
        self.time = QHBoxLayout()
        self.TimeLabel = QLabel('00:00')
        self.name = QLabel('')
        self.time.addWidget(self.TimeLabel)
        self.time.addWidget(self.name)
        self.layout.addLayout(self.time)

        # слайдер
        self.sldPosition = QSlider(Qt.Horizontal)
        self.sldPosition.setMinimum(0)
        self.sldPosition.sliderMoved[int].connect(self.position)
        self.layout.addWidget(self.sldPosition)
        self.sldPosition.setEnabled(False)

        # соединение позиции времени проигрывания с используемыми объектами
        self.player.positionChanged.connect(self.sldPosition.setValue)
        self.player.durationChanged.connect(self.duration)
        self.player.durationChanged.connect(self.durationTime)

        # создание кнопки play
        self.btnplay = QPushButton(" ▶️", clicked=self.play)
        self.layout.addWidget(self.btnplay)
        self.btnplay.setFixedSize(40, 40)
        self.btnplay.setEnabled(False)

        # создание кноки pause
        self.btnpause = QPushButton("||", clicked=self.pause)
        self.layout.addWidget(self.btnpause)
        self.btnpause.setFixedSize(40, 40)
        self.btnpause.setEnabled(False)

        # создание кнопок увеличения и уменьшения громкости
        volumeControl = QHBoxLayout()
        self.layout.addLayout(volumeControl)
        btnVolumeUp = QPushButton('+', clicked=self.volumeUp)
        btnVolumeDown = QPushButton('-', clicked=self.volumeDown)
        butVolumeMute = QPushButton('Mute', clicked=self.volumeMute)
        volumeControl.addWidget(btnVolumeUp)
        volumeControl.addWidget(butVolumeMute)
        volumeControl.addWidget(btnVolumeDown)

        # создание кнопки открытия файла(open)
        findAudio = QHBoxLayout()
        self.layout.addLayout(findAudio)
        btnOpenFile = QPushButton('Open', clicked=self.OpenAudioFile)
        findAudio.addWidget(btnOpenFile)
        # отображение какой-либо ошибки
        self.player.error.connect(self._errorHandle)

    def position(self, value):
         self.player.setPosition(value)

    def durationTime(self, t):
        time = str(int(str(t)[:3]) // 60) + ':' + str(int(str(t)[:3]) - (int(str(t)[:3]) // 60) * 60)
        self.TimeLabel.setText(time)

    def duration(self, n):
        self.sldPosition.setRange(0, n)

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
            self.name.setText(str(findFile[0]).split('/')[-1])
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(findFile[0])))
            self.player.play()
            self.btnpause.setEnabled(True)
            self.sldPosition.setEnabled(True)
        else:
            return

    def _errorHandle(self, error):
        print('ERROR', error, self.player.errorString())
# запуск плеера
if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = AudioPlayer()
    App.show()
    sys.exit(app.exec_())
