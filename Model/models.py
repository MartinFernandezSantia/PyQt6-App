from .base_de_datos import BD

class Model:
    def __init__(self):
        self.bd = BD()
        self.con = self.bd.con
        self.cursor = self.bd.cursor

    def guardar_datos(self, diccionario):
        self.cursor.execute("""
                                INSERT INTO transacciones(Nombre_transaccion, Cantidad, Dinero, Fecha_hora, Categoria, Metodo_pago, Transaccion)
                                VALUES(?,?,?,?,?,?,?)""", 
                                (
                                    diccionario["Nombre_transaccion"],
                                    diccionario["Cantidad"],
                                    diccionario["Dinero"], 
                                    diccionario["Fecha_hora"].toString("yyyy-MM-dd HH:mm:ss"), 
                                    diccionario["Categoria"], 
                                    diccionario["Metodo_pago"],
                                    diccionario["Transaccion"]
                                )
                            )
        self.con.commit()