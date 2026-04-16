# welcome_page.py
# WelcomePage — the first screen the user sees with animated stars and a
# "Start Learning!" button that switches to the main topic view.

from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from constants import WELCOME_BG, STAGE
from content_page   import TOPICS

from animations import FloatingStar

print("[welcome_page] Loading WelcomePage...")


class WelcomePage(QWidget):
    """Splash / welcome screen shown on app launch."""

    def __init__(self, on_start):
        super().__init__()
        self.setStyleSheet(f"WelcomePage {{ background: {WELCOME_BG}; }}")

        v = QVBoxLayout(self)
        v.setAlignment(Qt.AlignCenter)
        v.setSpacing(16)

        # ── Title labels 
        for text, font, color in [
            ("🚀",
             QFont("Segoe UI Emoji", 68), "#FFE566"),
            ("Computer Basics",
             QFont("Arial", 34, QFont.Bold), "#FFFFFF"),
            ("for Kids!  🌟",
             QFont("Arial", 22, QFont.Bold), "#FFE566"),
            ("Learn about computers, coding and more!\nClick below to start your adventure!",
             QFont("Arial", 12), "#C5B8FF"),
        ]:
            lbl = QLabel(text)
            lbl.setFont(font)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet(f"color:{color}; background:transparent;")
            v.addWidget(lbl)

        # ── Topic emoji preview row (first 4 topics) ──────────────────────────
        row = QHBoxLayout()
        row.setAlignment(Qt.AlignCenter)
        row.setSpacing(12)
        for i, topic in enumerate(TOPICS[:4]):
            em = QLabel(topic["emoji"])
            em.setFont(QFont("Segoe UI Emoji", 26))
            em.setFixedSize(56, 56)
            em.setAlignment(Qt.AlignCenter)
            em.setStyleSheet(
                f"background:{STAGE[i]['btn_on']}; border-radius:14px; border:3px solid #FFFFFF;"
            )
            row.addWidget(em)
        v.addLayout(row)

        # ── Start button ──────────────────────────────────────────────────────
        btn = QPushButton("  🚀  Start Learning!  ")
        btn.setFont(QFont("Arial", 15, QFont.Bold))
        btn.setFixedSize(270, 52)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background: #5533CC; border-radius: 26px;
                color: #FFFFFF; border: 3px solid #AA99FF;
            }
            QPushButton:hover { background: #7755FF; border: 3px solid #FFFFFF; color: #FFE566; }
            QPushButton:pressed { padding-top: 3px; }
        """)
        btn.clicked.connect(self._on_start_clicked)
        self._on_start_cb = on_start
        v.addSpacing(6)
        v.addWidget(btn, alignment=Qt.AlignCenter)

        # ── Floating stars ────────────────────────────────────────────────────
        for x, y, sz, col in [
            (40,  70, 16, "#FFE566"),
            (680, 55, 13, "#FF94C2"),
            (70, 390, 11, "#A5FFB0"),
            (700,360, 15, "#FFD180"),
            (380, 22, 13, "#CE93D8"),
            (185,275, 10, "#80D8FF"),
            (560,230, 17, "#FF94C2"),
            (120,460, 11, "#84FFFF"),
        ]:
            FloatingStar(self, x, y, sz, col)

        print("[WelcomePage.__init__] Done.")

    def _on_start_clicked(self):
        self._on_start_cb()


