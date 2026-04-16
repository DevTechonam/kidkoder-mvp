# app.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QStackedWidget,
    QGraphicsOpacityEffect, QProgressBar
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer
from PyQt5.QtGui import QFont

from constants      import STAGE, SIDEBAR_BG, BRAND_BG
from topics_content import *
from topics_button  import TopicButton
from animations     import FadeOverlay
from content_page   import TOPICS
from welcome_page   import WelcomePage


# Add more indices here as you add content, e.g. {0, 1, 2} for the first 3.
ACTIVE_TOPIC_INDICES: set = {0, 1}


# ── MainWindow 

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 Computer Basics for Kids!")
        self.setMinimumSize(980, 620)
        self.resize(1100, 680)

        self._cur     = -1          # currently active topic index 
        self._btns    = []          # list of TopicButton widgets
        self._visited = set()       # set of visited topic indices 
        self._pages   = {}          # cache: index → ContentPage/EmptyPage

        self._root    = QStackedWidget()
        self._welcome = WelcomePage(self._show_main)
        self._root.addWidget(self._welcome)

        self._main_w = QWidget()
        self._build_main()
        self._root.addWidget(self._main_w)

        rl = QVBoxLayout(self)
        rl.setContentsMargins(0, 0, 0, 0)
        rl.addWidget(self._root)

        
        self._eff = QGraphicsOpacityEffect(self._main_w)
        self._main_w.setGraphicsEffect(self._eff)
        self._eff.setOpacity(0.0)

        self._fadein = QPropertyAnimation(self._eff, b"opacity")
        self._fadein.setDuration(500)
        self._fadein.setEasingCurve(QEasingCurve.OutCubic)



    def _build_main(self):
        h = QHBoxLayout(self._main_w)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(0)

        h.addWidget(self._build_sidebar())
        h.addWidget(self._build_content_area(), 1)

    def _build_sidebar(self) -> QWidget:
        sb = QWidget()
        sb.setFixedWidth(196)
        sb.setStyleSheet(f"QWidget {{ background: {SIDEBAR_BG}; }}")
        sv = QVBoxLayout(sb)
        sv.setContentsMargins(8, 10, 8, 10)
        sv.setSpacing(5)

        # Brand label
        brand = QLabel("🚀  CS for Kids")
        brand.setFont(QFont("Arial", 11, QFont.Bold))
        brand.setAlignment(Qt.AlignCenter)
        brand.setFixedHeight(38)
        brand.setStyleSheet(
            f"color:#FFE566; background:{BRAND_BG}; "
            "border-radius:10px; border:2px solid #5533CC;"
        )
        sv.addWidget(brand)

        # Progress label + bar
        self._plbl = QLabel(f"Progress: 0 / {len(TOPICS)}")
        self._plbl.setFont(QFont("Arial", 8, QFont.Bold))
        self._plbl.setAlignment(Qt.AlignCenter)
        self._plbl.setStyleSheet("color:#C5B8FF; background:transparent;")

        self._pbar = QProgressBar()
        self._pbar.setMaximum(len(TOPICS))
        self._pbar.setValue(0)
        self._pbar.setTextVisible(False)
        self._pbar.setFixedHeight(6)
        self._pbar.setStyleSheet("""
            QProgressBar { background:#2A0080; border-radius:3px; border:none; }
            QProgressBar::chunk { background:#FFE566; border-radius:3px; }
        """)
        sv.addWidget(self._plbl)
        sv.addWidget(self._pbar)
        sv.addSpacing(5)

        # Topic buttons
        for i, topic in enumerate(TOPICS):
            btn = TopicButton(topic, i, self._switch, STAGE[i])
            sv.addWidget(btn)
            self._btns.append(btn)

        sv.addStretch()

        # Home button
        hbtn = QPushButton("🏠  Home")
        hbtn.setFont(QFont("Arial", 9, QFont.Bold))
        hbtn.setFixedHeight(34)
        hbtn.setCursor(Qt.PointingHandCursor)
        hbtn.setStyleSheet("""
            QPushButton { background:#2A0080; border:2px solid #5533CC; border-radius:9px; color:#C5B8FF; }
            QPushButton:hover { background:#5533CC; color:#FFFFFF; border:2px solid #FFFFFF; }
        """)
        hbtn.clicked.connect(self._go_home)
        sv.addWidget(hbtn)

        return sb

    def _build_content_area(self) -> QWidget:
        self._cc = QWidget()
        self._cc.setStyleSheet(f"background:{SIDEBAR_BG};")
        cl = QVBoxLayout(self._cc)
        cl.setContentsMargins(0, 0, 0, 0)

        self._stack = QStackedWidget()
        self._stack.setStyleSheet("background:transparent;")

        # Placeholder shown before any topic is selected
        placeholder = QWidget()
        placeholder.setStyleSheet(f"background:{SIDEBAR_BG};")
        ph_lay = QVBoxLayout(placeholder)
        ph_lay.setAlignment(Qt.AlignCenter)
        ph_lbl = QLabel("")
        ph_lbl.setFont(QFont("Arial", 13))
        ph_lbl.setAlignment(Qt.AlignCenter)
        ph_lbl.setStyleSheet("color:#C5B8FF; background:transparent;")
        ph_lay.addWidget(ph_lbl)

        self._placeholder = placeholder
        self._stack.addWidget(placeholder)
        cl.addWidget(self._stack)

        self._overlay = FadeOverlay(self._cc)
        return self._cc

    # ── Navigation callbacks 

    def _show_main(self):
        self._root.setCurrentIndex(1)
        self._fadein.setStartValue(0.0)
        self._fadein.setEndValue(1.0)
        self._fadein.start()
        self._stack.setCurrentWidget(self._placeholder)
        self._cur = -1

    def _go_home(self):
        self._root.setCurrentIndex(0)
        for btn in self._btns:
            btn.set_active(False)
        # Hide content panels of the currently active page
        if self._cur >= 0 and self._cur in self._pages:
            page = self._pages[self._cur]
            if isinstance(page, ContentPage):
                page._img_frame.hide()
                page._content_frame.hide()
                page._btn_row_widget.hide()
        self._cur = -1
        self._eff.setOpacity(0.0)

    def _switch(self, index: int):
       
        if index == self._cur:
            return

        if self._cur >= 0:
            self._btns[self._cur].set_active(False)

        self._btns[index].set_active(True)
        self._btns[index].bounce()

        # Update progress 
        self._visited.add(index)
        self._pbar.setValue(len(self._visited))
        self._plbl.setText(f"Progress: {len(self._visited)} / {len(TOPICS)}")

        if index not in self._pages:
            if index in ACTIVE_TOPIC_INDICES:
                page = ContentPage(TOPICS[index], STAGE[index])
            else:
                page = EmptyPage(STAGE[index])
            self._pages[index] = page
            self._stack.addWidget(page)

        self._overlay.flash(self._stack.size())
        self._stack.setCurrentWidget(self._pages[index])
        self._cur = index

        QTimer.singleShot(250, self._pages[index].show_content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())