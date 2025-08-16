# The Real Library Control

import itertools

class Libro:
    
    def __init__(self,titulo:str="",autor:str="",genero:str="",fecha_publicacion:int=None):
        def asignador_id(titulo:str,autor:str):
            numeros = itertools.count(0)
            if len(autor.split()) != 2:
                return autor[0]+titulo[0]+str(next(numeros))
            try:
                nombre,apellido = autor.split()
                return apellido[0]+nombre[0]+titulo[0]+str(next(numeros))
            except:
                raise ValueError("Debe ingresar autor con el siguiente formato: 'nombre' 'apellido'")
        
        self.id = asignador_id(titulo,autor) 
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.fecha_publicacion = fecha_publicacion
        self.prestado = False

# class Revista(Libro):
    
#     def __init__(self, titulo = "", autor = "", genero = "", fecha_publicacion = None):
#         super().__init__(titulo, autor, genero, fecha_publicacion)

class Biblioteca:
    
    def __init__(self):
        
        self.libros = []
    
    def agregar_libro(self,titulo,autor,genero,fecha_publicacion):
        libro = Libro(titulo,autor,genero,fecha_publicacion)
        self.libros.append(libro)
    
    def buscar_libro(self,parametro):
        resultado = []
        for libro in self.libros:
            if (parametro == libro.id or
                parametro == libro.autor or
                parametro == libro.genero or
                parametro == libro.titulo or
                parametro == libro.fecha_publicacion):
                resultado.append(libro)
        if not resultado:
            return "No se encontraron resultados"
        else: 
            for n, libro in enumerate(resultado,1):
                print(f"{n}. [{libro.id}] {libro.titulo} - {libro.autor} - {libro.genero}, ({libro.fecha_publicacion}) Prestado: {libro.prestado}")
        return ""
    
    def eliminar_libro(self,id):
        for libro in self.libros:
            if libro.id == id:
                self.libros.remove(libro)
    
    def listar_libros(self):
        if not self.libros:
            return "\nLa biblioteca esta vacía"
        for n, libro in enumerate(self.libros,1):
            print(f"{n}. [{libro.id}] {libro.titulo} - {libro.autor} - {libro.genero}, ({libro.fecha_publicacion}) Prestado: {libro.prestado}")
        return ""

biblioteca1 = Biblioteca()

biblioteca1.agregar_libro("Administracion","Juan","Terror",2005)
biblioteca1.agregar_libro("Administracion","Miguel Angel","Fantasia",2010)

print(biblioteca1.buscar_libro("Administracion"))

