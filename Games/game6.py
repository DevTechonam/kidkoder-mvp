from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import random


class Game6Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(350, 200, 400, 350)

        self.choices = ["Rock", "Paper", "Scissors"]

        layout = QVBoxLayout()

        title = QLabel("🪨 Rock  📄 Paper  ✂️ Scissors")
        title.setFont(QFont("Arial", 18))
        title.setAlignment(Qt.AlignCenter)

        self.result_label = QLabel("Choose your move")
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(self.result_label)

        # ✅ BUTTON LAYOUT
        btn_layout = QHBoxLayout()

        rock_btn = QPushButton("🪨 Rock")
        paper_btn = QPushButton("📄 Paper")
        scissors_btn = QPushButton("✂️ Scissors")

        for btn in (rock_btn, paper_btn, scissors_btn):
            btn.setFont(QFont("Arial", 11))
            btn.setFixedHeight(40)

        rock_btn.clicked.connect(lambda: self.play("Rock"))
        paper_btn.clicked.connect(lambda: self.play("Paper"))
        scissors_btn.clicked.connect(lambda: self.play("Scissors"))

        btn_layout.addWidget(rock_btn)
        btn_layout.addWidget(paper_btn)
        btn_layout.addWidget(scissors_btn)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

    # ✅ GAME LOGIC
    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        if user_choice == computer_choice:
            result = "It's a Draw!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win! "
        else:
            result = "Computer Wins "

        QMessageBox.information(
            self,
            "Result",
            f"Your Choice: {user_choice}\nComputer Choice: {computer_choice}\n\n{result}"
        )
