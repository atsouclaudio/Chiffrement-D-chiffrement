import sys, json
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,QTextEdit, QLabel, QFrame, QLineEdit, QPushButton, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt, QUrl, QUrlQuery
from PySide6.QtGui import QColor 
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest


class StyledCard(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: #F8F4FF;
                border-radius: 20px;
                padding: 10px;
            }
        """)
        shadow = QGraphicsDropShadowEffect(blurRadius=15, xOffset=0, yOffset=5)
        shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(shadow)

class AESWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chiffrement AES")
        self.resize(380, 650)
        self.setStyleSheet("background-color: #7E57C2;")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 40, 20, 20)
        main_layout.setSpacing(15)

        # --- En(tête) ---
        header_label = QLabel("Chiffrement AES")
        header_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)

        # --- Entre le text a coder ou à décoder ---
        input_card = StyledCard()
        input_layout = QVBoxLayout(input_card)
        input_title = QLabel("Texte à traiter")
        input_title.setStyleSheet("color: #5E35B1; font-weight: bold;")
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Entrez votre texte ici...")
        self.input_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #D1C4E9;
                border-radius: 10px;
                background: white;
                padding: 10px;
            }
        """)
        input_layout.addWidget(input_title)
        input_layout.addWidget(self.input_text)
        main_layout.addWidget(input_card)