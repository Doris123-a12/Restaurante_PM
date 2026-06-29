# Clase cliente

class Cliente:
    def __init__(self, nombre: str, edad: int, telefono: str, vip: bool):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.vip = vip

    def __str__(self):
        tipo = "Cliente VIP" if self.vip else "Cliente Normal"
        return f"{self.nombre} | Edad: {self.edad} | Tel: {self.telefono} | {tipo}"