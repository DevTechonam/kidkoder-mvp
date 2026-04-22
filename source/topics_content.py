# content_page.py
# ContentPage displays images  descriptions for an active topic.
# Images are loaded from a snaps folder on disk (preferred) or fall
# EmptyPage blank coloured page shown for topics not yet activated.

import os
import json
from pathlib import Path

from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap





def _build_snaps_path(tag):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    snaps_path = os.path.join(
        project_root,
        "lessons",
        "modules",
        "module1",
        "topics",
        tag,
        "snaps"
    )

    return os.path.normpath(snaps_path)


def _load_metadata(snaps_dir: str) -> dict:
   
    metadata_path = os.path.join(snaps_dir, "metadata.json")
    try:
        with open(metadata_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        print(f"[_load_metadata] Loaded {len(data)} metadata entries.")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"[_load_metadata] WARNING — could not load metadata: {exc}")
        return {}


def _collect_images_from_disk(snaps_dir: str, metadata: dict) -> list:
  
    images = []
    SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")
    try:
        entries = sorted(os.listdir(snaps_dir))   
    except FileNotFoundError:
        return images

    for filename in entries:
        if not filename.lower().endswith(SUPPORTED_FORMATS):
            continue
        stem = Path(filename).stem

        if stem not in metadata:
            print(f"[_collect_images_from_disk] Skipping {filename} (not in metadata)")
            continue

        content = metadata[stem].get("content", "")
        full_path = os.path.join(snaps_dir, filename)
        images.append({"path": full_path, "content": content})
        print(f"[_collect_images_from_disk]   + {filename}")

    print(f"[_collect_images_from_disk] Found {len(images)} image(s).")
    return images


# ── ContentPage 

class ContentPage(QWidget):
   

    def __init__(self, topic: dict, pal: dict):
        super().__init__()

        self._idx = 0
        self._images_data = self._resolve_images(topic)


        self.setStyleSheet(f"ContentPage {{ background: {pal['bg']}; }}")

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(self._build_header(topic, pal))
        root.addWidget(self._build_centre(pal), 1)

    # ── Image resolution (disk → fallback) 

    def _resolve_images(self, topic: dict) -> list:
      
        tag = topic.get("tag", "")
        if tag:
            snaps_dir = _build_snaps_path(tag)
            metadata  = _load_metadata(snaps_dir)
            disk_images = _collect_images_from_disk(snaps_dir, metadata)
            if disk_images:
                return disk_images

        # Fall back to hardcoded list
        fallback = list(topic.get("images", []))
        return fallback

    # ── UI builders 

    def _build_header(self, topic: dict, pal: dict) -> QFrame:
        header = QFrame()
        header.setFixedHeight(80)
        header.setStyleSheet(
            f"background:{pal['side']}; border-bottom: 3px solid {pal['btn_on']};"
        )
        hlay = QHBoxLayout(header)
        hlay.setContentsMargins(24, 0, 20, 0)
        hlay.setSpacing(10)

        emo = QLabel(topic["emoji"])
        emo.setFont(QFont("Segoe UI Emoji", 28))
        emo.setStyleSheet("background:transparent; color:#FFFFFF;")
        hlay.addWidget(emo)

        title = QLabel(topic["name"])
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet(f"background:transparent; color:{pal['title']};")

        hlay.addWidget(title)

        hlay.addStretch()

        ''' self._counter_lbl = QLabel("")
        self._counter_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self._counter_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self._counter_lbl.setMinimumWidth(110)
        self._counter_lbl.setStyleSheet(
            f"background:transparent; color:{pal['ctitle']}; border:none;"
        )
        hlay.addWidget(self._counter_lbl)'''

        return header

    def _build_centre(self, pal: dict) -> QWidget:
        centre = QWidget()
        centre.setStyleSheet(f"background:{pal['bg']};")
        cv = QVBoxLayout(centre)
        cv.setContentsMargins(40, 20, 40, 24)
        cv.setSpacing(20)
        cv.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # Image frame
        self._img_frame = QFrame()
        self._img_frame.setFixedSize(1200, 650)
        self._img_frame.setStyleSheet(
            f"QFrame {{ background:{pal['side']}; border-radius:22px; "
            f"border: 4px solid {pal['btn_on']}; }}"
        )
        self._img_frame.hide()
        ifl = QVBoxLayout(self._img_frame)
        ifl.setContentsMargins(0,0,0,0)

        self._img_lbl = QLabel()
        self._img_lbl.setAlignment(Qt.AlignCenter)
        self._img_lbl.setWordWrap(True)
        self._img_lbl.setStyleSheet("background:transparent; border:none;")
        ifl.addWidget(self._img_lbl)
        cv.addWidget(self._img_frame, alignment=Qt.AlignHCenter)

        # Description frame
        '''self._content_frame = QFrame()
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
        cv.addWidget(self._content_frame, alignment=Qt.AlignHCenter)'''

        # Nav buttons
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

        return centre

    # ── Navigation 

    def _on_prev(self):
        if self._idx > 0:
            self._idx -= 1
            self._display()

    def _on_next(self):
        if self._idx < len(self._images_data) - 1:
            self._idx += 1
            self._display()

    # ── Rendering 

    def _display(self):
        if not self._images_data:
            return

        img   = self._images_data[self._idx]
        path  = img["path"]
        #text  = img.get("content", "") or f"📄  {os.path.basename(path)}"

        #self._desc_lbl.setText(text)

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
        #self._counter_lbl.setText(f"Image {self._idx + 1} / {total}")
        self._prev_btn.setEnabled(self._idx > 0)
        self._next_btn.setEnabled(self._idx < total - 1)

    def _refresh_view(self):
        has = bool(self._images_data)
        self._img_frame.setVisible(has)
        #self._content_frame.setVisible(has)
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


# ── EmptyPage 

class EmptyPage(QWidget):

    def __init__(self, pal: dict):
        super().__init__()
        self.setStyleSheet(f"EmptyPage {{ background: {pal['bg']}; }}")

    def show_content(self):
        print("[EmptyPage.show_content] Nothing to show.")


#print("[content_page] ContentPage / EmptyPage ready.")