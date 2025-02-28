import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from image_utils import select_area, capture_area, RegionSelector
from ocr import recognize_text
from overlay import OverlayWindow
from config.settings import CHECK_INTERVAL

class AppLogic:
    def __init__(self):
        self.area1 = None
        self.area2 = None
        self.circle_area = None
        self.overlay = OverlayWindow()
        self.timer = None
        self.selector = None

    def select_first_area(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите изображение", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.selector = RegionSelector(file_path)
            self.selector.region_selected.connect(self.on_first_area_selected)
            self.selector.exec_()
        else:
            print("Изображение не выбрано.")

    def on_first_area_selected(self, region):
        if region:
            self.area1 = region
            print("Первая область выбрана:", region)
        else:
            print("Первая область не была выбрана.")
        self.selector = None

    def select_second_area(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите изображение", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.selector = RegionSelector(file_path)
            self.selector.region_selected.connect(self.on_second_area_selected)
            self.selector.exec_()
        else:
            print("Изображение не выбрано.")

    def on_second_area_selected(self, region):
        if region:
            self.area2 = region
            print("Вторая область выбрана:", region)
        else:
            print("Вторая область не была выбрана.")
        self.selector = None

    def select_circle_area(self):
        self.selector = RegionSelector()
        self.selector.region_selected.connect(self.on_circle_area_selected)
        self.selector.exec_()

    def on_circle_area_selected(self, region):
        if region:
            self.circle_area = region
            print("Область для кружка выбрана:", region)
        else:
            print("Область для кружка не была выбрана.")
        self.selector = None

    def start_program(self):
        if None in (self.area1, self.area2, self.circle_area):
            print("Пожалуйста, выберите все области перед запуском.")
            return
        self.timer = QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(CHECK_INTERVAL * 1000)

    def run(self):
        num1 = self.get_number_from_area(self.area1)
        num2 = self.get_number_from_area(self.area2)
        if num1 is not None and num2 is not None and num2 != 0:
            percent_diff = ((num1 - num2) / num2) * 100
            if percent_diff >= 10:
                self.overlay.show_overlay(self.circle_area)
            else:
                self.overlay.hide_overlay()

    def get_number_from_area(self, area):
        img = capture_area(area)
        text = recognize_text(img)
        try:
            return float(text)
        except ValueError:
            return None
