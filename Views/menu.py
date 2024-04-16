from PyQt6.QtWidgets import *

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()

        # Configuraciones de la ventana

        # Botones
        self.boton_transacciones = QPushButton("Nueva transacción")

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.boton_transacciones)

        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

