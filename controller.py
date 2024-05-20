from PyQt6.QtWidgets import QApplication
from Views.transactions_form import TransactionWindow
from Views.menu import Menu
from Model.models import Model

class Controller:
    def __init__(self):
        self.app = QApplication([])
        self.app.setStyle("fusion")
        self.app.setApplicationName("Gestor de gastos")

        self.model = Model()
        self.menu = Menu()

        self.transaction_window = TransactionWindow()
        
        # Señales del menu
        self.menu.boton_transacciones.clicked.connect(lambda: self.new_window(self.transaction_window))

        # Connect signals to slots
        self.transaction_window.button1.clicked.connect(lambda:self.new_transaction("Ingreso"))
        self.transaction_window.button2.clicked.connect(lambda:self.new_transaction("Egreso"))

        self.menu.show()
        self.app.exec()

    def new_transaction(self, transaction: str):
        """" Toma los datos ingresados por el usuario en la TransactionWindow y los imprime
        """
        data = {
            "Nombre_transaccion": self.transaction_window.nombre_transaccion.currentText(),
            "Dinero": self.transaction_window.cant_dinero.value(),
            "Cantidad": self.transaction_window.cantidad.value(),
            "Moneda": self.transaction_window.moneda.currentText(),
            "Fecha_hora": self.transaction_window.fecha_hora.dateTime(),
            "Categoria": self.transaction_window.categoria.currentText(),
            "Metodo_pago": self.transaction_window.metodo_pago.currentText(),
            "Transaccion": transaction
        }
        self.model.guardar_datos(data)

    def new_window(self, window):
        window.show()

if __name__ == "__main__":
    controller = Controller()
