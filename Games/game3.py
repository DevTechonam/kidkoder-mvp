import random
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Game3Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guess The Number Game")
        self.setGeometry(350, 200, 400, 350)

        self.number = random.randint(1, 10)

        layout = QVBoxLayout()

        title = QLabel(" Guess The Number (1 to 10)")
        title.setFont(QFont("Arial", 18))
        title.setAlignment(Qt.AlignCenter)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter your guess...")
        self.input.setFixedHeight(35)
        self.input.setAlignment(Qt.AlignCenter)

        self.btn = QPushButton("Check")
        self.btn.setFixedHeight(40)

        self.reset_btn = QPushButton("Reset Game")
        self.reset_btn.setFixedHeight(35)

        self.btn.clicked.connect(self.check_number)
        self.reset_btn.clicked.connect(self.reset_game)

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.input)
        layout.addWidget(self.btn)
        layout.addWidget(self.reset_btn)

        self.setLayout(layout)

    def check_number(self):
        try:
            guess = int(self.input.text())
            if guess == self.number:
                QMessageBox.information(self, "Winner ", "Correct! You guessed the number!")
            elif guess < self.number:
                QMessageBox.warning(self, "Try Again", "Too Low!")
            else:
                QMessageBox.warning(self, "Try Again", "Too High!")
        except:
            QMessageBox.warning(self, "Invalid", "Please enter a number")

    def reset_game(self):
        self.number = random.randint(1, 10)
        self.input.clear()
        QMessageBox.information(self, "Reset", "New number generated!")
