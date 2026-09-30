# SULTAN RESTAURANT - TURKISH BBQ
Sistema de gestión de restaurante

Proyecto desarrollado en Python como continuación de la aplicación de gestión de restaurante realizada en la Semana 15 de la asignatura de Programación Orientada a Objetos (POO).

En esta Semana 16 se incorporó el manejo de eventos aplicado a la gestión de usuarios, permitiendo registrar, consultar, actualizar y eliminar usuarios mediante una interfaz gráfica desarrollada con Tkinter.

## 👩‍💻 Autora

Briggitte Cerón

## 📚 Semana 16
Tema

Manejo de eventos aplicado a la gestión de usuarios en restaurante_app

Objetivo

Implementar el manejo de eventos en la interfaz gráfica para mejorar la gestión de usuarios del sistema, manteniendo la arquitectura orientada a objetos y la persistencia de información mediante archivos JSON.

# 🍽️ Descripción del proyecto

SULTAN RESTAURANT - TURKISH BBQ es una aplicación de escritorio desarrollada en Python para gestionar diferentes procesos de un restaurante.

El sistema permite:

Iniciar sesión.
Gestionar usuarios.
Registrar clientes, empleados y administradores.
Consultar usuarios.
Actualizar información de usuarios.
Eliminar usuarios.
Gestionar productos.
Consultar productos.
Registrar ventas.
Consultar ventas.
Guardar la información en archivos JSON.

La aplicación utiliza una arquitectura modular basada en modelos, servicios e interfaces gráficas.

## 🆕 Funcionalidades implementadas en Semana 16
Gestión de usuarios

Se incorporó un sistema completo para administrar usuarios desde la interfaz gráfica.

Cada usuario contiene:

Identificación.
Nombre.
Usuario.
Contraseña.
Rol.

Los roles disponibles son:

Administrador
Empleado
Cliente

# 🎯 Manejo de eventos

Para cumplir con los requerimientos de la Semana 16 se implementaron diferentes eventos de Tkinter.

<<TreeviewSelect>>

Permite seleccionar un usuario desde la tabla y cargar automáticamente sus datos en el formulario.

<Return>

Permite registrar un usuario utilizando la tecla Enter.

<Escape>

Permite limpiar el formulario y cancelar la selección actual utilizando la tecla Esc.

<<ComboboxSelected>>

Permite reaccionar al cambio del rol seleccionado en el Combobox.

command=

Los botones continúan utilizando funciones callback mediante el atributo command, manteniendo la separación entre la interfaz y la lógica del sistema.

# 👥 Roles de usuario
Administrador

Puede acceder a la gestión de usuarios y realizar las operaciones administrativas disponibles.

Empleado

Puede utilizar las funcionalidades permitidas por la aplicación, pero no tiene acceso a la administración de usuarios.

Cliente

Representa a los clientes registrados en el sistema y no tiene acceso a la administración de usuarios.

# 🛡️ Control de eliminación

El sistema evita que el usuario actualmente autenticado sea eliminado accidentalmente desde la gestión de usuarios.

# 🏗️ Arquitectura del proyecto

El proyecto mantiene una estructura modular basada en Programación Orientada a Objetos:

restaurante_app15/
│
├── assets/
│   ├── icono.png
│   └── logo.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md

# 🧩 Tecnologías utilizadas
Python
Tkinter
Programación Orientada a Objetos (POO)
JSON
Visual Studio Code
Git
GitHub

# 📂 Modelos
Usuario

Representa a los usuarios registrados en el sistema y contiene información como identificación, nombre, usuario, contraseña y rol.

Producto

Representa los productos disponibles en el restaurante y controla información como código, nombre, precio, categoría y stock.

Venta

Representa las ventas realizadas y mantiene información relacionada con el usuario, producto, identificación de la venta y fecha.

⚙️ Servicios
ArchivoServicio

Se encarga de cargar y guardar información en archivos JSON.

RestauranteServicio

Contiene la lógica principal del sistema y se encarga de:

Gestionar usuarios.
Registrar usuarios.
Actualizar usuarios.
Eliminar usuarios.
Buscar usuarios.
Validar el inicio de sesión.
Gestionar productos.
Gestionar ventas.
Guardar y cargar información.

La interfaz gráfica delega estas operaciones al servicio para mantener una separación adecuada de responsabilidades.

🖥️ Interfaz gráfica

La interfaz fue desarrollada utilizando Tkinter.

La aplicación contiene:

Pantalla de inicio de sesión.
Logo del restaurante.
Menú principal.
Gestión de usuarios.
Gestión de productos.
Gestión de ventas.
Botón para cerrar sesión.

La aplicación utiliza los recursos visuales almacenados en la carpeta assets.

💾 Persistencia de datos

La información del sistema se almacena mediante archivos JSON:

datos/usuarios.json
datos/productos.json
datos/ventas.json

Esto permite conservar los datos después de cerrar y volver a ejecutar la aplicación.

▶️ Ejecución del proyecto

Para ejecutar la aplicación se debe abrir una terminal dentro de la carpeta principal del proyecto y utilizar:

python main.py

También puede ejecutarse desde Visual Studio Code.

🔐 Datos de acceso de prueba

Para ingresar al sistema se puede utilizar un usuario administrador registrado en el archivo usuarios.json.

Ejemplo:

Usuario: briggitte
Contraseña: 1234
Rol: Administrador
📝 Conclusión

En esta Semana 16 se amplió el sistema desarrollado anteriormente incorporando el manejo de eventos en la gestión de usuarios.

La aplicación mantiene el enfoque de Programación Orientada a Objetos y la separación entre modelos, servicios e interfaz gráfica. Además, la información se conserva mediante archivos JSON.

La implementación permite demostrar el uso de eventos de Tkinter como <<TreeviewSelect>>, <Return>, <Escape> y <<ComboboxSelected>>, junto con el uso de command= para las acciones de los botones.

De esta manera, SULTAN RESTAURANT - TURKISH BBQ continúa evolucionando como una aplicación modular para la gestión de un restaurante.