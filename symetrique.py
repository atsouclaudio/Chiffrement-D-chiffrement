# SymWindow.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton
from PySide6.QtCore import Qt

# Import de ta fenêtre César
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
        header.setStyleSheet("color: #4A148C; font-size: 18px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        self.combo = QComboBox()
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
        else:
            # Ici tu peux créer AESWindow ou DESWindow si tu les as
            # Exemple :
            # self.page = AESWindow()
            # ou self.page = DESWindow()
            #print(f"Fenêtre pour {choix} pas encore définie")
            if choix == "AES":
                self.page = AESWindow()  # Assure-toi d'avoir une classe AESWindow définieg
            return

        self.page.show()
        self.close()  # ferme la fenêtre actuelle pour basculer
