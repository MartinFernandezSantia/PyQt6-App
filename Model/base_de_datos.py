import sqlite3
import PyQt6
import PyQt6.QtCore




class Save:
    def __init__(self):
        try:
            self.con = sqlite3.connect("database.db")
        except:
            print("The database already exist")
        self.cursor = sqlite3.Cursor(self.con)
        d1 = {
               'Nombre_transaccion': 'Alquiler',
               'Dinero': 123546.43,
               'Cantidad': 1,
               'Moneda': 'AR$',
               'Fecha_hora': PyQt6.QtCore.QDateTime(2024, 4, 12, 23, 16, 39, 53),
               'Categoria': 'Otros',
               'Metodo_pago': 'Efectivo',
               'Transaccion': 'Ingreso'
                }
        self.cursor.execute("""CREATE TABLE IF NOT EXIST trnasacciones(
                        Id INT PRIMARY KEY 
                        Nombre_transaccion VARCHAR(100) NOT NULL   
                        Cantidad INT NOT NULL
                        Dinero REAL NOT NULL
                        Fecha_hora TEXT
                        Categoria VARCHAR(50) NOT NULL
                        Metodo_pago VARCHAR(50) NOT NULL
                        Transaccion VARCHAR(20) NOT NULL
                         
                            )
        """)
        
        d1['Fecha_hora'].toString("yyyy-MM-dd HH:mm:ss")
        self.con.close()
        
        
    def guardar_datos(self, d1):

        
        return
    
save = Save()
    