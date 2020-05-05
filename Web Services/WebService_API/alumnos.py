
"""clase para manejar los datos de mi DBA"""

class MisProductos():

    def __init__(self):
        self.lista_alumnos = [
                {"id_alumno": 1, "nombre": "Luis"},
                {"id_alumno": 2, "nombre": "Milton"},
                {"id_alumno": 3, "nombre": "Maria Laura"},
            ]


    def buscar_id(self,id_alumno):
        #loop de for cada elemento en mi lista iterable
        for diccionario in self.lista_alumnos:
            #si mi diccionario actual cumple la condicion
            if diccionario['id_alumno']==id_alumno:
                #devuelvo ese diccionario especifico
                return diccionario;



    def actualizar_alumno(self, id_original, id_new, new_name):
        alumno = self.buscar_id(id_original)
        ind = self.lista_alumnos.index(alumno)
        
        if ind!=-1:
            self.lista_alumnos[ind]['id_alumno'] = id_new
            self.lista_alumnos[ind]['nombre'] = new_name
            return "Alumno Actualizado!"


    def eliminar_alumno(self, id_eliminar):
        alumno = self.buscar_id(id_eliminar)
        self.lista_alumnos.pop(self.lista_alumnos.index(alumno))
        return "Estudiante eliminado!"
