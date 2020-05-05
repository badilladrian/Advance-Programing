import sqlite3

class Controller():
    
    #global controller object
    controller= None
    
    def __init__(self, conector):
        #class init
        self.conector = conector;
        
    def start(self):
        conector=self.conector
        controller = Controller(conector)
        self.conector = controller.inicia_base_datos()
        #Creates a controller Object and inits the method inicia_base_datos()
        print("Iniciando el controlador")

    def stop(self):
        #exits the program
        print("Gracias por correr el controller!")
        exit()
        
        
    def inicia_base_datos(self):
        #inits the data base
        self.conector = sqlite3.connect("mi_base.db")
        print("Base de Datis iniciada!")
        return self.conector
        
        
    def insert_query(self, values):
        cursor = self.conector.cursor()
        cursor.execute('INSERT INTO millas_viajadas(ID, name, millas) VALUES(?, ?, ?)', values)
        self.conector.commit()
        #executes queries
        print("Acaba de hacer un SQL injection!")
        print("Query Creado!")
    
    
    def crear_tabla(self, conector):
        cursor = self.conector.cursor()
        cursor.execute("CREATE TABLE millas_viajadas(ID integer PRIMARY KEY, name text, millas integer)") 
        #creating a table
        print("Tabla millas_viajadas Creada!")
        conector.commit()
        
        
    def update_query(self,data):
        cursor = self.conector.cursor()
        query = "UPDATE millas_viajadas SET millas = {} where ID = 2".format(data)
        cursor.execute(query)
        print("Se ha hecho un update!")
        #updating a register
        conector.commit()
        
        
    def fetch_registers(self,fetch):
        cursor = self.conector.cursor()
        if fetch==1:
            query = "SELECT * FROM millas_viajadas"
            cursor.execute(query)
            allrows = cursor.fetchall()
            print("Todos los registros desplegados!")
            return allrows;
        if fetch==2:
            query = "SELECT ID, name FROM millas_viajadas WHERE millas > 4500"
            cursor.execute(query)
            specific_select = cursor.fetchall()
            print("Todos los registros con condicional!")
            return specific_select;
        
        
    def print_values(self, result):
        for hilera in result:
            print(hilera)
            
            
    def another_transaction(self):
        decision = input("Desea hacer otra gestion? (Y/N)")
        if decision == "Y":
           newValues= controller.pedir_valores()
           return newValues;
        if decision == "N":
            controller.stop()
           
            
    def pedir_valores(self):
        ID = input("Ingrese el ID: ")
        nombre = input("Ingrese el nombre: ")
        millas = input("Ingrese el numero de millas: ")
        lista_valores= (ID,nombre,millas)
        return lista_valores
        
            
    def main(self):
        controller.start()
        controller.crear_tabla(controller.conector)
        valores = controller.pedir_valores()
        controller.insert_query(valores)
        resultado = controller.fetch_registers(1)
        controller.print_values(resultado)
        accion =controller.another_transaction()
        if (accion!= None):
            controller.insert_query(accion)
            resultado = controller.fetch_registers(2)
            controller.print_values(resultado)
        controller.stop()
    
    
if __name__ == "__main__":
    con = sqlite3.connect(":memory:")
    controller = Controller(con)
    controller.main()
        
            
            
        


      
      
      
  
    