import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDateTime

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("My App")

        # Layout principal
        layout = QVBoxLayout()        
        layout.setSpacing(20)

        # Primera fila
        layout2 = QVBoxLayout()
        layout2.setSpacing(0)

        self.nombre_transaccion = QComboBox()
        self.nombre_transaccion.addItems(["", "Opcion 2", "Opcion 3"])
        self.nombre_transaccion.setEditable(True)

        self.nombre_transaccion_label = QLabel("Nombre de la transacción")

        layout2.addWidget(self.nombre_transaccion_label)
        layout2.addWidget(self.nombre_transaccion)
        
        # Segunda fila
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QHBoxLayout()

        layout3.setSpacing(0)
        layout4.setSpacing(0)

        self.cant_dinero = QDoubleSpinBox()
        self.cant_dinero.setRange(0, 999999999.99)

        self.cant_dinero_label = QLabel("Cantidad de dinero")

        self.moneda = QComboBox()
        self.moneda.addItems(["AR$", "U$D"])

        self.moneda_label = QLabel("Moneda")

        layout3.addWidget(self.cant_dinero_label)
        layout3.addWidget(self.cant_dinero)

        layout4.addWidget(self.moneda_label)
        layout4.addWidget(self.moneda)

        layout5.addLayout(layout3)
        layout5.addLayout(layout4)

        # Tercera fila
        layout6 = QVBoxLayout()
        layout6.setSpacing(0)

        self.cantidad_label = QLabel("Cantidad")
        self.cantidad = QSpinBox()
        self.cantidad.setRange(1, 999999)

        layout6.addWidget(self.cantidad_label)
        layout6.addWidget(self.cantidad)

        # Cuarta fila
        layout7 = QVBoxLayout()
        layout7.setSpacing(0)

        self.fecha_hora_label = QLabel("Fecha y hora")
        self.fecha_hora = QDateTimeEdit(self, calendarPopup=True)
        self.fecha_hora.setDateTime(QDateTime.currentDateTime())
        self.fecha_hora.setDisplayFormat("dd/MM/yyyy | hh:mm AP")

        layout7.addWidget(self.fecha_hora_label)
        layout7.addWidget(self.fecha_hora)

        # Quinta fila

        # Ultima fila
        button = QPushButton("Print")
        button.clicked.connect(self.print_stuff)

        # Asignacion de widgets y filas a layout principal
        layout.addLayout(layout2)
        layout.addLayout(layout5)
        layout.addLayout(layout6)
        layout.addLayout(layout7)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def print_stuff(self):
        print(self.nombre_transaccion_input.currentText())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()