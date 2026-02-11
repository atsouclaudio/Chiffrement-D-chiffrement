import sys
from PySide6.QtWidgets import ( # type: ignore
    QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt # type: ignore
from PySide6.QtGui import QColor # type: ignore

# Import des deux pages
from symetrique import SymWindow
from asymetrique import AsymWindow

class StyledCard(QFrame):
    def __init__(self, title, description, callback, color="#F8F4FF"):
        super().__init__()
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 20px;
                padding: 20px;
            }}
            QLabel {{
                color: #4A148C;
            }}
        """)
        shadow = QGraphicsDropShadowEffect(blurRadiusw=15, xOffset=0, yOffset=5)
        shadow.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)
        title_label = QLabel(f"<b>{title}</b>")
        title_label.setAlignment(Qt.AlignCenter)
        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignCenter)

        btn = QPushButton(f"Choisir {title}")
        btn.setStyleSheet("""
            QPushButton {
                background-color: #7E57C2;
                color: white;
                border-radius: 10px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5E35B1;
            }
        """)
        btn.clicked.connect(callback)

        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addWidget(btn)

class ChoiceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choix du chiffrement")
        self.resize(400, 500)
        self.setStyleSheet("background-color: #EDE7F6;")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 40, 20, 20)
        main_layout.setSpacing(25)

        header = QLabel("Sélectionnez votre type de chiffrement")
        header.setStyleSheet("color: #311B92; font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        # Carte Symétrique
        sym_card = StyledCard(
            "Symétrique",
            "Un seul secret partagé pour chiffrer et déchiffrer.",
            self.open_sym
        )
        main_layout.addWidget(sym_card)

        # Carte Asymétrique
        asym_card = StyledCard(
            "Asymétrique",
            "Utilise une clé publique pour chiffrer et une clé privée pour déchiffrer.",
            self.open_asym
        )
        main_layout.addWidget(asym_card)

    def open_sym(self):
        self.sym_win = SymWindow()
        self.sym_win.show()

    def open_asym(self):
        self.asym_win = AsymWindow()
        self.asym_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChoiceWindow()
    window.show()
    sys.exit(app.exec())
