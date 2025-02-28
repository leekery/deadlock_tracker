from PyQt5 import QtWidgets, QtCore, QtGui
from PIL import Image
import numpy as np
from PyQt5.QtCore import pyqtSignal

class RegionSelector(QtWidgets.QDialog):
    region_selected = pyqtSignal(tuple)
    def __init__(self, image_path=None):
        super().__init__()
        self.image_path = image_path
        if self.image_path:
            self.pixmap = QtGui.QPixmap(self.image_path)
        else:
            screen = QtWidgets.QApplication.primaryScreen()
            self.pixmap = screen.grabWindow(0)
            self.setWindowTitle('Выбор области')
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(self.pixmap.size())
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.rect = None
        self.is_selecting = False
        self.region = None

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.is_selecting = True
        self.update()

    def mouseMoveEvent(self, event):
        if self.is_selecting:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        self.is_selecting = False
        self.rect = QtCore.QRect(self.begin, self.end).normalized()
        self.region = (self.rect.left(), self.rect.top(), self.rect.width(), self.rect.height())
        self.region_selected.emit(self.region)
        self.accept()
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)
        if self.is_selecting:
            rect = QtCore.QRect(self.begin, self.end)
            painter.setPen(QtGui.QPen(QtGui.QColor(0, 255, 0), 2))
            painter.setBrush(QtGui.QColor(0, 255, 0, 50))
            painter.drawRect(rect)
            
    def reject(self):
        self.region_selected.emit(None)
        super().reject()

def select_area():
    selector = RegionSelector()
    if selector.exec_() == QtWidgets.QDialog.Accepted:
        return selector.region
    else:
        print("Область не была выбрана.")
        return None

def capture_area(region):
    x, y, width, height = region
    screen = QtWidgets.QApplication.primaryScreen()
    screenshot = screen.grabWindow(0, x, y, width, height)
    image = screenshot.toImage().convertToFormat(QtGui.QImage.Format.Format_RGB32)
    width = image.width()
    height = image.height()
    ptr = image.bits()
    ptr.setsize(image.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)
    img = Image.fromarray(arr[:, :, :3], 'RGB')
    return img
