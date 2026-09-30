class Producto:

    def __init__(self, codigo, nombre, precio, categoria, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria
        self.stock = int(stock)

    @property
    def disponible(self):
        return self.stock > 0

    @property
    def estado(self):
        if self.stock > 0:
            return "Disponible"
        return "Agotado"

    def vender(self):
        if self.stock <= 0:
            return False

        self.stock -= 1
        return True

    def convertir_a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            categoria=datos["categoria"],
            stock=datos["stock"]
        )