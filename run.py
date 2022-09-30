from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import ctypes

whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd)
        
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationDisplayName('Mine-imator 2.0') #窗口标题
    app.setWindowIcon(QIcon("./assets/1.png"))
    player = QMediaPlayer()
    wgt_video = QVideoWidget()  # 视频显示的widget
    wgt_video.show()
    player.setVideoOutput(wgt_video)  # 视频输出的widget
    player.setMedia(QMediaContent(QUrl.fromLocalFile(r'./assets/1.mp4')))  # 视频文件路径
    player.play()
    app.exec_()
