import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:

    def __init__(self, root):

        self.root = root

        self.root.state("normal")
        self.root.resizable(True, True)

        self.servicio = RestauranteServicio()

        self.mostrar_login()

    def limpiar_ventana(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):

        self.limpiar_ventana()

        LoginView(
            self.root,
            self.servicio,
            self.iniciar_sesion
        )

    def iniciar_sesion(self, usuario):

        self.limpiar_ventana()

        MainView(
            self.root,
            self.servicio,
            usuario,
            self.cerrar_sesion
        )

    def cerrar_sesion(self):

        self.mostrar_login()


def main():

    root = tk.Tk()

    Aplicacion(root)

    root.mainloop()


if __name__ == "__main__":
    main()