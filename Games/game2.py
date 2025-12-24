from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Game2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Quiz Game")
        self.setGeometry(350, 200, 600, 400)

        layout = QVBoxLayout()

        title = QLabel(" Python Quiz")
        title.setFont(QFont("Arial", 20))
        title.setAlignment(Qt.AlignCenter)

        question = QLabel("Q1. What is the output of: print(2 + 3 * 2)?")
        question.setFont(QFont("Arial", 12))
        question.setAlignment(Qt.AlignCenter)

        self.btn1 = QPushButton("A) 10")
        self.btn2 = QPushButton("B) 8")
        self.btn3 = QPushButton("C) 12")
        self.btn4 = QPushButton("D) 5")

        for btn in (self.btn1, self.btn2, self.btn3, self.btn4):
            btn.setFixedHeight(40)

        self.btn1.clicked.connect(lambda: self.check_answer(False))
        self.btn2.clicked.connect(lambda: self.check_answer(True))
        self.btn3.clicked.connect(lambda: self.check_answer(False))
        self.btn4.clicked.connect(lambda: self.check_answer(False))

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(question)
        layout.addSpacing(10)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)

        self.setLayout(layout)

    def check_answer(self, correct):
        if correct:
            QMessageBox.information(self, "Correct ", "Good job! Answer is 7")
        else:
            QMessageBox.warning(self, "Wrong ", "Try again!")
