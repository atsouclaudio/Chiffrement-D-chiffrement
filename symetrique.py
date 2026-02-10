# SymWindow.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton
from PySide6.QtCore import Qt

# Import des fenêtres de chiffrement
from AES import AESWindow
from DES import DESWindow
from cesar import CesarWindow  

class SymWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chiffrement Symétrique")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #F3E5F5;")

        layout = QVBoxLayout(self)

        layout.addStretch()

        header = QLabel("Choisissez un algorithme symétrique")
        header.setStyleSheet("color: #4A148C; font-size: 30px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        self.combo = QComboBox()
        self.combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #D1C4E9;
                border-radius: 10px;
                padding: 5px 10px;
                font-size: 16px;}
                                 """)
        self.combo.addItems(["César", "AES", "DES"])
        layout.addWidget(self.combo, alignment=Qt.AlignCenter)

        self.button = QPushButton("Valider")
        self.button.clicked.connect(self.on_validate)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)

        layout.addStretch()

    def on_validate(self):
        choix = self.combo.currentText()
        if choix == "César":
            self.page = CesarWindow()   # Ouvre la fenêtre César
        #else:
            # Ici tu peux créer AESWindow ou DESWindow si tu les as
            # Exemple :
            # self.page = AESWindow()
            # ou self.page = DESWindow()
            #print(f"Fenêtre pour {choix} pas encore définie")
        if choix == "AES":
            self.page = AESWindow()  # Assure-toi d'avoir une classe AESWindow définieg
        if choix == "DES":
            self.page = DESWindow()  # Assure-toi d'avoir une classe DESWindow définie
        if choix == "":
            return

        self.page.show()
        self.close()  # ferme la fenêtre actuelle pour basculer
