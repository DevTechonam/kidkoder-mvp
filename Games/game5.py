import random
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Game5Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Words Game")
        self.setGeometry(350, 200, 500, 450)

        self.words = ["python", "selenium", "automation", "database", "Testing"]
        self.reset_game()

        layout = QVBoxLayout()

        # ✅ TITLE
        title = QLabel(" words GAME")
        title.setFont(QFont("Arial", 20))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # ✅ WORD DISPLAY
        self.word_label = QLabel("")
        self.word_label.setFont(QFont("Arial", 18))
        self.word_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.word_label)

        # ✅ LIFE DISPLAY
        self.life_label = QLabel("")
        self.life_label.setFont(QFont("Arial", 12))
        self.life_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.life_label)

        # ✅ LETTER BUTTONS
        self.buttons_layout = QVBoxLayout()
        self.create_letter_buttons()
        layout.addLayout(self.buttons_layout)

        # ✅ RESET BUTTON
        reset_btn = QPushButton("Reset Game")
        reset_btn.setFixedHeight(40)
        reset_btn.clicked.connect(self.reset_game)
        layout.addWidget(reset_btn)

        self.setLayout(layout)
        self.update_display()

    # ✅ CREATE A-Z BUTTONS
    def create_letter_buttons(self):
        self.letter_buttons = []
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        row_layout = QHBoxLayout()
        for i, letter in enumerate(letters):
            btn = QPushButton(letter)
            btn.setFixedSize(40, 40)
            btn.clicked.connect(lambda _, l=letter: self.check_letter(l.lower()))
            self.letter_buttons.append(btn)
            row_layout.addWidget(btn)

            if (i + 1) % 7 == 0:
                self.buttons_layout.addLayout(row_layout)
                row_layout = QHBoxLayout()

        self.buttons_layout.addLayout(row_layout)

    # ✅ RESET GAME
    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guessed = set()
        self.lives = 6

    # ✅ CHECK LETTER
    def check_letter(self, letter):
        if letter in self.guessed:
            return

        self.guessed.add(letter)

        if letter not in self.secret_word:
            self.lives -= 1

        self.update_display()

        if self.lives == 0:
            QMessageBox.information(self, "Game Over", f"You Lost! Word was: {self.secret_word}")
            self.reset_game()
            self.update_display()

        elif all(c in self.guessed for c in self.secret_word):
            QMessageBox.information(self, "Winner", "You Won the Game! 🎉")
            self.reset_game()
            self.update_display()

    # ✅ UPDATE DISPLAY
    def update_display(self):
        display_word = " ".join([c if c in self.guessed else "_" for c in self.secret_word])
        self.word_label.setText(display_word)
        self.life_label.setText(f"Lives Left: {self.lives}")
