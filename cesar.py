import sys
from PySide6.QtWidgets import ( # type: ignore
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLabel, QFrame, QLineEdit, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt # type: ignore
from PySide6.QtGui import QColor # type: ignore

class StyledCard(QFrame):
    """Crée un conteneur avec un fond blanc et des coins arrondis."""
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: #F8F4FF;
                border-radius: 20px;
                padding: 10px;
            }
        """)
        # Effet d'ombre légère pour une meilleur expérience utilisateur
        shadow = QGraphicsDropShadowEffect(blurRadius=15, xOffset=0, yOffset=5)
        shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(shadow)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chiffrement de César")
        self.resize(380, 650)
        self.setStyleSheet("background-color: #7E57C2;") # Fond violet principal

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 40, 20, 20)
        main_layout.setSpacing(15)

        # --- HEADER ---
        header_label = QLabel("Chiffrement de César")
        header_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)

        # --- SECTION MODE ---
        mode_card = StyledCard()
        mode_layout = QHBoxLayout(mode_card)
        mode_label = QLabel("Mode: <b>Encoder</b>")
        mode_label.setStyleSheet("color: #5E35B1; font-size: 16px;")
        mode_layout.addWidget(mode_label)
        main_layout.addWidget(mode_card)

        # --- SECTION INPUT ---
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

        # --- SECTION DÉCALAGE ---
        shift_card = StyledCard()
        shift_layout = QVBoxLayout(shift_card)
        shift_title = QLabel("Décalage")
        shift_title.setStyleSheet("color: #5E35B1; font-weight: bold;")
        
        self.shift_input = QLineEdit("3")
        self.shift_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #D1C4E9;
                border-radius: 10px;
                background: white;
                height: 40px;
                padding-left: 10px;
            }
        """)
        
        shift_layout.addWidget(shift_title)
        shift_layout.addWidget(self.shift_input)
        main_layout.addWidget(shift_card)

        # --- SECTION RÉSULTAT ---
        result_card = StyledCard()
        result_layout = QVBoxLayout(result_card)
        result_title = QLabel("Résultat")
        result_title.setStyleSheet("color: #5E35B1; font-weight: bold;")
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Le résultat apparaîtra ici...")
        self.output_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #D1C4E9;
                border-radius: 10px;
                background: #F3E5F5;
                padding: 10px;
                color: #7B1FA2;
            }
        """)
        
        result_layout.addWidget(result_title)
        result_layout.addWidget(self.output_text)
        main_layout.addWidget(result_card)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())