from datetime import datetime


class Venta:

    def __init__(
        self,
        id,
        usuario_id,
        producto_codigo,
        fecha=None
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo

        if fecha:
            self.fecha = fecha
        else:
            self.fecha = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha
        }

    @classmethod
    def desde_diccionario(cls, datos, id_por_defecto=None):

        return cls(
            id=datos.get("id", id_por_defecto),
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            fecha=datos.get("fecha")
        )