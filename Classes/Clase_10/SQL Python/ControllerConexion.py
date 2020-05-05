import sqlite3

class Controller():
    
    #variable global controller object
    controller= None
    
    
    def __init__(self,conector):
        self.conector = conector;
        #funcion init de mi class
    
        
    def start(self):
        conector=self.conector
        self.controller=Controller(conector)
        self.conector= controller.iniciar_nueva_base_datos()
        #Create a controller Object and inits the method iniciar_nueva_base_datos
        print("Iniciando mi controlador!")
        
    
    def iniciar_nueva_base_datos(self):
        self.conector = sqlite3.connect("mi_propia_base.db")
        print("Se ha creado una base de datos!")
        return self.conector


    def crear_tabla(self):
        cursor = self.conector.cursor()
        cursor.execute("CREATE TABLE millas_viajadas(ID integer PRIMARY KEY, nombre text, millas integer)")
        print("Tabla millas_viajadas Creada!")
        self.conector.commit()
        
        
    def insert_query(self,valores):
        cursor = self.conector.cursor()#formamos el query con los valores dados
        cursor.execute("INSERT INTO millas_viajadas(ID,nombre,millas) VALUES(?,?,?)",valores)
        print("Se ha creado un nuevo registro en la tabla millas_viajadas!")
        self.conector.commit()
        
        
    def solicitar_valores(self):
        ID = input("Ingrese el ID: ")
        nombre = input("Ingrese el nombre: ")
        millas = input("Ingrese el numero de millas: ")
        lista_valores = (ID,nombre,millas)
        return lista_valores
    
    
    def update_query(self,value):
        cursor = self.conector.cursor()
        query = "UPDATE millas_viajadas SET millas = {} WHERE ID =50".format(value) #capturo el valor a modificar
        cursor.execute(query) #envio el query como un string
        print("Se ha actualizado un registro!")
        self.conector.commit()


    """El cursor tiene integrado varios tipos de fetch:
    cursor.fetchall() fetches all the rows of a query result. It returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch.
    cursor.fetchmany(size) returns the number of rows specified by size argument. 
    When called repeatedly this method fetches the next set of rows of a query result and returns a list of tuples.
    If no more rows are available, it returns an empty list.
    cursor.fetchone() method returns a single record or None if no more rows are available."""
    def fetch_registros(self, fetch_type):
        cursor = self.conector.cursor()
        
        if fetch_type==1:
            query = "SELECT * FROM millas_viajadas"
            #el cursor tiene el contenido de mis selects
            cursor.execute(query)#guardo en una variable el contenido total del cursor
            todos_los_elementos = cursor.fetchall()
            return todos_los_elementos;

        if fetch_type==2:
            query = "SELECT * FROM millas_viajadas WHERE millas > 4500"
            cursor.execute(query)
            elementos_con_condicional = cursor.fetchall()
            return elementos_con_condicional;
        
        
    def print_values(self,result):
        if result!=None:
            for hilera in result:
                print(hilera)
                
                
    def agregar_lista_datos(self):
        datos1=(1,"Adrian",800)
        datos2=(2,"Marco",5000)
        datos3=(3,"Juan",450)
        datos4=(4,"Luis",9999)
        datos5=(5,"Milton",4210)
        
        #hacemos inyeccion SQL de la sentencia insert con las listas de datos#
        controller.insert_query(datos1)
        controller.insert_query(datos2)
        controller.insert_query(datos3)
        controller.insert_query(datos4)
        controller.insert_query(datos5)

    
    def another_transaction(self):
        decision = input("Desea hacer otra gestion? (Y/N)")
        
        if decision == "Y": #Si se desea hacer otra gestion, pide nuevos inputs al usuario
            nuevosValores = controller.solicitar_valores()
            return nuevosValores;#devuelve los valores dados
        
        if decision == "N":#si no desea continuar
            controller.stop()#exit()


    def stop(self):
        print("Gracias por correr mi controlador!")
        exit()
        
    
    def main(self):
        controller.start()
        controller.crear_tabla()#acceso a mi objecto conector de mi variable global tipo controller
        #datos = controller.solicitar_valores()
        #controller.insert_query(datos)
        #controller.update_query(80000)
        controller.agregar_lista_datos()
        
        #el resultado del fetch son todos los registros
        registros = controller.fetch_registros(1)
        controller.print_values(registros)
        print("LOS REGISTROS DE ARRIBA SON TODOS, LOS DE ABAJO SON MILLAS>4500")
        #el resultado del fetch son solo elementos con la clausula where
        registros = controller.fetch_registros(2)
        controller.print_values(registros)
        #se le pregunta al usuario si desea hacer otra transaccion
        #de ser afirmativo registra nuevos valores, de ser negativo no hay return
        accion = controller.another_transaction()
        
        if (accion!=None):
            controller.insert_query(accion)
            resultado = controller.fetch_registros(2)
            controller.print_values(resultado)
        
        controller.stop()


#el metodo main para ejecutar mi aplicacion
if __name__=="__main__":
    con = sqlite3.connect(":memory:") #creo espacio en memoria para la base de datos
    controller = Controller(con) #creo una instancia de mi clase Controller
    controller.main() #ahora con un objecto controller puedo acceder a los metodos
