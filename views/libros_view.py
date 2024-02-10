#views.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from ttkbootstrap import Style
from centrar_ventana import centrar
import sqlite3


class Libros_view():
    def __init__(self, root) -> None:
        """constructor de la clase.

        Args:
            root (object): ventana pasada como parametro, sobre la cual se creara la ventana modal.
        """
        self.root = root
        # self.root.title('Gestión de Nombres')
        self.estilo=Style("darkly")
        self.ventana_modal= tk.Toplevel(self.root)
        self.ventana_modal.title("Gestion de Libros")
        self.ventana_modal.geometry(centrar(alto=520, ancho=640, app=self.root))
        self.ventana_modal.resizable(False, False)
        # Hacer que la ventana modal sea transitoria y modal
        self.ventana_modal.transient(self.root)
        # Bloquea el enfoque en la ventana modal
        self.ventana_modal.grab_set()

        #Define el Nombre y el ancho en píxeles de las columnas.(625 px en total)
        columns = {'Id': 25, 'Autor': 120, 'Título': 300, 'Fecha Publicación': 110, 'Páginas': 70}
        self.treeview = ttk.Treeview(self.ventana_modal, columns=tuple(columns.keys()), show='headings', height=14, selectmode='browse')
        #Define las cabeceras
        for clave, valor in columns.items():
            self.treeview.heading(clave, text=clave)
            self.treeview.column(clave, width=valor)

        self.treeview.grid(row=0, column=0, sticky='nsew')

        #Añade un barra lateral de scroll (enrollado).
        scrollbar = ttk.Scrollbar(self.ventana_modal, orient=tk.VERTICAL, command=self.treeview.yview)
        #self.treeview.configure(yscroll=scrollbar.set)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.frame3 = ttk.Frame(self.ventana_modal, border=0)
        self.frame3.grid(padx=5, pady=5, row=2, column=0, sticky='nsesw')

        self.buttonAdd = ttk.Button(self.frame3, text='Añadir')
        self.buttonAdd.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.buttonUpdate = ttk.Button(self.frame3, text='Actualizar')
        self.buttonUpdate.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.buttonRemove = ttk.Button(self.frame3, text='Eliminar')
        self.buttonRemove.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.buttonExit = ttk.Button(self.frame3, text='Salir')
        self.buttonExit.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.frame4 = ttk.Frame(self.ventana_modal, border=1, relief='groove')
        self.frame4.grid(padx=5, pady=5, row=3, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        

        # BUSCADOR DE DATOS ------------------------------------------------------------------------------------>
        # Barra superior donde ingresamos el titulo del libro a buscar.
        self.textvarBuscador = tk.StringVar()
        self.labelBuscador = tk.Label(self.frame4, text='Titulo Libro')
        self.labelBuscador.grid(column=0, row=0,padx=5,pady=5)
        self.entryBuscador = tk.Entry(self.frame4, textvariable=self.textvarBuscador, width=50)
        self.entryBuscador.grid(column=1, row=0,padx=5,pady=5)
        self.botonBuscador =tk.Button(self.frame4, text="Buscar")
        self.botonBuscador.grid(column=2, row=0,padx=5,pady=5)
        self.botonBuscador1 =tk.Button(self.frame4, text="Limpiar")
        self.botonBuscador1.grid(column=3, row=0,padx=5,pady=5)
        #, command=lambda: self.limpiar_campos()
        #, command=lambda: self.buscar_datos(self.textvarBuscador, self.textvarBuscadorId, 
        # self.textvarBuscadorAutor, self.textvarBuscadorTitulo, self.textvarBuscadorFecha, self.textvarBuscadorPaginas)
        
        # ID muestra
        self.textvarBuscadorId = tk.StringVar()
        self.labelBuscador2 = tk.Label(self.frame4, text='ID: ')
        self.labelBuscador2.grid(column=0, row=1,padx=5,pady=5)
        self.entryBuscador2 = tk.Entry(self.frame4, textvariable=self.textvarBuscadorId, state="disabled", width=8)
        self.entryBuscador2.grid(column=1, row=1,padx=5,pady=5)

        # Autor
        self.textvarBuscadorAutor = tk.StringVar()
        self.labelBuscador3 = tk.Label(self.frame4, text='Autor: ')
        self.labelBuscador3.grid(column=0, row=2,padx=5,pady=5)
        self.entryBuscador3 = tk.Entry(self.frame4, textvariable=self.textvarBuscadorAutor, state="disabled", width=40)
        self.entryBuscador3.grid(column=1, row=2, padx=5, pady=5)
        
        # Titulo
        self.textvarBuscadorTitulo = tk.StringVar()
        self.labelBuscador3 = tk.Label(self.frame4, text='Titulo: ')
        self.labelBuscador3.grid(column=0, row=3,padx=5,pady=5)
        self.entryBuscador3 = tk.Entry(self.frame4, textvariable=self.textvarBuscadorTitulo, state="disabled", width=40)
        self.entryBuscador3.grid(column=1, row=3,padx=5,pady=5)
        
        # Fechas
        self.textvarBuscadorFecha = tk.StringVar()
        self.labelBuscador3 = tk.Label(self.frame4, text='Fecha: ')
        self.labelBuscador3.grid(column=0, row=4,padx=5,pady=5)
        self.entryBuscador3 = tk.Entry(self.frame4, textvariable=self.textvarBuscadorFecha, state="disabled", width=40)
        self.entryBuscador3.grid(column=1, row=4,padx=5,pady=5)
        
        # Paginas
        self.textvarBuscadorPaginas = tk.StringVar()
        self.labelBuscador3 = tk.Label(self.frame4, text='Paginas: ')
        self.labelBuscador3.grid(column=0, row=5,padx=5,pady=5)
        self.entryBuscador3 = tk.Entry(self.frame4, textvariable=self.textvarBuscadorPaginas, state="disabled", width=40)
        self.entryBuscador3.grid(column=1, row=5,padx=5,pady=5)

        #Barra nombre tabla
        statusbar = tk.Label(self.frame4, text='Tabla Libros')
        statusbar.grid(column=4,row=0,padx=5,pady=5)



    
    # self.textvarBuscador, self.textvarBuscadorId, self.textvarBuscadorAutor, self.textvarBuscadorTitulo, self.textvarBuscadorFecha, self.textvarBuscadorPaginas
    

    def getCursorId(self) -> str:
        """getCursorId: Obtiene el valor de Id del cursor.

        Returns:
            str: Devuelve el valor de Id del cursor.
        """
        selectedLbData = self.treeview.selection()[0]
        id = self.treeview.item(selectedLbData)['values'][0]
        return id

    def getCursorAutor(self) -> str:
        """getCursorNombre: Obtiene el valor de Autor del cursor.

        Returns:
            str: Devuelve el valor de Autor del cursor.
        """
        selectedLbData = self.treeview.selection()[0]
        Nombre = self.treeview.item(selectedLbData)['values'][1]
        return Nombre

    def getCursorTitulo(self) -> str:
        """getCursorTitulo: Obtiene el valor de Titulo del cursor.

        Returns:
            str: Devuelve el valor de Titulo del cursor.
        """
        selectedLbData = self.treeview.selection()[0]
        inicio = self.treeview.item(selectedLbData)['values'][2]
        return inicio

    def getCursorFechaPublicacion(self):
        """getCursorFechaPublicacion: Obtiene el valor de la fecha de publicacion del cursor.

        Returns:
            str: Devuelve el valor de fecha de publicacion del cursor.
        """
        selectedLbData = self.treeview.selection()[0]
        fin = self.treeview.item(selectedLbData)['values'][3]
        return fin

    def getCursorPaginas(self):
        """getCursorPaginas: Obtiene el valor de Paginas del cursor.

        Returns:
            str: Devuelve el valor de Paginas del cursor.
        """
        selectedLbData = self.treeview.selection()[0]
        duracion = self.treeview.item(selectedLbData)['values'][4]
        return duracion
    
    def getValorBuscador(self):
        busqueda=self.textvarBuscador.get()
        return busqueda
    
    
    def setTreeview(self, data: list):
        """setTreeview: Pones datos en el treeview

        Args:
            data (list): Recibe datos como lista.
        """
        #Sale si no trae datos y evita la asignación de datos vacios.
        if not data: return

        #Elimina los datos anteriores.
        self.treeview.delete(*self.treeview.get_children())
        #Asigna los datos del data.
        for row in data:
            #Inserta una row en el treeview.
            self.treeview.insert('', tk.END, text=row[0], values=row)

    def showMessageBox(self, message: str, title: str, type: str)->None:
        """showMessageBox: Muestra un mensaje en una ventana emergente.

        Args:
            message (str): Mensaje a mostrar.
            title (str): Nombre de la ventana.
            type (str): Tipo de ventana.
        """
        if type == 'info':
            messagebox.showinfo(title, message)
        elif type == 'warning':
            messagebox.showwarning(title, message)
        elif type == 'error':
            messagebox.showerror(title, message)
            
class modalWindow:
    """modalWindow: Crea una ventana modal donde se manipulan los datos del treeview.
    """
    def __init__(self, parent, Nombre, datos=()) -> None:
        self.parent = parent

        self.modal = tk.Toplevel(self.parent)
        self.modal.geometry(centrar(alto=300, ancho=460, app=self.parent))
        # self.modal.geometry(centrar(alto=230, ancho=410, app=self.parent))
        self.modal.title(Nombre)

        # Fija el redimensionamiento de la ventana
        self.modal.resizable(False, False)
        # Hacer que la ventana modal sea transitoria y modal
        self.modal.transient(self.parent)
        # Bloquea el enfoque en la ventana modal
        self.modal.grab_set()

        self.frame1 = ttk.Frame(self.modal, border=2, relief='groove')
        self.frame1.grid(padx=10, pady=10, row=0, column=0, sticky='nsew')
        
        #ID controladores ------------------------------------------------------->
        self.labelId = ttk.Label(self.frame1, text='Id: ')
        self.labelId.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.textvarId = tk.StringVar()
        self.entryId = ttk.Entry(self.frame1, textvariable=self.textvarId, state='disabled')
        self.entryId.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        #Autor controladores ------------------------------------------------------->
        self.labelAutor = ttk.Label(self.frame1, text='Autor: ')
        self.labelAutor.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        self.textvarAutor = tk.StringVar()
        self.entryAutor = ttk.Entry(self.frame1, textvariable=self.textvarAutor, width=50,
                                    validate="key",
                                    validatecommand=(self.frame1.register(self.validacionTituloAutor),"%S", "%P", "%d", "%i"))
        self.entryAutor.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        #Titulo controladores ------------------------------------------------------->
        self.labelTitulo = ttk.Label(self.frame1, text='Título: ')
        self.labelTitulo.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.textvarTitulo = tk.StringVar()
        self.entryTitulo = ttk.Entry(self.frame1, textvariable=self.textvarTitulo, width=50,
                                     validate="key",
                                     validatecommand=(self.frame1.register(self.validacionTituloAutor),"%S", "%P", "%d", "%i"))
        self.entryTitulo.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        #Fecha publicacion controladores ------------------------------------------------------->
        self.labelFechaPublicacion = ttk.Label(self.frame1, text='Fecha Publicación: ')
        self.labelFechaPublicacion.grid(row=3, column=0, padx=5, pady=5, sticky='e')

        self.textvarFechaPublicacion = tk.StringVar()
        self.entryFechaPublicacion = ttk.Entry(self.frame1, textvariable=self.textvarFechaPublicacion, width=50,
                                        validate="key",
                                        validatecommand=(self.frame1.register(self.validacionFecha),"%S", "%P", "%d", "%i"))
        self.entryFechaPublicacion.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        
        #Paginas controladores ------------------------------------------------------->
        self.labelPaginas = ttk.Label(self.frame1, text='Páginas: ')
        self.labelPaginas.grid(row=4, column=0, padx=5, pady=5, sticky='e')

        self.textvarPaginas = tk.IntVar()
        self.entryPaginas = ttk.Entry(self.frame1, textvariable=self.textvarPaginas,
                                      validate="key",
                                      validatecommand=(self.frame1.register(self.validacionPaginas),"%S", "%P", "%d", "%i"))
        self.entryPaginas.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.frame2 = tk.Frame(self.modal)
        self.frame2.grid(padx=5, pady=5, row=2, column=0, sticky='nsesw')
        
        #Botones de la ventana 
        self.aceptarButton = tk.Button(self.frame2, text="Aceptar", command=lambda: self.close_modal(True))
        #self.aceptarButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.aceptarButton.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.cancelarButton = tk.Button(self.frame2, text="Cancelar", command=lambda: self.close_modal(False))
        #self.cancelarButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='e')
        self.cancelarButton.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=True)

        # Si vienen datos en la tupla se copian en los StingVar del formulario.
        # Da Falso cuando datos es None.
        if datos:
            self.setId(datos[0])
            self.setAutor(datos[1])
            self.setTitulo(datos[2])
            self.setFechaPublicacion(datos[3])
            self.setPaginas(datos[4])

        # Establece el enfoque en la ventana modal.
        self.modal.focus_set()
        # Establecer el enfoque en el botón de cierre.
        self.entryAutor.focus_set()
        self.modal.wait_window(self.modal)

    def close_modal(self, buttonClicked=False) -> None:
        """close_modal: Elimina o destruye la ventana modal.

        Args:
            buttonClicked (bool, optional): Defaults to False.
        """
        # Define la propiedad buttonCliked para guardar el boton pulsado.
        self.buttonClicked = buttonClicked
        # Liberar el bloqueo del enfoque
        self.modal.grab_release()
        # Eliminación completa del widget
        self.modal.destroy()
                   

    def getId(self) -> str:
        """getId: Obtiene el valor de textvarId

        Returns:
            str: Retorna el valor de textvarId
        """
        return self.textvarId.get()

    def setId(self, id: str) -> None:
        """setId: Establece el valor de textvarId.

        Args:
            id (str): Valor de textvarId.
        """
        self.textvarId.set(id)

    def getAutor(self) -> str:
        """getId: Obtiene el valor de textvarAutor

        Returns:
            str: Retorna el valor de textvarAutor
        """
        return self.textvarAutor.get()

    def setAutor(self, autor: str) -> None:
        """setId: Establece el valor de textvarAutor.

        Args:
            autor (str): Valor de textvarAutor.
        """
        self.textvarAutor.set(autor)

    def getTitulo(self) -> str:
        """getId: Obtiene el valor de textvarTitulo

        Returns:
            str: Retorna el valor de textvarTitulo
        """
        return self.textvarTitulo.get()

    def setTitulo(self, titulo: str) -> None:
        """setId: Establece el valor de textvarTitulo.

        Args:
            titulo (str): Valor de textvarTitulo.
        """
        self.textvarTitulo.set(titulo)

    def getFechaPublicacion(self) -> datetime:
        """getFechaPublicacion: Obtiene el valor de textvarFechaPublicacion

        Returns:
            datetime: Retorna la fecha mediante la funcion datetime.
        """
        return datetime.strptime(self.textvarFechaPublicacion.get(), "%Y-%m-%d")
        # '%Y-%m-%d'

    def setFechaPublicacion(self, FechaPublicaion: str) -> None:
        """setFechaPublicacion: Establece el valor de textvarFechaPublicacion.

        Args:
            FechaPublicaion (str): Valor de textvarFechaPublicacion.
        """
        self.textvarFechaPublicacion.set(FechaPublicaion)

    def getPaginas(self) -> int:
        """getPaginas: Obtiene el valor de textvarPaginas.

        Returns:
            int: Retorna el valor de textvarPaginas.
        """
        return self.textvarPaginas.get()

    def setPaginas(self, paginas: int) -> None:
        """setPaginas: Establece el valor de textvarPaginas.

        Args:
            paginas (int): Valor de textvarPaginas.
        """
        self.textvarPaginas.set(paginas)
        
    #FUNCIONES DE VALIDACION -------------------------------------------------------------------------------->
    #validacion de entrada en autor
    def validacionTituloAutor(self, entrada, texto, accion, indice) -> bool:
        """validacionTituloAutor: Verificacion de la entrada de datos en titulo y autor.

        Args:
            entrada (str): Tecla presionada.
            texto (str): Texto en caja mas la entrada.
            accion (int): Borrar o escribir (0 "borrar", 1 "escribir")
            indice (indice): Indice donde se alojara la entrada en la caja de texto.

        Returns:
            bool: retorna el estado de ingreso (True ingreso permitido / False ingreso invalido)
        """
        caracteres="!#$%&//(=?'¡¿)*+}{[-_@><;:,.|]"

        if entrada.isdigit() or entrada in caracteres:
            return False
        
        if len(texto) == 50 and accion != 0:
            return False

        #No deja empezar con espacio, tampoco dos espacios consecutivos
        if entrada.isspace():
            i=int(indice)-1
            if texto[i] == " ":
                return False
        #Permite el ingreso unicamente de cuatro espacios, sin la posibilidad de un quinto
        count=0
        for x in texto:
            if x.isspace():
                count+=1
            if count == 4 and accion!=0:
                return False

        return True
    
    def validacionFecha(self, entrada, texto, accion, indice) -> bool:
        """validacionFecha: Controlara el ingreso correcto de caracteres en el campo de fecha.

        Args:
            entrada (str): Tecla presionada.
            texto (str): Texto en caja mas la entrada.
            accion (int): Borrar o escribir (0 "borrar", 1 "escribir")
            indice (int): Indice donde se alojara la entrada en la caja de texto.

        Returns:
            bool: Retorna el estado de ingreso (True ingreso permitido / False ingreso invalido)
        """
        #"YYYY-MM-DD"
        caracteres="!#$%&//(=?'¡¿)*+}{[_@><;:,.|]"
        #Permite solo el ingreso de letras y el caracter especial "-"
        if entrada.isalpha() or entrada in caracteres or entrada.isspace():
            return False 
        cont1=int(indice)
        comparador=str(entrada)
        #Permite ingresar 4 caracteres numericos al principio, sin posibilidad de ingresar "-".
        if len(texto) <= 4 and "-" in texto[:5]:
            return False 
        #Restringe el ingreso de caracteres, permitiendo el ingreso solamente de un "-" en la posicion 4 de la cadena.
        if len(texto) == 5 and texto[4].isdigit():
            return False 
        #Restringe la posibilidad de ingresar "-" en las posiciones 5 y 6 de la cadena.
        if (7>= len(texto) >= 6) and "-" in texto[5:7]:
            return False 
        #Restringe la posibilidad de ingresar un numero mayor a 1 ó menor a 0 en el primer caracter del mes.
        if len(texto) == 6:
            if (1 != int(texto[5]) !=0):
                return False 

        #control de buen ingreso de mes.
        if len(texto) == 7:
            #Retringue la posibilidad de ingresar un cero en el indice 6 de la cadena si el caracter del indice 5 de la cadena es un 0, 
            # es decir, no permite un "-00-"
            if int(texto[5]) == 0 and int(texto[6]) == 0:
                return False 
            #Retringue la posibilidad de ingresar un numero mayor a 2 en el indice 6 de la cadena, 
            # si el numero anterior es 1, es decir, no permite "-13-", "-14-" y asi sucesivamente. Solo menores de 12 inclusive.
            if int(texto[5]) == 1 and int(texto[6]) > 2:
                return False 

        #Restringe el ingreso de caracteres, permitiendo el ingreso solamente de un "-" en la posicion 7 de la cadena.
        if len(texto) == 8 and texto[7].isdigit():
            return False 

        #Restringe la posibilidad de ingresar "-" en las posiciones 8 y 9 de la cadena.
        if len(texto) >= 9 and "-" in texto[8:]:
            return False 

        #control de buen ingreso de dias.
        #Restringe la posibilidad de ingresar un numero mayor a 31 
        if len(texto) == 9:
            #Restringe la posibilidad de ingresar un numero mayor a 3 en el indice 8 de la cadena
            if int(texto[8]) > 3:
                return False 
        if len(texto) > 9:
            #Restringe la posibilidad de ingresar un numero mayor a 1 en el indice 9 de la cadena si el numero del indice 8 de la cadena es 3.
            if int(texto[8]) == 3 and int(texto[9]) > 1:
                return False 
            #Restringe la posibilidad de ingresar dos ceros seguidos.
            if int(texto[8]) == 0 and int(texto[9]) == 0:
                return False 
            #Restringe la posibilidad de ingresar un numero mayor a 8 en el indice 9 de la cadena si el mes es febrero.
            if str(texto[5:7]) == "02" and int(texto[9]) > 8:
                return False 
        if len(texto) >=9:
            #Restringe la posibilidad de ingresar un numero mayor a 2 en el indice 8 de la cadena si el mes es febrero.
            if str(texto[5:7]) == "02" and int(texto[8]) == 3:
                return False 

        #Restinge la posibilidad de ingresar mas caracteres de los que una fecha deberia tener, siguiendo el siquiente fromato: "YYYY-MM-DD" 
        if len(texto) == 11 and accion != 0:
            return False 

        #No permite ingresar dos "-" seguidos.
        if entrada == "-" and "-" in texto[cont1-1]:
            return False 

        return True 
    
    
    def validacionPaginas(self,entrada, texto, accion, indice) -> bool:
        """validacionPaginas: Validacion de la entrada paginas, permite solo el ingreso de 10 caracteres numericos.

        Args:
            entrada (_type_): Tecla presionada.
            texto (_type_): Texto en caja mas la entrada.
            accion (_type_): Borrar o escribir (0 "borrar", 1 "escribir")
            indice (_type_): Indice donde se alojara la entrada en la caja de texto.

        Returns:
            bool: _description_
        """
        caracteres="!#$%&//(=?'¡¿)*+}{[\\-_@><;:,.|]"
        # Se permite solo el ingreso de numeros.
        if entrada.isalpha() or entrada in caracteres:
            return False
        # Se permite solo el ingreso de 10 caracteres.
        if len(texto) > 10:
            return False
        
        return True
    



        
