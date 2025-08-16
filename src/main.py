# The Real Library Control

import itertools

class Libro:
    
    def __init__(self,titulo:str="",autor:str="",genero:str="",fecha_publicacion:int=None):
        nombre,apellido = autor.split()
        numeros = itertools.count(0)
        self.id = apellido[0]+nombre[0]+titulo[0]+str(next(numeros))
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
    
    def eliminar_libro(self,id):
        for libro in self.libros:
            if libro.id == id:
                self.libros.remove(libro)
    
    def mostrar_libros(self):
        if not self.libros:
            return "La biblioteca esta vacía"
        for n, libro in enumerate(self.libros,1):
            print(f"{n}. [{libro.id}] {libro.titulo} - {libro.autor} - {libro.genero}, ({libro.fecha_publicacion}) Prestado: {libro.prestado}")
        return ""

biblioteca1 = Biblioteca()

biblioteca1.agregar_libro("Principios de administracion","Adalberto Chiavenato","Educacion",2010)

print(biblioteca1.mostrar_libros())



