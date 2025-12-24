from PyQt5.QtWidgets import (
    QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import random


class Game4Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe - Player vs Computer")
        self.setGeometry(350, 200, 400, 450)

        self.player = "X"
        self.computer = "O"
        self.board = [None] * 9

        layout = QVBoxLayout()

        title = QLabel("Player vs  Computer")
        title.setFont(QFont("Arial", 18))
        title.setAlignment(Qt.AlignCenter)

        self.info = QLabel("Your Turn (X)")
        self.info.setFont(QFont("Arial", 12))
        self.info.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(self.info)

        grid = QGridLayout()
        grid.setSpacing(6)

        self.buttons = []
        for i in range(9):
            btn = QPushButton("")
            btn.setFixedSize(100, 100)
            btn.setFont(QFont("Arial", 24))
            btn.clicked.connect(lambda _, idx=i: self.player_move(idx))
            self.buttons.append(btn)
            grid.addWidget(btn, i // 3, i % 3)

        layout.addLayout(grid)

        reset_btn = QPushButton("Reset Game")
        reset_btn.setFixedHeight(36)
        reset_btn.clicked.connect(self.reset_game)
        layout.addWidget(reset_btn)

        self.setLayout(layout)

    # ✅ PLAYER MOVE
    def player_move(self, idx):
        if self.board[idx] is not None:
            return

        self.board[idx] = self.player
        self.buttons[idx].setText(self.player)

        winner = self.check_winner()
        if winner:
            self.end_game(f"You Win! ")
            return

        if all(self.board):
            self.end_game("Draw!")
            return

        self.info.setText("Computer Thinking...")
        self.computer_move()

    # ✅ COMPUTER MOVE (AI)
    def computer_move(self):
        free_cells = [i for i in range(9) if self.board[i] is None]

        if not free_cells:
            return

        idx = random.choice(free_cells)
        self.board[idx] = self.computer
        self.buttons[idx].setText(self.computer)

        winner = self.check_winner()
        if winner:
            self.end_game("Computer Wins ")
            return

        if all(self.board):
            self.end_game("Draw!")
            return

        self.info.setText("Your Turn (X)")

    # ✅ WIN CHECK
    def check_winner(self):
        win_lines = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in win_lines:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    # ✅ GAME OVER
    def end_game(self, message):
        QMessageBox.information(self, "Game Over", message)
        self.reset_game()

    # ✅ RESET
    def reset_game(self):
        self.board = [None] * 9
        for btn in self.buttons:
            btn.setText("")
        self.info.setText("Your Turn (X)")
