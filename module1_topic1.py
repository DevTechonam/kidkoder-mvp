import sys
import os
import math
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QStackedWidget, QFrame,
    QGraphicsOpacityEffect, QProgressBar, QFileDialog,
    QMessageBox
)
from PyQt5.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QTimer,
    QPoint, pyqtProperty
)
from PyQt5.QtGui import QFont, QPixmap

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))


SAVED_IMAGES_FILE = os.path.join(BASE_DIR, "saved_images.json")

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp', '.tiff', '.tif'}


STAGE = [
    dict(bg="#3B1F8C", side="#2D1870", title="#FFE566", ctitle="#FF94C2",
         body="#E8D5FF", btn_on="#FF94C2", btn_off="#5C3BBF", hover="#7B55D9"),
    dict(bg="#C0134E", side="#960F3D", title="#FFF176", ctitle="#FFD6E8",
         body="#FFE8F0", btn_on="#FF6BAE", btn_off="#E0366E", hover="#F05090"),
    dict(bg="#0B4F8A", side="#083B6A", title="#ADEBFF", ctitle="#80D8FF",
         body="#D6F0FF", btn_on="#40C4FF", btn_off="#1565C0", hover="#1E88E5"),
    dict(bg="#1B6B3A", side="#145230", title="#C6FF8A", ctitle="#A5FFB0",
         body="#D8FFE4", btn_on="#69FF8A", btn_off="#2E7D50", hover="#43A862"),
    dict(bg="#B84B00", side="#8F3900", title="#FFF59D", ctitle="#FFD180",
         body="#FFEEC8", btn_on="#FFAB40", btn_off="#D45500", hover="#EF6C00"),
    dict(bg="#5B0F8E", side="#470C70", title="#E8B4FF", ctitle="#CE93D8",
         body="#F3E0FF", btn_on="#CE93D8", btn_off="#7B1FA2", hover="#9C27B0"),
    dict(bg="#7A5100", side="#5E3D00", title="#FFEE58", ctitle="#FFCC02",
         body="#FFF8DC", btn_on="#FFD740", btn_off="#9E6A00", hover="#F9A825"),
    dict(bg="#006064", side="#004D51", title="#84FFFF", ctitle="#A7FFEB",
         body="#D0FFF8", btn_on="#64FFDA", btn_off="#00838F", hover="#00ACC1"),
]

SIDEBAR_BG = "#12005E"
BRAND_BG   = "#1E0080"
WELCOME_BG = "#12005E"


TOPICS = [
    {
        "name": "What is a Computer", "emoji": "💻",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "compu.jpg"),
             "content": "📚 What is a Computer?\n\nA computer is an electronic device that processes information and helps us solve problems, create things, and connect with others around the world!"},
            {"path": os.path.join(BASE_DIR, "images", "cpu.jpg"),
             "content": "⚙️ Inside the Computer\n\nThis is the CPU (Central Processing Unit) - it's like the brain of the computer! It makes all the decisions and does all the calculations."},
            {"path": os.path.join(BASE_DIR, "images", "monitor.jpeg"),
             "content": "🖥️ Monitor\n\nThe monitor shows us pictures, videos, and everything we do on the computer."},
        ]
    },
    {
        "name": "Keyboard & Mouse", "emoji": "⌨️",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "keyboard.jpg"),
             "content": "⌨️ Keyboard\n\nThe keyboard is how we type information into the computer. Each key has a letter, number, or special character on it!"},
            {"path": os.path.join(BASE_DIR, "images", "keyboard2.jpg.jpeg"),
             "content": "⌨️ Keyboard\n\nThe keyboard is how we type information into the computer. Each key has a letter, number, or special character on it!"},
            {"path": os.path.join(BASE_DIR, "images", "mouse.jpeg"),
             "content": "🖱️ Mouse\n\nThe mouse helps us move the pointer on the screen and click to open, select, and move things on the computer."},
        ]
    },
    {
        "name": "Files & Folders", "emoji": "📁",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "file.png"),
             "content": "📁 Files & Folders\n\nFiles are like documents and pictures. Folders are like containers that hold multiple files organized together!"},
            {"path": os.path.join(BASE_DIR, "images", "folder.png"),
             "content": "📁 Files & Folders\n\nFiles are like documents and pictures. Folders are like containers that hold multiple files organized together!"},
        ]
    },
    {
        "name": "Operating System", "emoji": "🖥️",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "Osystem.jpg"),
             "content": "🖥️ Operating System\n\nThe Operating System is like a manager! It controls all the programs and makes sure everything works smoothly together."},
            {"path": os.path.join(BASE_DIR, "images", "Osystem2.jpg"),
             "content": "🖥️ Operating System\n\nThe Operating System is like a manager! It controls all the programs and makes sure everything works smoothly together."},
        ]
    },
    {
        "name": "Text Editors", "emoji": "📝",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "text_editor.jpg"),
             "content": "📝 Text Editors\n\nText editors are programs where you can write and edit text. They're simple tools for creating documents!"},
        ]
    },
    {
        "name": "Internet Safety", "emoji": "🛡️",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "internet.jpg"),
             "content": "🛡️ Internet Safety\n\nStay safe online! Never share personal information, use strong passwords, and always ask an adult before visiting websites."},
            {"path": os.path.join(BASE_DIR, "images", "internet2.jpg"),
             "content": "🛡️ Internet Safety\n\nStay safe online! Never share personal information, use strong passwords, and always ask an adult before visiting websites."},
        ]
    },
    {
        "name": "Problem Solving", "emoji": "🧩",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "problem_solve.jpg"),
             "content": "🧩 Problem Solving\n\nProblem solving means breaking down big problems into smaller steps and finding solutions. This is what computers do!"},
        ]
    },
    {
        "name": "Numbers & Logic", "emoji": "🔢",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "number.png"),
             "content": "🔢 Numbers & Logic\n\nComputers work with numbers and logic. They use patterns and rules to process information very quickly!"},
        ]
    },
]




