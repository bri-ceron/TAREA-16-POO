import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


class LoginView:

    def __init__(self, root, servicio, iniciar_sesion):

        self.root = root
        self.servicio = servicio
        self.iniciar_sesion = iniciar_sesion

        self.root.title("SULTAN RESTAURANT - Login")
        self.root.geometry("500x550")
        self.root.resizable(True, True)

        base = Path(__file__).resolve().parent.parent

        ruta_logo = base / "assets" / "logo.png"
        ruta_icono = base / "assets" / "icono.png"

        try:
            self.logo = tk.PhotoImage(file=ruta_logo)

            while (
                self.logo.width() > 220
                or self.logo.height() > 120
            ):
                self.logo = self.logo.subsample(2, 2)

        except Exception:
            self.logo = None

        try:
            self.icono = tk.PhotoImage(file=ruta_icono)

            self.root.iconphoto(
                True,
                self.icono
            )

        except Exception:
            self.icono = None

        self.crear_interfaz()

    def crear_interfaz(self):

        contenedor = tk.Frame(
            self.root,
            bg="white"
        )

        contenedor.pack(
            expand=True,
            fill="both",
            padx=30,
            pady=20
        )

        if self.logo:

            etiqueta_logo = tk.Label(
                contenedor,
                image=self.logo,
                bg="white"
            )

            etiqueta_logo.pack(
                pady=(0, 10)
            )

        titulo = tk.Label(
            contenedor,
            text="SULTAN RESTAURANT",
            font=("Arial", 22, "bold"),
            bg="white"
        )

        titulo.pack(
            pady=(5, 0)
        )

        subtitulo_restaurante = tk.Label(
            contenedor,
            text="TURKISH BBQ",
            font=("Arial", 14, "bold"),
            bg="white"
        )

        subtitulo_restaurante.pack(
            pady=(0, 10)
        )

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Arial", 12, "bold"),
            bg="white"
        )

        subtitulo.pack(
            pady=(0, 25)
        )

        fila_usuario = tk.Frame(
            contenedor,
            bg="white"
        )

        fila_usuario.pack(
            fill="x",
            pady=8
        )

        etiqueta_usuario = tk.Label(
            fila_usuario,
            text="Usuario:",
            font=("Arial", 11, "bold"),
            bg="white",
            width=12,
            anchor="w"
        )

        etiqueta_usuario.pack(
            side="left"
        )

        self.entry_usuario = tk.Entry(
            fila_usuario,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.entry_usuario.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=6
        )

        fila_clave = tk.Frame(
            contenedor,
            bg="white"
        )

        fila_clave.pack(
            fill="x",
            pady=8
        )

        etiqueta_clave = tk.Label(
            fila_clave,
            text="Contraseña:",
            font=("Arial", 11, "bold"),
            bg="white",
            width=12,
            anchor="w"
        )

        etiqueta_clave.pack(
            side="left"
        )

        self.entry_clave = tk.Entry(
            fila_clave,
            font=("Arial", 11),
            show="*",
            relief="solid",
            bd=1
        )

        self.entry_clave.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=6
        )

        boton = tk.Button(
            contenedor,
            text="INICIAR SESIÓN",
            font=("Arial", 11, "bold"),
            bg="#C49A3A",
            fg="white",
            activebackground="#A9822E",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.validar_login
        )

        boton.pack(
            pady=25,
            ipadx=25,
            ipady=8
        )

        self.entry_usuario.focus()

        self.root.bind(
            "<Return>",
            self.evento_enter
        )

    def evento_enter(self, event=None):

        if (
            self.entry_usuario.winfo_exists()
            and
            self.entry_clave.winfo_exists()
        ):

            self.validar_login()

    def validar_login(self):

        if not self.entry_usuario.winfo_exists():
            return

        if not self.entry_clave.winfo_exists():
            return

        usuario = self.entry_usuario.get().strip()

        clave = self.entry_clave.get().strip()

        if not usuario or not clave:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )

            return

        persona = self.servicio.validar_login(
            usuario,
            clave
        )

        if persona:

            self.root.unbind(
                "<Return>"
            )

            self.iniciar_sesion(
                persona
            )

        else:

            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )