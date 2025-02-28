from PyQt5 import QtWidgets, QtGui, QtCore

class OverlayWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.region = None
        self.hide()

    def show_overlay(self, region):
        self.region = region
        x, y, width, height = region
        self.setGeometry(x, y, width, height)
        self.show()

    def hide_overlay(self):
        self.hide()

    def paintEvent(self, event):
        if self.region:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setBrush(QtGui.QColor(0, 255, 0, 150))
            painter.setPen(QtCore.Qt.NoPen)
            painter.drawEllipse(self.rect())