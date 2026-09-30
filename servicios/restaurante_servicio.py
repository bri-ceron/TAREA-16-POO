from pathlib import Path

from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta

from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):

        base = Path(__file__).resolve().parent.parent

        self.ruta_datos = base / "datos"

        self.ruta_usuarios = self.ruta_datos / "usuarios.json"
        self.ruta_productos = self.ruta_datos / "productos.json"
        self.ruta_ventas = self.ruta_datos / "ventas.json"

        self.usuarios = self.cargar_usuarios()
        self.productos = self.cargar_productos()
        self.ventas = self.cargar_ventas()

        self.mostrar_estado()

    # ==========================================================
    # ESTADO
    # ==========================================================

    def mostrar_estado(self):

        print("=" * 40)
        print("SULTAN RESTAURANT")
        print("TURKISH BBQ")
        print("=" * 40)

        print("RUTA DE PRODUCTOS:")
        print(self.ruta_productos)

        print(
            f"PRODUCTOS CARGADOS: {len(self.productos)}"
        )

        for producto in self.productos:

            print(
                producto.codigo,
                producto.nombre,
                producto.precio,
                producto.categoria,
                producto.stock
            )

        print(
            f"USUARIOS CARGADOS: {len(self.usuarios)}"
        )

        print(
            f"VENTAS CARGADAS: {len(self.ventas)}"
        )

        print("=" * 40)

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def cargar_usuarios(self):

        datos = ArchivoServicio.cargar(
            self.ruta_usuarios
        )

        return [
            Usuario.desde_diccionario(item)
            for item in datos
        ]

    def guardar_usuarios(self):

        datos = [
            usuario.convertir_a_diccionario()
            for usuario in self.usuarios
        ]

        ArchivoServicio.guardar(
            self.ruta_usuarios,
            datos
        )

    def listar_usuarios(self):

        return self.usuarios

    def buscar_usuario(self, identificacion):

        identificacion = str(
            identificacion
        ).strip()

        for usuario in self.usuarios:

            if str(
                usuario.identificacion
            ).strip() == identificacion:

                return usuario

        return None

    def validar_login(
        self,
        usuario,
        contrasena
    ):

        for persona in self.usuarios:

            if (
                persona.usuario == usuario
                and
                persona.contrasena == contrasena
            ):

                return persona

        return None

    def registrar_usuario(
        self,
        identificacion,
        nombre,
        usuario,
        contrasena,
        rol
    ):

        identificacion = str(
            identificacion
        ).strip()

        nombre = str(
            nombre
        ).strip()

        usuario = str(
            usuario
        ).strip()

        contrasena = str(
            contrasena
        ).strip()

        rol = str(
            rol
        ).strip()

        if not identificacion:

            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre:

            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not usuario:

            raise ValueError(
                "El usuario no puede estar vacío."
            )

        if not contrasena:

            raise ValueError(
                "La contraseña no puede estar vacía."
            )

        if not rol:

            raise ValueError(
                "Debe seleccionar un rol."
            )

        if rol not in [
            "Administrador",
            "Empleado",
            "Cliente"
        ]:

            raise ValueError(
                "El rol seleccionado no es válido."
            )

        if self.buscar_usuario(
            identificacion
        ):

            raise ValueError(
                "Ya existe un usuario con esa identificación."
            )

        for persona in self.usuarios:

            if persona.usuario == usuario:

                raise ValueError(
                    "Ya existe ese nombre de usuario."
                )

        nuevo_usuario = Usuario(
            identificacion,
            nombre,
            usuario,
            contrasena,
            rol
        )

        self.usuarios.append(
            nuevo_usuario
        )

        self.guardar_usuarios()

        return nuevo_usuario

    def actualizar_usuario(
        self,
        identificacion_original,
        nueva_identificacion,
        nombre,
        usuario,
        contrasena,
        rol
    ):

        usuario_obj = self.buscar_usuario(
            identificacion_original
        )

        if usuario_obj is None:

            raise ValueError(
                "El usuario no existe."
            )

        nueva_identificacion = str(
            nueva_identificacion
        ).strip()

        nombre = str(
            nombre
        ).strip()

        usuario = str(
            usuario
        ).strip()

        contrasena = str(
            contrasena
        ).strip()

        rol = str(
            rol
        ).strip()

        if not nueva_identificacion:

            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre:

            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not usuario:

            raise ValueError(
                "El usuario no puede estar vacío."
            )

        if not contrasena:

            raise ValueError(
                "La contraseña no puede estar vacía."
            )

        if not rol:

            raise ValueError(
                "Debe seleccionar un rol."
            )

        if rol not in [
            "Administrador",
            "Empleado",
            "Cliente"
        ]:

            raise ValueError(
                "El rol seleccionado no es válido."
            )

        otro_usuario = self.buscar_usuario(
            nueva_identificacion
        )

        if (
            otro_usuario is not None
            and
            otro_usuario is not usuario_obj
        ):

            raise ValueError(
                "La nueva identificación ya existe."
            )

        for persona in self.usuarios:

            if (
                persona is not usuario_obj
                and
                persona.usuario == usuario
            ):

                raise ValueError(
                    "Ya existe ese nombre de usuario."
                )

        identificacion_anterior = (
            usuario_obj.identificacion
        )

        usuario_obj.identificacion = (
            nueva_identificacion
        )

        usuario_obj.nombre = nombre

        usuario_obj.usuario = usuario

        usuario_obj.contrasena = contrasena

        usuario_obj.rol = rol

        # Actualizar referencias de ventas
        for venta in self.ventas:

            if str(
                venta.usuario_id
            ) == str(
                identificacion_anterior
            ):

                venta.usuario_id = (
                    nueva_identificacion
                )

        self.guardar_usuarios()

        self.guardar_ventas()

        return usuario_obj

    def eliminar_usuario(
        self,
        identificacion
    ):

        usuario_obj = self.buscar_usuario(
            identificacion
        )

        if usuario_obj is None:

            raise ValueError(
                "El usuario no existe."
            )

        self.usuarios.remove(
            usuario_obj
        )

        self.guardar_usuarios()

        return True

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def cargar_productos(self):

        datos = ArchivoServicio.cargar(
            self.ruta_productos
        )

        return [
            Producto.desde_diccionario(item)
            for item in datos
        ]

    def guardar_productos(self):

        datos = [
            producto.convertir_a_diccionario()
            for producto in self.productos
        ]

        ArchivoServicio.guardar(
            self.ruta_productos,
            datos
        )

    def listar_productos(self):

        return self.productos

    def buscar_producto(self, codigo):

        codigo = str(
            codigo
        ).strip()

        for producto in self.productos:

            if str(
                producto.codigo
            ).strip() == codigo:

                return producto

        return None

    def registrar_producto(
        self,
        codigo,
        nombre,
        precio,
        categoria,
        stock
    ):

        codigo = str(
            codigo
        ).strip()

        nombre = str(
            nombre
        ).strip()

        categoria = str(
            categoria
        ).strip()

        if not codigo:

            raise ValueError(
                "El código no puede estar vacío."
            )

        if not nombre:

            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not categoria:

            raise ValueError(
                "La categoría no puede estar vacía."
            )

        if self.buscar_producto(
            codigo
        ):

            raise ValueError(
                "Ya existe un producto con ese código."
            )

        try:

            precio = float(
                precio
            )

        except ValueError:

            raise ValueError(
                "El precio debe ser numérico."
            )

        try:

            stock = int(
                stock
            )

        except ValueError:

            raise ValueError(
                "El stock debe ser un número entero."
            )

        if precio < 0:

            raise ValueError(
                "El precio no puede ser negativo."
            )

        if stock < 0:

            raise ValueError(
                "El stock no puede ser negativo."
            )

        nuevo_producto = Producto(
            codigo,
            nombre,
            precio,
            categoria,
            stock
        )

        self.productos.append(
            nuevo_producto
        )

        self.guardar_productos()

        return nuevo_producto

    def actualizar_producto(
        self,
        codigo_original,
        nuevo_codigo,
        nombre,
        precio,
        categoria,
        stock
    ):

        producto_obj = self.buscar_producto(
            codigo_original
        )

        if producto_obj is None:

            raise ValueError(
                "El producto no existe."
            )

        nuevo_codigo = str(
            nuevo_codigo
        ).strip()

        nombre = str(
            nombre
        ).strip()

        categoria = str(
            categoria
        ).strip()

        if not nuevo_codigo:

            raise ValueError(
                "El código no puede estar vacío."
            )

        if not nombre:

            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not categoria:

            raise ValueError(
                "La categoría no puede estar vacía."
            )

        otro_producto = self.buscar_producto(
            nuevo_codigo
        )

        if (
            otro_producto is not None
            and
            otro_producto is not producto_obj
        ):

            raise ValueError(
                "El nuevo código ya existe."
            )

        try:

            precio = float(
                precio
            )

        except ValueError:

            raise ValueError(
                "El precio debe ser numérico."
            )

        try:

            stock = int(
                stock
            )

        except ValueError:

            raise ValueError(
                "El stock debe ser un número entero."
            )

        if precio < 0:

            raise ValueError(
                "El precio no puede ser negativo."
            )

        if stock < 0:

            raise ValueError(
                "El stock no puede ser negativo."
            )

        codigo_anterior = (
            producto_obj.codigo
        )

        producto_obj.codigo = (
            nuevo_codigo
        )

        producto_obj.nombre = (
            nombre
        )

        producto_obj.precio = (
            precio
        )

        producto_obj.categoria = (
            categoria
        )

        producto_obj.stock = (
            stock
        )

        # Actualizar referencias de ventas
        for venta in self.ventas:

            if str(
                venta.producto_codigo
            ) == str(
                codigo_anterior
            ):

                venta.producto_codigo = (
                    nuevo_codigo
                )

        self.guardar_productos()

        self.guardar_ventas()

        return producto_obj

    def eliminar_producto(
        self,
        codigo
    ):

        producto_obj = self.buscar_producto(
            codigo
        )

        if producto_obj is None:

            raise ValueError(
                "El producto no existe."
            )

        self.productos.remove(
            producto_obj
        )

        self.guardar_productos()

        return True

    # ==========================================================
    # VENTAS
    # ==========================================================

    def cargar_ventas(self):

        datos = ArchivoServicio.cargar(
            self.ruta_ventas
        )

        ventas = []

        for posicion, item in enumerate(
            datos,
            start=1
        ):

            venta = Venta.desde_diccionario(
                item,
                id_por_defecto=posicion
            )

            ventas.append(
                venta
            )

        return ventas

    def listar_ventas(self):

        return self.ventas

    def guardar_ventas(self):

        datos = [
            venta.convertir_a_diccionario()
            for venta in self.ventas
        ]

        ArchivoServicio.guardar(
            self.ruta_ventas,
            datos
        )

    def generar_id_venta(self):

        if not self.ventas:

            return 1

        ids = []

        for venta in self.ventas:

            try:

                ids.append(
                    int(venta.id)
                )

            except (
                ValueError,
                TypeError
            ):

                pass

        if not ids:

            return 1

        return max(ids) + 1

    def registrar_venta(
        self,
        usuario_id,
        producto_codigo
    ):

        usuario = self.buscar_usuario(
            usuario_id
        )

        if usuario is None:

            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto = self.buscar_producto(
            producto_codigo
        )

        if producto is None:

            raise ValueError(
                "El producto seleccionado no existe."
            )

        if not producto.disponible:

            raise ValueError(
                "El producto está agotado."
            )

        producto.vender()

        nueva_venta = Venta(
            id=self.generar_id_venta(),
            usuario_id=usuario.identificacion,
            producto_codigo=producto.codigo
        )

        self.ventas.append(
            nueva_venta
        )

        self.guardar_productos()

        self.guardar_ventas()

        return nueva_venta