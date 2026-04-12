# ── Topic Button 

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


class TopicButton(QPushButton):
    def __init__(self, topic, idx, cb, pal):
        super().__init__()
        self._on       = pal["btn_on"]
        self._off      = pal["btn_off"]
        self._hov      = pal["hover"]
        self._revealed = False
        self._cb       = cb
        self._idx      = idx

        self._inner = QStackedWidget(self)
        self._inner.setStyleSheet("background:transparent;")

        # Locked face
        locked_w = QWidget()
        locked_w.setStyleSheet("background:transparent;")
        lv = QVBoxLayout(locked_w)
        lv.setContentsMargins(4, 6, 4, 6)
        lv.setSpacing(2)
        lv.setAlignment(Qt.AlignCenter)
        lock_icon = QLabel("🔒")
        lock_icon.setFont(QFont("Segoe UI Emoji", 20))
        lock_icon.setAlignment(Qt.AlignCenter)
        lock_icon.setStyleSheet("background:transparent; border:none; color:#FFFFFF;")
        lv.addWidget(lock_icon)
        lock_hint = QLabel("???")
        lock_hint.setFont(QFont("Arial", 8, QFont.Bold))
        lock_hint.setAlignment(Qt.AlignCenter)
        lock_hint.setStyleSheet("background:transparent; border:none; color:#DDCCFF;")
        lv.addWidget(lock_hint)

        # Revealed face
        revealed_w = QWidget()
        revealed_w.setStyleSheet("background:transparent;")
        rv = QVBoxLayout(revealed_w)
        rv.setContentsMargins(4, 6, 4, 6)
        rv.setSpacing(2)
        rv.setAlignment(Qt.AlignCenter)
        for txt, fnt in [
            (topic["emoji"], QFont("Segoe UI Emoji", 21)),
            (topic["name"],  QFont("Arial", 8, QFont.Bold)),
        ]:
            lbl = QLabel(txt)
            lbl.setFont(fnt)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setWordWrap(True)
            lbl.setStyleSheet("background:transparent; border:none; color:#FFFFFF;")
            rv.addWidget(lbl)

        self._inner.addWidget(locked_w)
        self._inner.addWidget(revealed_w)

        il = QVBoxLayout(self)
        il.setContentsMargins(0, 0, 0, 0)
        il.addWidget(self._inner)

        self.setFixedHeight(78)
        self.setCursor(Qt.PointingHandCursor)
        self._set_style(False)
        self.clicked.connect(self._on_click)

        self._ba = QPropertyAnimation(self, b"pos")
        self._ba.setDuration(220)
        self._ba.setEasingCurve(QEasingCurve.OutBounce)

    def _on_click(self):
        if not self._revealed:
            self._revealed = True
            self._inner.setCurrentIndex(1)
        self._cb(self._idx)

    def _set_style(self, active):
        if active:
            self.setStyleSheet(f"""
                QPushButton {{ background: {self._on}; border-radius: 12px; border: 3px solid #FFFFFF; }}
                QPushButton:hover {{ background: {self._hov}; }}
            """)
        else:
            self.setStyleSheet(f"""
                QPushButton {{ background: {self._off}; border-radius: 12px; border: 2px solid rgba(255,255,255,0.25); }}
                QPushButton:hover {{ background: {self._hov}; border: 3px solid #FFFFFF; }}
            """)

    def set_active(self, v): self._set_style(v)

    def bounce(self):
        p = self.pos()
        self._ba.setStartValue(p)
        self._ba.setKeyValueAt(0.4, QPoint(p.x(), p.y() - 9))
        self._ba.setKeyValueAt(0.75, QPoint(p.x(), p.y() - 3))
        self._ba.setEndValue(p)
        self._ba.start()
