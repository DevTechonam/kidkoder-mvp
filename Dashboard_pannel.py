from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QStackedWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from Games.game1 import Game1Window
from Games.game2 import Game2Window
from Games.game3 import Game3Window
from Games.game4 import Game4Window
from Games.game5 import Game5Window
from Games.game6 import Game6Window



class GamePanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Dashboard")

        main_layout = QHBoxLayout()

        # -----------------------------
        # LEFT MENU PANEL
        # -----------------------------
        left_panel = QFrame()
        left_panel.setFixedWidth(280)
        left_panel.setStyleSheet("background-color:#0b4f6c;")
        left_layout = QVBoxLayout()

        title = QLabel(" GAMES")
        title.setFont(QFont("Arial", 16))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color:white; padding:15px;")

        # Buttons
        buttons = {
            "Game 1 - Treasure Hunt": self.show_game1,
            "Game 2 - Python Quiz": self.show_game2,
            "Game 3 - Guess Number": self.show_game3,
            "Game 4 - Tic Tac Toe": self.show_game4,
            "Game 5 - Words Game": self.show_game5,
            "Game 6 - Rock Paper Scissor": self.show_game6,
           
        }

        # Create button objects
        for text, function in buttons.items():
            btn = QPushButton(text)
            btn.setFont(QFont("Arial", 11))
            btn.setFixedHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: red;
                    color: white;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: darkred;
                }
            """)
            btn.clicked.connect(function)
            left_layout.addWidget(btn)

        # Exit button
        btn_exit = QPushButton("Exit")
        btn_exit.setFixedHeight(40)
        btn_exit.setStyleSheet("""
            QPushButton {
                background-color:#522;
                color:white;
                border-radius:8px;
            }
            QPushButton:hover {
                background-color:#300;
            }
        """)
        btn_exit.clicked.connect(self.close)

        left_layout.addStretch()
        left_layout.addWidget(btn_exit)
        left_panel.setLayout(left_layout)

        # -----------------------------
        # RIGHT PANEL (STACK)
        # -----------------------------
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("")

        # Default welcome page
        welcome_widget = QWidget()
        welcome_widget.setStyleSheet("background-color:#123456;") 
        w_layout = QVBoxLayout()

        title2 = QLabel("Welcome to Python Game Dashboard")
        title2.setFont(QFont("Arial", 18))
        title2.setStyleSheet("color:white;")
        title2.setAlignment(Qt.AlignCenter)

        sub = QLabel("Select a game from the left panel")
        sub.setFont(QFont("Arial", 12))
        sub.setStyleSheet("color:lightgray;")
        sub.setAlignment(Qt.AlignCenter)

        w_layout.addStretch()
        w_layout.addWidget(title2)
        w_layout.addWidget(sub)
        w_layout.addStretch()

        welcome_widget.setLayout(w_layout)
        

        self.stack.addWidget(welcome_widget)

        # Add all game pages
        self.game1 = Game1Window()
        self.game2 = Game2Window()
        self.game3 = Game3Window()
        self.game4 = Game4Window()
        self.game5 = Game5Window()
        self.game6 = Game6Window()
        

        self.stack.addWidget(self.game1)
        self.stack.addWidget(self.game2)
        self.stack.addWidget(self.game3)
        self.stack.addWidget(self.game4)
        self.stack.addWidget(self.game5)
        self.stack.addWidget(self.game6)
        

        main_layout.addWidget(left_panel)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)
    

    # GAME SWITCH FUNCTIONS
    def show_game1(self):
        self.stack.setCurrentWidget(self.game1)
        

    def show_game2(self):
        self.stack.setCurrentWidget(self.game2)

    def show_game3(self):
        self.stack.setCurrentWidget(self.game3)

    def show_game4(self):
        self.stack.setCurrentWidget(self.game4)

    def show_game5(self):
        self.stack.setCurrentWidget(self.game5)

    def show_game6(self):
        self.stack.setCurrentWidget(self.game6)


