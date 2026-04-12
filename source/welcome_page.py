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


from constants import WELCOME_BG, STAGE, SIDEBAR_BG
from topics_content import TOPICS
from animations import FloatingStar
# ── Welcome Page 

class WelcomePage(QWidget):
    def __init__(self, on_start):
        super().__init__()
        self.setStyleSheet(f"WelcomePage {{ background: {WELCOME_BG}; }}")
        v = QVBoxLayout(self)
        v.setAlignment(Qt.AlignCenter)
        v.setSpacing(16)

        for txt, fnt, col in [
            ("🚀",                  QFont("Segoe UI Emoji", 68), "#FFE566"),
            ("Computer Basics",     QFont("Arial", 34, QFont.Bold), "#FFFFFF"),
            ("for Kids!  🌟",       QFont("Arial", 22, QFont.Bold), "#FFE566"),
            ("Learn about computers, coding and more!\n"
             "Click below to start your adventure!",
             QFont("Arial", 12), "#C5B8FF"),
        ]:
            lbl = QLabel(txt)
            lbl.setFont(fnt)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet(f"color:{col}; background:transparent;")
            v.addWidget(lbl)

        row = QHBoxLayout()
        row.setAlignment(Qt.AlignCenter)
        row.setSpacing(12)
        for i, t in enumerate(TOPICS[:4]):
            em = QLabel(t["emoji"])
            em.setFont(QFont("Segoe UI Emoji", 26))
            em.setFixedSize(56, 56)
            em.setAlignment(Qt.AlignCenter)
            em.setStyleSheet(
                f"background:{STAGE[i]['btn_on']}; border-radius:14px; border:3px solid #FFFFFF;"
            )
            row.addWidget(em)
        v.addLayout(row)

        btn = QPushButton("  🚀  Start Learning!  ")
        btn.setFont(QFont("Arial", 15, QFont.Bold))
        btn.setFixedSize(270, 52)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton { background: #5533CC; border-radius: 26px; color: #FFFFFF; border: 3px solid #AA99FF; }
            QPushButton:hover { background: #7755FF; border: 3px solid #FFFFFF; color: #FFE566; }
            QPushButton:pressed { padding-top: 3px; }
        """)
        btn.clicked.connect(on_start)
        v.addSpacing(6)
        v.addWidget(btn, alignment=Qt.AlignCenter)

        for x, y, sz, col in [
            (40,  70, 16, "#FFE566"), (680,  55, 13, "#FF94C2"),
            (70, 390, 11, "#A5FFB0"), (700, 360, 15, "#FFD180"),
            (380,  22, 13, "#CE93D8"), (185, 275, 10, "#80D8FF"),
            (560, 230, 17, "#FF94C2"), (120, 460, 11, "#84FFFF"),
        ]:
            FloatingStar(self, x, y, sz, col)
