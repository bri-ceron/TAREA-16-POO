class Usuario:

    def __init__(
        self,
        identificacion,
        nombre,
        usuario,
        contrasena,
        rol="Cliente"
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    def convertir_a_diccionario(self):

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contraseña": self.contrasena,
            "rol": self.rol
        }

    @classmethod
    def desde_diccionario(cls, datos):

        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            usuario=datos["usuario"],
            contrasena=datos["contraseña"],
            rol=datos.get("rol", "Cliente")
        )