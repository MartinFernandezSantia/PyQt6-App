import sys
from Views.transactions_form import TransactionWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject



class Controller(QObject):
    """Controla las interacciones entre la vista y el modelo. Responde a las interacciones 
    del usuario, y actualiza la vista o el modelo cuando sea necesario.
    """
    def __init__(self, view, model):
        super().__init__()

        self.view = view
        self.model = model

        view.button1.clicked.connect(lambda:self.new_transaction("Ingreso"))
        view.button2.clicked.connect(lambda:self.new_transaction("Egreso"))

        self.view.show()

    def new_transaction(self, transaction):
        data = {
            "Nombre_transaccion": self.view.nombre_transaccion.currentText(),
            "Dinero": self.view.cant_dinero.value(),
            "Cantidad": self.view.cantidad.value(),
            "Moneda": self.view.moneda.currentText(),
            "Fecha_hora": self.view.fecha_hora.dateTime(),
            "Categoria": self.view.categoria.currentText(),
            "Metodo_pago": self.view.metodo_pago.currentText(),
            "Transaccion": transaction
        }

        print(data)

app = QApplication(sys.argv)
app.setStyle("fusion")
view = TransactionWindow()
window = Controller(view=view, model=None)
app.exec()
