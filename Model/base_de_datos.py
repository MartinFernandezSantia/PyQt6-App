import sqlite3
import PyQt6
import PyQt6.QtCore


class BD:
    def __init__(self):
        try:
            self.con = sqlite3.connect("database.db")
        except:
            print("The database already exist")
        self.cursor = sqlite3.Cursor(self.con)

        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS transacciones(
                            Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            Nombre_transaccion VARCHAR(100) NOT NULL,   
                            Cantidad INT NOT NULL,
                            Dinero REAL NOT NULL,
                            Fecha_hora TEXT,
                            Categoria VARCHAR(50) NOT NULL,
                            Metodo_pago VARCHAR(50) NOT NULL,
                            Transaccion VARCHAR(20) NOT NULL
                        )""")