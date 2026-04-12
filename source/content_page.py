import sys
import os
import json
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

from pprint import pprint

from pathlib import Path



CONTENT_BASE_PATH = "C:\\Users\\91998\\Documents\\GitRepos\\kidkoder-mvp\\lessons\\modules\\module1\\topics\\{}\\snaps"
# Content Page 

class ContentPage(QWidget):
    def __init__(self, topic, pal, content_path=""):
        print("Inside Content Page __init__")
        pprint(content_path)
        super().__init__()
        self.topic_tag = topic["tag"].lower()
        #self._images_data = list(topic["images"])
        self.content_base_path = CONTENT_BASE_PATH.format(self.topic_tag)
        self.image_content = self.get_image_content()
        self._images_data = self.get_topic_images()
       
        print("************")
        pprint(self._images_data)
        print(self.topic_tag)
        print(self.content_base_path)
        print("************")
        self._idx         = 0

        self.setStyleSheet(f"ContentPage {{ background: {pal['bg']}; }}")

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Header ────────────────────────────────────────────────────────────
        header = QFrame()
        header.setFixedHeight(64)
        header.setStyleSheet(
            f"background:{pal['side']}; border-bottom: 3px solid {pal['btn_on']};"
        )
        hlay = QHBoxLayout(header)
        hlay.setContentsMargins(24, 0, 20, 0)
        hlay.setSpacing(10)

        emo_lbl = QLabel(topic["emoji"])
        emo_lbl.setFont(QFont("Segoe UI Emoji", 28))
        emo_lbl.setStyleSheet("background:transparent; color:#FFFFFF;")
        hlay.addWidget(emo_lbl)

        name_lbl = QLabel(topic["name"])
        name_lbl.setFont(QFont("Arial", 18, QFont.Bold))
        name_lbl.setStyleSheet(f"background:transparent; color:{pal['title']};")
        hlay.addWidget(name_lbl)

        hlay.addStretch()

        self._counter_lbl = QLabel("")
        self._counter_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self._counter_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self._counter_lbl.setMinimumWidth(110)
        self._counter_lbl.setStyleSheet(
            f"background:transparent; color:{pal['ctitle']}; border:none;"
        )
        hlay.addWidget(self._counter_lbl)

        root.addWidget(header)

        # ── Centre area 
        centre = QWidget()
        centre.setStyleSheet(f"background:{pal['bg']};")
        cv = QVBoxLayout(centre)
        cv.setContentsMargins(40, 20, 40, 24)
        cv.setSpacing(20)
        cv.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # Image display frame
        self._img_frame = QFrame()
        self._img_frame.setFixedSize(1200, 580)
        self._img_frame.setStyleSheet(
            f"QFrame {{ background:{pal['side']}; border-radius:22px; "
            f"border: 4px solid {pal['btn_on']}; }}"
        )
        self._img_frame.hide()
        ifl = QVBoxLayout(self._img_frame)
        ifl.setContentsMargins(12, 12, 12, 12)

        self._img_lbl = QLabel()
        self._img_lbl.setAlignment(Qt.AlignCenter)
        self._img_lbl.setWordWrap(True)
        self._img_lbl.setStyleSheet("background:transparent; border:none;")
        ifl.addWidget(self._img_lbl)
        cv.addWidget(self._img_frame, alignment=Qt.AlignHCenter)

        # Description box
        self._content_frame = QFrame()
        self._content_frame.setStyleSheet(
            f"QFrame {{ background:{pal['side']}; border-radius:14px; "
            f"border: 2px solid {pal['btn_on']}; }}"
        )
        self._content_frame.setFixedHeight(120)
        self._content_frame.hide()
        cfl = QVBoxLayout(self._content_frame)
        cfl.setContentsMargins(20, 15, 20, 15)

        self._desc_lbl = QLabel()
        self._desc_lbl.setFont(QFont("Arial", 11))
        self._desc_lbl.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self._desc_lbl.setWordWrap(True)
        self._desc_lbl.setStyleSheet(
            f"color:{pal['body']}; background:transparent; border:none;"
        )
        cfl.addWidget(self._desc_lbl)
        cv.addWidget(self._content_frame, alignment=Qt.AlignHCenter)

        # Prev / Next buttons
        nav_style = f"""
            QPushButton {{
                background: {pal['btn_off']}; border-radius: 12px;
                color: #FFFFFF; border: 2px solid {pal['btn_on']};
            }}
            QPushButton:hover {{ background: {pal['hover']}; border: 2px solid #FFFFFF; }}
            QPushButton:disabled {{ background: {pal['side']}; color: #555555; border: 2px solid #333333; }}
        """

        self._prev_btn = QPushButton("◀   Prev")
        self._prev_btn.setFixedSize(140, 50)
        self._prev_btn.setFont(QFont("Arial", 11, QFont.Bold))
        self._prev_btn.setCursor(Qt.PointingHandCursor)
        self._prev_btn.setStyleSheet(nav_style)
        self._prev_btn.setEnabled(False)
        self._prev_btn.clicked.connect(self._on_prev)
        self._prev_btn.hide()

        self._next_btn = QPushButton("Next   ▶")
        self._next_btn.setFixedSize(140, 50)
        self._next_btn.setFont(QFont("Arial", 11, QFont.Bold))
        self._next_btn.setCursor(Qt.PointingHandCursor)
        self._next_btn.setStyleSheet(nav_style)
        self._next_btn.clicked.connect(self._on_next)
        self._next_btn.hide()

        btn_row = QHBoxLayout()
        btn_row.setSpacing(18)
        btn_row.setAlignment(Qt.AlignHCenter)
        btn_row.addWidget(self._prev_btn)
        btn_row.addStretch()
        btn_row.addWidget(self._next_btn)

        self._btn_row_widget = QWidget()
        self._btn_row_widget.setLayout(btn_row)
        self._btn_row_widget.hide()
        cv.addWidget(self._btn_row_widget)

        root.addWidget(centre, 1)


    def get_image_content(self):
        metadata_path = os.path.join(self.content_base_path, "metadata.json")
        with open(metadata_path, "r") as file:
            data = json.load(file)

        return(data)


    def get_topic_images(self):
        image_files = []
        if os.path.isdir(self.content_base_path):
            print(f"Directory exists: {self.content_base_path }")

            for f in os.listdir(self.content_base_path ):
                if f.lower().endswith('.jpg'):
                    filename = Path(f)
                    image_key = filename.stem
                    image_content = self.image_content[image_key]["content"]
                    img_topic_path = os.path.join(self.content_base_path , f)
                    print(img_topic_path)
                    image_files.append({"path": img_topic_path, "content": image_content})
            return image_files
        else:
            print(f"Directory does not exist: {CONTENT_BASE_PATH}")

    # ── Navigation 
    def _on_prev(self):
        if self._idx > 0:
            self._idx -= 1
            self._display()

    def _on_next(self):
        if self._idx < len(self._images_data) - 1:
            self._idx += 1
            self._display()

    # ── Render current image 

    def _display(self):
        if not self._images_data:
            return
        
    
        img_data = self._images_data[self._idx]
        path     = img_data["path"]
        content  = img_data.get("content", "")

        self._desc_lbl.setText(content if content else f"📄  {os.path.basename(path)}")

        pix = QPixmap(path)
        if pix.isNull():
            self._img_lbl.setText(f"❌  Image not found:\n{os.path.basename(path)}")
            self._img_lbl.setFont(QFont("Arial", 11))
            self._img_lbl.setStyleSheet("color:#FF6666; background:transparent; border:none;")
        else:
            self._img_lbl.setStyleSheet("background:transparent; border:none;")
            self._img_lbl.setPixmap(
                pix.scaled(
                    self._img_lbl.width()  or 1150,
                    self._img_lbl.height() or 540,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )
       
        total = len(self._images_data)
        self._counter_lbl.setText(f"Image {self._idx + 1} / {total}")
        self._prev_btn.setEnabled(self._idx > 0)
        self._next_btn.setEnabled(self._idx < total - 1)
        
    

    def _refresh_view(self):
        has = bool(self._images_data)
        self._img_frame.setVisible(has)
        self._content_frame.setVisible(has)
        self._btn_row_widget.setVisible(has)
        self._prev_btn.setVisible(has)
        self._next_btn.setVisible(has)
        if has:
            self._display()
        else:
            self._counter_lbl.setText("")

    def show_content(self):
        self._idx = 0
        self._refresh_view()


# ── Empty Page 
class EmptyPage(QWidget):
    def __init__(self, pal):
        super().__init__()
        self.setStyleSheet(f"EmptyPage {{ background: {pal['bg']}; }}")

    def show_content(self):
        pass

