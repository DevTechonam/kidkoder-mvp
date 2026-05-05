# animations.py
#- FloatingStar  : animated floating star label used on the welcome screen
#- FadeOverlay   : brief dark flash that plays when switching topics

import math
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, pyqtProperty
from PyQt5.QtGui import QFont



# ── FloatingStar 

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

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(55)            
        self.show()

    def _tick(self):
        self._angle = (self._angle + 3) % 360
        new_y = self._base_y + int(7 * math.sin(math.radians(self._angle)))
        self.move(self.x(), new_y)


# ── FadeOverlay 

class FadeOverlay(QWidget):

    def __init__(self, parent):
        print("[FadeOverlay.__init__] Creating fade overlay")
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._opacity = 0.0
        self.hide()

    def _get_opacity(self):
        return self._opacity

    def _set_opacity(self, v):
        self._opacity = v
        self.setWindowOpacity(max(0.0, min(1.0, v)))

    val = pyqtProperty(float, _get_opacity, _set_opacity)

    def flash(self, sz):
        self.setGeometry(0, 0, sz.width(), sz.height())
        self.setStyleSheet("background: rgb(10,0,60);")
        self.setWindowOpacity(0.55)
        self.raise_()
        self.show()

        self._anim = QPropertyAnimation(self, b"windowOpacity")
        self._anim.setDuration(220)
        self._anim.setStartValue(0.55)
        self._anim.setEndValue(0.0)
        self._anim.setEasingCurve(QEasingCurve.OutCubic)
        self._anim.finished.connect(self.hide)
        self._anim.start()