def load_saved_images() -> dict:
    """Read the JSON file and return a dict  {topic_name: [image_dicts]}."""
    if not os.path.exists(SAVED_IMAGES_FILE):
        return {}
    try:
        with open(SAVED_IMAGES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Validate — must be a dict of lists
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    return {}


def save_images_for_topic(topic_name: str, user_images: list):
    """
    Persist only the USER-ADDED images for one topic.
    user_images is a list of dicts {"path": ..., "content": ...}
    The hardcoded images/ folder images are NOT stored here — they always load from TOPICS.
    """
    data = load_saved_images()
    data[topic_name] = user_images
    try:
        with open(SAVED_IMAGES_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[save error] {e}")


def get_saved_images_for_topic(topic_name: str) -> list:
    """Return the saved user-added images for a topic (empty list if none)."""
    data = load_saved_images()
    return data.get(topic_name, [])


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


# ── Topic Button 

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


# ── Content Page 

class ContentPage(QWidget):
    def __init__(self, topic, pal):
        super().__init__()
        self._pal        = pal
        self._topic      = topic
        self._topic_name = topic["name"]
        self._idx        = 0

       
        self._default_images = list(topic["images"])          # never removed
        self._user_images    = get_saved_images_for_topic(self._topic_name)  # persisted
        # Combined list — single source of truth used by _display()
        self._images_data    = self._default_images + self._user_images

        self.setStyleSheet(f"ContentPage {{ background: {pal['bg']}; }}")

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Header 
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

        # "Image X / Y" counter
        self._counter_lbl = QLabel("")
        self._counter_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self._counter_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self._counter_lbl.setMinimumWidth(110)
        self._counter_lbl.setStyleSheet(
            f"background:transparent; color:{pal['ctitle']}; border:none;"
        )
        hlay.addWidget(self._counter_lbl)

        # ＋ Add Photo button
        add_btn = QPushButton("  ＋  Add Photo")
        add_btn.setFont(QFont("Arial", 10, QFont.Bold))
        add_btn.setFixedHeight(36)
        add_btn.setCursor(Qt.PointingHandCursor)
        add_btn.setStyleSheet(f"""
            QPushButton {{
                background: {pal['btn_on']}; border-radius: 10px;
                color: #1A0050; border: 2px solid #FFFFFF; padding: 0 16px;
            }}
            QPushButton:hover {{ background: #FFFFFF; color: {pal['side']}; border: 2px solid {pal['btn_on']}; }}
            QPushButton:pressed {{ background: {pal['hover']}; color: #FFFFFF; }}
        """)
        add_btn.clicked.connect(self._open_file_picker)
        hlay.addWidget(add_btn)

        # 🗑 Delete Current Image button
        del_btn = QPushButton("  🗑  Delete")
        del_btn.setFont(QFont("Arial", 10, QFont.Bold))
        del_btn.setFixedHeight(36)
        del_btn.setCursor(Qt.PointingHandCursor)
        del_btn.setStyleSheet(f"""
            QPushButton {{
                background: #8B0000; border-radius: 10px;
                color: #FFFFFF; border: 2px solid #FF6666; padding: 0 14px;
            }}
            QPushButton:hover {{ background: #FF2222; border: 2px solid #FFFFFF; }}
            QPushButton:pressed {{ background: #660000; }}
        """)
        del_btn.clicked.connect(self._delete_current_image)
        hlay.addWidget(del_btn)

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

    #  ADD PHOTO — opens OS file manager, saves to JSON immediately
    

    def _open_file_picker(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Photos to Add",
            os.path.expanduser("~"),
            "Images (*.jpg *.jpeg *.png *.bmp *.gif *.webp *.tiff *.tif);;"
            "All Files (*)"
        )
        if not files:
            return

        existing_paths = {img["path"] for img in self._images_data}
        first_new_idx  = len(self._images_data)

        for f in files:
            if f not in existing_paths:
                entry = {"path": f, "content": ""}
                self._images_data.append(entry)
                self._user_images.append(entry)   # track user-added separately
                existing_paths.add(f)

        if len(self._images_data) > first_new_idx:
            # ── Save immediately so it persists after app restart ─────
            save_images_for_topic(self._topic_name, self._user_images)
            self._idx = first_new_idx
            self._refresh_view()

    # 
    #  DELETE CURRENT IMAGE — only user-added images can be deleted
    #  Hardcoded images/ folder images are protected
    

    def _delete_current_image(self):
        if not self._images_data:
            return

        num_defaults = len(self._default_images)

        
        if self._idx < num_defaults:
            QMessageBox.information(
                self,
                "Cannot Delete",
                "This is a built-in image and cannot be deleted.\n\n"
                "Only images you added via '＋ Add Photo' can be deleted."
            )
            return

        # Confirm deletion
        img_name = os.path.basename(self._images_data[self._idx]["path"])
        reply = QMessageBox.question(
            self,
            "Delete Image",
            f"Remove  \"{img_name}\"  from this topic?\n\n"
            "This will NOT delete the file from your computer,\n"
            "only remove it from the app.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply != QMessageBox.Yes:
            return

        # Remove from both lists
        removed = self._images_data.pop(self._idx)
        # Remove from user
        self._user_images = [
            img for img in self._user_images
            if img["path"] != removed["path"]
        ]

        # ── Save updated list to JSON so deletion persists 
        save_images_for_topic(self._topic_name, self._user_images)

        # Adjust index so we don't go out of bounds
        if self._idx >= len(self._images_data):
            self._idx = max(0, len(self._images_data) - 1)

        self._refresh_view()

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

        img_data = self._images_data[self._idx]   # always a dict ✓
        path     = img_data["path"]
        content  = img_data.get("content", "")

        # Show content or filename
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

    # ── Show / hide panels 

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
        """Called by MainWindow when this topic is selected."""
        self._idx = 0
        self._refresh_view()


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


# ── Main Window 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 Computer Basics for Kids!")
        self.setMinimumSize(980, 620)
        self.resize(1100, 680)

        self._cur     = -1
        self._btns    = []
        self._visited = set()
        self._pages   = {}

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

        # Sidebar
        sb = QWidget()
        sb.setFixedWidth(196)
        sb.setStyleSheet(f"QWidget {{ background: {SIDEBAR_BG}; }}")
        sv = QVBoxLayout(sb)
        sv.setContentsMargins(8, 10, 8, 10)
        sv.setSpacing(5)

        brand = QLabel("🚀  CS for Kids")
        brand.setFont(QFont("Arial", 11, QFont.Bold))
        brand.setAlignment(Qt.AlignCenter)
        brand.setFixedHeight(38)
        brand.setStyleSheet(
            f"color: #FFE566; background: {BRAND_BG}; "
            "border-radius: 10px; border: 2px solid #5533CC;"
        )
        sv.addWidget(brand)

        self._plbl = QLabel("Progress: 0 / 8")
        self._plbl.setFont(QFont("Arial", 8, QFont.Bold))
        self._plbl.setAlignment(Qt.AlignCenter)
        self._plbl.setStyleSheet("color:#C5B8FF; background:transparent;")

        self._pbar = QProgressBar()
        self._pbar.setMaximum(len(TOPICS))
        self._pbar.setValue(0)
        self._pbar.setTextVisible(False)
        self._pbar.setFixedHeight(6)
        self._pbar.setStyleSheet("""
            QProgressBar { background: #2A0080; border-radius:3px; border:none; }
            QProgressBar::chunk { background: #FFE566; border-radius:3px; }
        """)
        sv.addWidget(self._plbl)
        sv.addWidget(self._pbar)
        sv.addSpacing(5)

        for i, t in enumerate(TOPICS):
            btn = TopicButton(t, i, self._switch, STAGE[i])
            sv.addWidget(btn)
            self._btns.append(btn)

        sv.addStretch()

        hbtn = QPushButton("🏠  Home")
        hbtn.setFont(QFont("Arial", 9, QFont.Bold))
        hbtn.setFixedHeight(34)
        hbtn.setCursor(Qt.PointingHandCursor)
        hbtn.setStyleSheet("""
            QPushButton { background: #2A0080; border: 2px solid #5533CC; border-radius: 9px; color: #C5B8FF; }
            QPushButton:hover { background: #5533CC; color: #FFFFFF; border: 2px solid #FFFFFF; }
        """)
        hbtn.clicked.connect(self._go_home)
        sv.addWidget(hbtn)

        # Content area
        self._cc = QWidget()
        self._cc.setStyleSheet(f"background:{SIDEBAR_BG};")
        cl = QVBoxLayout(self._cc)
        cl.setContentsMargins(0, 0, 0, 0)

        self._stack = QStackedWidget()
        self._stack.setStyleSheet("background:transparent;")

        placeholder = QWidget()
        placeholder.setStyleSheet(f"background:{SIDEBAR_BG};")
        ph_lbl = QLabel(
            
        )
        ph_lbl.setFont(QFont("Arial", 13))
        ph_lbl.setAlignment(Qt.AlignCenter)
        ph_lbl.setStyleSheet("color:#C5B8FF; background:transparent;")
        ph_lay = QVBoxLayout(placeholder)
        ph_lay.setAlignment(Qt.AlignCenter)
        ph_lay.addWidget(ph_lbl)

        self._placeholder = placeholder
        self._stack.addWidget(placeholder)

        cl.addWidget(self._stack)
        self._overlay = FadeOverlay(self._cc)

        h.addWidget(sb)
        h.addWidget(self._cc, 1)

    def _show_main(self):
        self._root.setCurrentIndex(1)
        self._fadein.setStartValue(0.0)
        self._fadein.setEndValue(1.0)
        self._fadein.start()
        self._stack.setCurrentWidget(self._placeholder)
        self._cur = -1

    def _go_home(self):
        self._root.setCurrentIndex(0)
        for b in self._btns:
            b.set_active(False)
        if self._cur >= 0 and self._cur in self._pages:
            page = self._pages[self._cur]
            page._img_frame.hide()
            page._content_frame.hide()
            page._btn_row_widget.hide()
        self._cur = -1
        self._eff.setOpacity(0.0)

    def _switch(self, index):
        if index == self._cur:
            return
        if self._cur >= 0:
            self._btns[self._cur].set_active(False)
        self._btns[index].set_active(True)
        self._btns[index].bounce()

        self._visited.add(index)
        self._pbar.setValue(len(self._visited))
        self._plbl.setText(f"Progress: {len(self._visited)} / {len(TOPICS)}")

        if index not in self._pages:
            page = ContentPage(TOPICS[index], STAGE[index])
            self._pages[index] = page
            self._stack.addWidget(page)

        self._overlay.flash(self._stack.size())
        self._stack.setCurrentWidget(self._pages[index])
        self._cur = index

        QTimer.singleShot(250, self._pages[index].show_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())