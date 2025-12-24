import random
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Game1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Treasure Hunt Game")
        self.setGeometry(300, 150, 500, 450)

        self.main_layout = QVBoxLayout()

        self.title = QLabel(" Treasure Hunt Game")
        self.title.setFont(QFont("Arial", 20))
        self.title.setAlignment(Qt.AlignCenter)

        self.info = QLabel("Find the hidden treasure!")
        self.info.setFont(QFont("Arial", 11))
        self.info.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.info)

        self.grid = QGridLayout()
        self.buttons = []

        self.treasure_index = random.randint(0, 8)

        positions = [(i, j) for i in range(3) for j in range(3)]

        for index, position in enumerate(positions):
            btn = QPushButton("❓")
            btn.setFixedSize(100, 100)
            btn.setFont(QFont("Arial", 14))
            btn.clicked.connect(lambda _, i=index: self.check_treasure(i))
            self.buttons.append(btn)
            self.grid.addWidget(btn, *position)

        self.main_layout.addLayout(self.grid)
        self.setLayout(self.main_layout)

    def check_treasure(self, index):
        if index == self.treasure_index:
            self.buttons[index].setText("💎")
            QMessageBox.information(self, "Winner!", " You found the Treasure!")
            self.reset_game()
        else:
            self.buttons[index].setText("❌")
            self.buttons[index].setEnabled(False)

    def reset_game(self):
        self.treasure_index = random.randint(0, 8)
        for btn in self.buttons:
            btn.setText("❓")
            btn.setEnabled(True)
