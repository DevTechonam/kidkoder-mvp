import sys
import os
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QStackedWidget, QFrame,
    QGraphicsOpacityEffect, QProgressBar
)
from PyQt5.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QTimer,
    QPoint, pyqtProperty
)
from PyQt5.QtGui import QFont, QPixmap

# ── Floating Star 

class FloatingStar(QLabel):
    def __init__(self, parent, x, y, size, color):
        super().__init__("★", parent)
        self.setStyleSheet(f"color:{color}; background:transparent; border:none;")
        self.setFont(QFont("Arial", size))
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._base_y = y
        self._angle  = (x * 41) % 360
        self.move(x, y)
        self.raise_()
        self._t = QTimer(self)
        self._t.timeout.connect(self._tick)
        self._t.start(55)
        self.show()

    def _tick(self):
        self._angle = (self._angle + 3) % 360
        self.move(self.x(), self._base_y + int(7 * math.sin(math.radians(self._angle))))


# ── Fade Overlay 

class FadeOverlay(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._v = 0.0
        self.hide()

    def _get(self): return self._v
    def _set(self, v):
        self._v = v
        self.setWindowOpacity(max(0.0, min(1.0, v)))

    val = pyqtProperty(float, _get, _set)

    def flash(self, sz):
        self.setGeometry(0, 0, sz.width(), sz.height())
        self.setStyleSheet("background: rgb(10,0,60);")
        self.setWindowOpacity(0.55)
        self.raise_()
        self.show()
        self._a = QPropertyAnimation(self, b"windowOpacity")
        self._a.setDuration(220)
        self._a.setStartValue(0.55)
        self._a.setEndValue(0.0)
        self._a.setEasingCurve(QEasingCurve.OutCubic)
        self._a.finished.connect(self.hide)
        self._a.start()
