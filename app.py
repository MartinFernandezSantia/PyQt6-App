import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDateTime


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Gestor de gastos")
        self.resize(300, 200)

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)

        # Primera fila
        self.nombre_transaccion = QComboBox()
        self.nombre_transaccion.addItems(["", "Opcion 2", "Opcion 3"])
        self.nombre_transaccion.setEditable(True)
        self.labeled_widget(
            "Nombre de la transacción", self.nombre_transaccion, self.layout
        )

        # Segunda fila
        self.cant_dinero = QDoubleSpinBox()
        self.cant_dinero.setRange(0, 999999999.99)
        self.labeled_widget("Cantidad de dinero", self.cant_dinero, self.layout)

        # Tercera fila
        self.layout2 = QHBoxLayout()

        self.cantidad = QSpinBox()
        self.cantidad.setRange(1, 999999)
        self.labeled_widget("Cantidad", self.cantidad, self.layout2)

        self.moneda = QComboBox()
        self.moneda.addItems(["AR$", "U$D"])
        self.labeled_widget("Moneda", self.moneda, self.layout2)

        self.layout.addLayout(self.layout2)

        # # Cuarta fila
        self.fecha_hora = QDateTimeEdit(self, calendarPopup=True)
        self.fecha_hora.setDateTime(QDateTime.currentDateTime())
        self.fecha_hora.setDisplayFormat("dd/MM/yyyy | hh:mm AP")
        self.labeled_widget("Fecha y hora", self.fecha_hora, self.layout)

        # # Quinta fila
        self.categoria = QComboBox()
        self.categoria.addItems(["Otros", "Servicios", "Tecnología", "Alimentación"])
        self.labeled_widget("Categoría", self.categoria, self.layout)

        # # Sexta fila
        self.metodo_pago = QComboBox()
        self.metodo_pago.addItems(["Efectivo", "Debito", "Credito"])
        self.labeled_widget("Metodo de pago", self.metodo_pago, self.layout)

        # # Ultima fila
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(3)

        button1 = QPushButton("+")
        button2 = QPushButton("-")
        button1.setStyleSheet(
            "background-color: #116233; font-size: 15px; color: white;"
        )
        button1.font()
        button2.setStyleSheet(
            "background-color: #841717; font-size: 15px; color: white;"
        )

        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)

        self.layout.addLayout(buttons_layout)
        # button.clicked.connect(self.print_stuff)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def labeled_widget(self, label_text, widget, parent_layout):
        new_layout = QVBoxLayout()
        new_layout.setSpacing(0)

        label = QLabel(label_text)

        new_layout.addWidget(label)
        new_layout.addWidget(widget)

        parent_layout.addLayout(new_layout)


app = QApplication(sys.argv)
app.setStyle("fusion")

window = MainWindow()
window.show()

app.exec()
