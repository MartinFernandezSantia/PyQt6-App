from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDateTime
from .components import labeled_widget


class TransactionWindow(QWidget):
    def __init__(self):
        super(TransactionWindow, self).__init__()

        self.resize(300, 200)
        self.setWindowTitle("Gestor de gastos")

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)

        # Primera fila
        self.nombre_transaccion = QComboBox()
        self.nombre_transaccion.addItems(["", "Opcion 2", "Opcion 3"])
        self.nombre_transaccion.setEditable(True)
        self.layout.addLayout(labeled_widget("Nombre de la transacción", self.nombre_transaccion))

        # Segunda fila
        self.cant_dinero = QDoubleSpinBox()
        self.cant_dinero.setRange(0, 999999999.99)
        self.layout.addLayout(labeled_widget("Cantidad de dinero", self.cant_dinero))

        # Tercera fila
        self.layout2 = QHBoxLayout()

        self.cantidad = QSpinBox()
        self.cantidad.setRange(1, 999999)
        self.layout2.addLayout(labeled_widget("Cantidad", self.cantidad))

        self.moneda = QComboBox()
        self.moneda.addItems(["AR$", "U$D"])
        self.layout2.addLayout(labeled_widget("Moneda", self.moneda))

        self.layout.addLayout(self.layout2)

        # # Cuarta fila
        self.fecha_hora = QDateTimeEdit(self, calendarPopup=True)
        self.fecha_hora.setDateTime(QDateTime.currentDateTime())
        self.fecha_hora.setDisplayFormat("dd/MM/yyyy | hh:mm AP")
        self.layout.addLayout(labeled_widget("Fecha y hora", self.fecha_hora))

        # # Quinta fila
        self.categoria = QComboBox()
        self.categoria.addItems(["Otros", "Servicios", "Tecnología", "Alimentación"])
        self.layout.addLayout(labeled_widget("Categoría", self.categoria))

        # # Sexta fila
        self.metodo_pago = QComboBox()
        self.metodo_pago.addItems(["Efectivo", "Debito", "Credito"])
        self.layout.addLayout(labeled_widget("Metodo de pago", self.metodo_pago))

        # # Ultima fila
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(3)

        self.button1 = QPushButton("+")
        self.button2 = QPushButton("-")
        self.button1.setStyleSheet(
            "background-color: #116233; font-size: 15px; color: white;"
        )
        self.button1.font()
        self.button2.setStyleSheet(
            "background-color: #841717; font-size: 15px; color: white;"
        )


        buttons_layout.addWidget(self.button1)
        buttons_layout.addWidget(self.button2)

        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)

