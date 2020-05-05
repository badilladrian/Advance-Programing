import psycopg2
from psycopg2 import Error

class Conector():
    
    def start(self,conector):
        self.conector = conector;
        self.cursor = self.conector.cursor()
        #funcion init de mi class
    
    
    #metodo para iniciar conexion con la DBA
    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            # connect to the PostgreSQL server
            print('Conectandocon PostgreSQL...')
            conexion = psycopg2.connect(host="localhost", database="dvdrental", user="postgres", password="Franco2!2!")
            print('Conectado to the PostgreSQL DVDRENTAL DBA...')
            return conexion
        except (Exception, psycopg2.Error) as error :
            print ("Error conectando a PostgreSQL", error)


    def ejecutar_query(self,query):
        # execute a statement
        try:
            print('Ejecutando query...')
            self.cursor.execute(query)
            print(query)
            print("Query ejecutado!")
            self.conector.commit()
        except (Exception, psycopg2.Error) as error :
            print(error)
 
 
    def retornar_query(self,query):
        # execute a statement
        try:
            print('Ejecutando query...')
            self.cursor.execute(query)
            print("Query ejecutado!")
            elementos = self.cursor.fetchall()
            return elementos;      

        except (Exception, psycopg2.Error) as error :
            print(error)


if __name__ == '__main__':
    objecto_conexion = Conector()
    conexion = objecto_conexion.connect()
    objecto_conexion.start(conexion)
    my_query = "select * from category;"
    objecto_conexion.ejecutar_query("CALL actualizalenguaje(2);")
    resultados = objecto_conexion.retornar_query(my_query)
    print(resultados)