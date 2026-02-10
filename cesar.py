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

class CesarWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chiffrement de César")
        self.resize(380, 650)
        self.setStyleSheet("background-color: #7E57C2;")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 40, 20, 20)
        main_layout.setSpacing(15)

        # --- En(tête) ---
        header_label = QLabel("Chiffrement de César")
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

        # --- le décalage 3 pour le code de césar ---
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

        # --- BUTTONS pour choisir le mode ---
        button_layout = QHBoxLayout()
        self.encode_button = QPushButton("Encoder")
        self.decode_button = QPushButton("Décoder")
        for btn in (self.encode_button, self.decode_button):
            btn.setStyleSheet("background-color: #5E35B1; color: white; border-radius: 10px; height: 40px;")
            button_layout.addWidget(btn)
        main_layout.addLayout(button_layout)

        # --- Voici le RESULTAT ---
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

        # --- NETWORK ---
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.RecupReponseEtAffichage)
        self.encode_button.clicked.connect(lambda: self.appelDeLApi("encode"))
        self.decode_button.clicked.connect(lambda: self.appelDeLApi("decode"))

    # def appelDeLApi(self, mode):
    #     text = self.input_text.toPlainText()
    #     shift = self.shift_input.text()
    #     url = QUrl(f"http://127.0.0.1:8000/api/cipher/?text={text}&shift={shift}&mode={mode}")
    #     request = QNetworkRequest(url)
    #     self.manager.get(request)

    def appelDeLApi(self, mode): 
        text = self.input_text.toPlainText() 
        shift = self.shift_input.text() 
        url = QUrl("http://127.0.0.1:8000/api/cipher/") 
        query = QUrlQuery() 
        query.addQueryItem("text", text) 
        query.addQueryItem("shift", shift) 
        query.addQueryItem("mode", mode) 
        url.setQuery(query) 
        request = QNetworkRequest(url) 
        self.manager.get(request)

    def RecupReponseEtAffichage(self, reply):
        data = reply.readAll().data()
        result = json.loads(data.decode("utf-8"))
        self.output_text.setPlainText(result["result"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CesarWindow()
    window.show()
    sys.exit(app.exec())

