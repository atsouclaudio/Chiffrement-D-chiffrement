from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt

class SymWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chiffrement Symétrique")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #F3E5F5;")

        layout = QVBoxLayout(self)

        # Ajout d'un espace flexible en haut
        layout.addStretch()

        header = QLabel("Choisissez un algorithme symétrique")
        header.setStyleSheet("color: #4A148C; font-size: 18px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        self.combo = QComboBox()
        self.combo.addItems(["César", "AES", "DES"])
        self.combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #AB47BC;
                border-radius: 10px;
                padding: 8px;
                background: green;
                font-size: 14px;
            }
            QComboBox:hover {
                border: 1px solid #7E57C2;
            }
        """)
        layout.addWidget(self.combo, alignment=Qt.AlignCenter)

        # Ajout d'un espace flexible en bas

        layout.addStretch()
