import tkinter as tk
from ttkbootstrap import Style

from controlers.libros_controler import Libros_controler
from centrar_ventana import centrar

class mainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Gestion")

        self.estilo= Style("darkly")
        
        # Agregamos un icono a la ventana principal
        self.imagenCarena = tk.PhotoImage(file = "image\\logocarena.png")
        self.imagenLibro = tk.PhotoImage(file = "image\\libro-abierto.png")
        self.root.iconphoto(True, self.imagenLibro)
        self.labelFondo=tk.Label(image= self.imagenCarena, master=self.root).grid(row=1, column=1, padx=170, pady=20)
        self.labelTitulo=tk.Label(text="Instituto Superior Dr. Carlos María Carena", master=self.root).grid(row=5, column=1)
        
        # Crea menubar
        self.menubar = tk.Menu(master=self.root)
        # Asigna menubar a root.
        root.config(menu=self.menubar)
        # Establece el tamaño de la ventana
        root.geometry(centrar(ancho=600, alto=400, app=self.root))
        # Fija el redimensionamiento de la ventana
        root.resizable(False, False)

        # Creamos los componentes del menu flotante
        self.alumnos_menu = tk.Menu(master=self.menubar, tearoff=False)
        self.carreras_menu = tk.Menu(master=self.menubar, tearoff=False)
        self.cursos_menu = tk.Menu(master=self.menubar, tearoff=False)
        # Añade al menu bar los submenu mediante la propiedad menu.
        self.menubar.add_cascade(label="Libros", menu=self.alumnos_menu)
        self.menubar.add_cascade(label="Empleados", menu=self.carreras_menu)
        self.menubar.add_cascade(label="Compras", menu=self.cursos_menu)
        # Añadir funcion al menu de alumnos_menu
        self.alumnos_menu.add_command(label="Libros", command= lambda: Libros_controler(self.root))
        self.alumnos_menu.add_separator()
        self.alumnos_menu.add_command(label="Salir", command=self.root.quit)
        # Añadir funcion al menu de carreras_menu
        self.carreras_menu.add_command(label="Empleados")
        self.carreras_menu.add_separator()
        self.carreras_menu.add_command(label="Salir", command=self.root.quit)
        # Añadir funcion al menu de alumnos_menu
        self.cursos_menu.add_command(label="Compras")
        self.cursos_menu.add_separator()
        self.cursos_menu.add_command(label="Salir", command=self.root.quit)
        

def main():
    root = tk.Tk()
    ventana= mainView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
