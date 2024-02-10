"""
libros_controler.py maneja los modulos libros_model y lirbso_view.
"""
from views.libros_view import Libros_view, modalWindow
from models.libros_model import Libros_model

class Libros_controler():
    def __init__(self, root: object) -> None:
        """constructor de la clase Libros_controler().
        """
        self.root = root
        # Instancia el modelo.
        self.model = Libros_model()
        # Crea  un istancia la vista.
        self.view = Libros_view(self.root)
        # Añade la función addToTreeview al botón de agregar.
        self.view.buttonAdd["command"] = self.addToTreeview
        # Añade la función removeFromTreeview al botón de eliminar.
        self.view.buttonUpdate["command"] = self.updateFromTreeview
        # Añade la función updateFromTreeview al botón de actualizar.
        self.view.buttonRemove["command"] = self.removeFromTreeview
        # Añade la función loadTreeviewToEntry al evento de selección de fila.
        self.view.buttonExit["command"] = self.__del__
        
        self.view.botonBuscador["command"] = self.cargar_datos_buscador
        self.view.botonBuscador1["command"] = self.limpiar_campos

        # Añade la función loadTreeviewToEntry al evento de selección de fila.
        #self.view.treeview.bind('<<TreeviewSelect>>', self.loadTreeviewToEntry)
        # Carga los datos de la base de datos al treeview.
        self.loadToTreeview()

        pass

    def loadToTreeview(self)->None:
        """loadToTreeview Carga los datos de la base de datos al treeview.
        """
        data = self.model.getAllData()
        self.view.setTreeview(data)

    def addToTreeview(self)->None:
        """addToTreeview Agrega un registro a la base de datos y al treeview.
        """
        try:
            # Crea una instancia de la ventana modal
            self.modal = modalWindow(self.root, 'Altas de Libros')

            #Solo si hay un registro seleccionado el el treeview.
            if self.modal.buttonClicked:
                if self.modal.textvarAutor.get() != '' and \
                    self.modal.textvarTitulo.get() != '' and \
                    self.modal.textvarFechaPublicacion.get() != '' and \
                    self.modal.textvarPaginas.get() != '' :

                    self.addToDB()
                    self.loadToTreeview()
                    self.clearForm()
                else:
                    self.view.showMessageBox(message='Debe llenar todos los campos.', title='Error', type='error')
        except:
            print("Ventana 'Altas de Libros' cerrada inesperadamente")

    def removeFromTreeview(self)->None:
        """
        removeFromTreeview: Elimina un registro de la base de datos y del treeview.
        Solo si hay un registro seleccionado el el treeview.
        """
        if self.view.treeview.selection():
            # Crea una instancia de la ventana modal
            self.modal = modalWindow(self.root, 'Bajas de Libros', self.loadTreeviewToEntry())

            if self.modal.buttonClicked:
                    self.removeFromDB()
                    self.loadToTreeview()
                    self.clearForm()

    def updateFromTreeview(self)->None:
        """
        updateFromTreeview: Actualiza un registro de la base de datos y del treeview.
        Solo si hay un registro seleccionado el el treeview.
        """
        try:
            if self.view.treeview.selection():
                # Crea una instancia de la ventana modal
                self.modal = modalWindow(self.root, 'Modificación de Libros', self.loadTreeviewToEntry())
    
                if self.modal.buttonClicked:
                        self.updateDB()
                        self.loadToTreeview()
                        self.clearForm()
        except:
            print("Ventana 'Modificación de Libros' cerrada inesperadamente")

    def loadTreeviewToEntry(self, event=None)->tuple:
        """
        loadTreeviewToEntry: Carga un nuevo registro a la base de datos y al treeview.
        Solo si hay un registro seleccionado el el treeview.

        Args:
            event (_type_, optional): Defaults to None.

        Returns:
            tuple: con los datos a cargar en base de datos y treeview.
        """
        if self.view.treeview.selection():
            self.id = self.view.getCursorId()
            self.autor = self.view.getCursorAutor()
            self.titulo = self.view.getCursorTitulo()
            self.fechaPublicacion = self.view.getCursorFechaPublicacion()
            self.paginas = self.view.getCursorPaginas()
        return (self.id,
                self.autor,
                self.titulo,
                self.fechaPublicacion,
                self.paginas)

    def addToDB(self)->None:
        """addToDB: Agrega un registro a la base de datos.
        """
        autor = self.modal.getAutor()
        titulo = self.modal.getTitulo()
        fechaPublicacion = self.modal.getFechaPublicacion()
        paginas = self.modal.getPaginas()
        self.model.create(autor, titulo, fechaPublicacion, paginas)

    def updateDB(self)->None:
        """uodateDB: Actualiza un registro en la base de datos.
        """
        id = self.view.getCursorId()
        autor = self.modal.getAutor()
        titulo = self.modal.getTitulo()
        fechaPublicacion = self.modal.getFechaPublicacion()
        paginas = self.modal.getPaginas()
        self.model.update(id, autor, titulo, fechaPublicacion, paginas)

    def removeFromDB(self)->None:
        """removeFromDB: Elimina un registro de la base de datos.
        """
        id = self.view.getCursorId()
        self.model.delete(id)
        

    def clearForm(self)->None:
        """clearForm: Limpia la vista del treeview.
        """
        self.modal.setId("")
        self.modal.setAutor('')
        self.modal.setTitulo('')
        self.modal.setFechaPublicacion('')
        self.modal.setPaginas(0)

        #Deselecciona fila de treeview.
        self.view.treeview.selection_remove(self.view.treeview.selection())

        return

    def __del__(self)->None:
        """__del__: Destruye la ventana modal en conjunto con sus respectivos frames.
        """
        self.view.ventana_modal.destroy()
        self.view.frame3.destroy()
        self.view.frame4.destroy()

        #del self
    def cargar_datos_buscador(self) -> None:
        buscador = self.view.textvarBuscador
        id = self.view.textvarBuscadorId
        autor = self.view.textvarBuscadorAutor
        titulo = self.view.textvarBuscadorTitulo
        fecha = self.view.textvarBuscadorFecha
        paginas = self.view.textvarBuscadorPaginas
        resultados = self.model.buscar_datos(buscador.get())
        if len(resultados) > 0:
            # Agregamos valores a los stringvar con los resultados de la busqueda.
            id.set(f" {resultados[0][0]}")
            autor.set(f" {resultados[0][1]}")
            titulo.set(f" {resultados[0][2]}")
            fecha.set(f" {resultados[0][3]}")
            paginas.set(f" {resultados[0][4]}")
        else:
            buscador.set("Libro no encontrado")
            id.set("--------")
            autor.set("--------")
            titulo.set("--------")
            fecha.set("--------")
            paginas.set("--------")
            #fin
    def limpiar_campos(self) -> None:
        """limpiar_campos: Limpia los campos del fromulario de busqueda.
        """
        self.view.textvarBuscador.set("")
        self.view.textvarBuscadorAutor.set("")
        self.view.textvarBuscadorFecha.set("")
        self.view.textvarBuscadorTitulo.set("")
        self.view.textvarBuscadorId.set("")
        self.view.textvarBuscadorPaginas.set("")
