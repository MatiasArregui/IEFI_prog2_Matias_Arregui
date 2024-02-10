#Libros_model.py
from datetime import date

from database.dbConn import dbConn

class Libros_model():
    """Libros_model: Modelo de la tabla libros.
    """
    def __init__(self) -> None:
        """Constructor de la clase, establece la conexión a la base
        de datos e intenta crear la tabla si no existe..
        """
        self.titulo = ""
        self.autor = ""
        self.fecha_publicacion = None
        self.paginas = 0

        #Abre la conexión con la base de datos alumnos y si no existe la crea.
        self.conn = dbConn("database\\libros.sqlite3")
        #Crea la tabla carreras si no existe.
        tableName = 'libros'
        fieldsDescripcion = '('\
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '\
            'autor TEXT(100) NOT NULL UNIQUE, '\
            'titulo TEXT(100) NOT NULL UNIQUE, '\
            'fecha_publicacion DATE NOT NULL, '\
            'paginas INTEGER NOT NULL)'
        #Ejecuta el comando en la base de datos.
        self.conn.createTable(tableName=tableName, fieldsDescripcion=fieldsDescripcion)

    def create(self, autor: str, titulo: str, fecha_publicacion: date, paginas: int) -> list:
        """create: Crea un registro en una tabla.

        Args:
            autor (str): Nombre del autor del libro.
            titulo (str): Titulo del libro.
            fecha_publicacion (date): Fecha de publicacion del libro.
            paginas (int): Cantidad de paginas del libro.

        Returns:
            list: Lista con el comando y los valores que conformaran el mismo.
        """
        command = 'INSERT INTO libros (autor, titulo, fecha_publicacion, paginas) VALUES (?, ?, date(?), ?)'
        values = (autor, titulo, fecha_publicacion, paginas)
        return self.conn.execute(command, values)

    def read(self, id: str) -> list:
        """read: Lee un registro de la base de datos.

        Args:
            id (int): Id del registro a leer.

        Returns:
            list: Retorna el registro leído.
        """
        command = 'SELECT * FROM libros WHERE id = ?'
        values = (id,)
        return self.conn.execute(command, values)

    def update(self, id: str, autor: str, titulo: str, fecha_publicacion: date, paginas: int) -> list:
        """update: Actualiza un registro de la base de datos.

        Args:
            id (int): Id del registro a actualizar.
            autor (str): Nombre del autor del libro.
            titulo (str): Titulo del libro.
            fecha_publicacion (date): Fecha de publicacion del libro.
            paginas (int): Cantidad de paginas del libro.

        Returns:
            list: Lista con los valores del registro a actualizar.
        """
        command = 'UPDATE libros SET autor = ?, titulo = ?, fecha_publicacion = date(?), paginas = ? WHERE id = ?'
        values = (autor, titulo, fecha_publicacion, paginas, id)
        return self.conn.execute(command, values)

    def delete(self, id: str) -> list:
        """delete: Borra un registro de la base de datos.

        Args:
            id (int): Id del registro a borrar.

        Returns:
            list: Devuelve el registro borrado.
        """
        command = 'DELETE FROM libros WHERE id = ?'
        values = (id,)
        return self.conn.execute(command, values)

    def getAllData(self) -> list:
        """getAllData: Recupera todos los registros de la base de datos.

        Returns:
            list: devuelve una lista de libros.
        """
        command = 'SELECT * FROM libros'
        return self.conn.execute(command)

    
    def __del__(self) -> None:
        """__del__: Destructor de la clase.
        """
        del self.conn
        del self
        
    def buscar_datos(self, buscador) -> list:
        command = f"SELECT * FROM libros WHERE titulo = ?"
        values = (buscador,)
        return self.conn.execute(command, values)

