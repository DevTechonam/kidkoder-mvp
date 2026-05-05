# topics_button.py
# TopicButton — a sidebar button that starts locked  and
# reveals the topic emoji + name on first click, then stays revealed.

from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QFont



class TopicButton(QPushButton):

    def __init__(self, topic, idx, callback, pal):
        super().__init__()
        self._color_on  = pal["btn_on"]
        self._color_off = pal["btn_off"]
        self._color_hov = pal["hover"]
        self._revealed  = False
        self._callback  = callback
        self._idx       = idx

        # ── Inner stacked widget (locked ↔ revealed) 
        self._inner = QStackedWidget(self)
        self._inner.setStyleSheet("background:transparent;")

        # Page 0 — locked
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

        # Page 1 — revealed
        revealed_w = QWidget()
        revealed_w.setStyleSheet("background:transparent;")
        rv = QVBoxLayout(revealed_w)
        rv.setContentsMargins(4, 6, 4, 6)
        rv.setSpacing(2)
        rv.setAlignment(Qt.AlignCenter)

        for text, font in [
            (topic["emoji"], QFont("Segoe UI Emoji", 21)),
            (topic["name"],  QFont("Arial", 8, QFont.Bold)),
        ]:
            lbl = QLabel(text)
            lbl.setFont(font)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setWordWrap(True)
            lbl.setStyleSheet("background:transparent; border:none; color:#FFFFFF;")
            rv.addWidget(lbl)

        self._inner.addWidget(locked_w)    # index 0
        self._inner.addWidget(revealed_w)  # index 1

        il = QVBoxLayout(self)
        il.setContentsMargins(0, 0, 0, 0)
        il.addWidget(self._inner)

        self.setFixedHeight(78)
        self.setCursor(Qt.PointingHandCursor)
        self._apply_style(active=False)
        self.clicked.connect(self._on_click)

        # Bounce animation
        self._bounce_anim = QPropertyAnimation(self, b"pos")
        self._bounce_anim.setDuration(220)
        self._bounce_anim.setEasingCurve(QEasingCurve.OutBounce)

    # ── Slots 

    def _on_click(self):
        if not self._revealed:
            self._revealed = True
            self._inner.setCurrentIndex(1)   # flip to revealed face
        self._callback(self._idx)

    # ── Style helpers 

    def _apply_style(self, active: bool):
        if active:
            self.setStyleSheet(f"""
                QPushButton {{ background: {self._color_on}; border-radius: 12px; border: 3px solid #FFFFFF; }}
                QPushButton:hover {{ background: {self._color_hov}; }}
            """)
        else:
            self.setStyleSheet(f"""
                QPushButton {{ background: {self._color_off}; border-radius: 12px; border: 2px solid rgba(255,255,255,0.25); }}
                QPushButton:hover {{ background: {self._color_hov}; border: 3px solid #FFFFFF; }}
            """)

    def set_active(self, active: bool):
        self._apply_style(active)

    def bounce(self):
        p = self.pos()
        self._bounce_anim.setStartValue(p)
        self._bounce_anim.setKeyValueAt(0.4,  QPoint(p.x(), p.y() - 9))
        self._bounce_anim.setKeyValueAt(0.75, QPoint(p.x(), p.y() - 3))
        self._bounce_anim.setEndValue(p)
        self._bounce_anim.start()


