import sqlite3
#import of the sqlite module
#importamos del modulo de sqlite3 el paquete de Errores
from sqlite3 import Error

"""Para crear una conexion sqlite3 
definimos el nombre de la base de datos a conectar / crear
y moldeamos el codigo dentro de un try_except para evitar breaks"""
def sql_connexion():
    try:
        conexion = sqlite3.connect('my_first_database.db') #podemos utilizar el parametro :memory: 
        return conexion
    except Error:
        print(Error)
        
def create_table(con):
    cursor = con.cursor()
    cursor.execute("CREATE table personal(id integer PRIMARY KEY,descripcion text,salario integer)")
    print("Se ha creado con exito la tabla personal!")
    con.commit()
    
def insertar_new_row(con, valores):
    cursor= con.cursor()
    cursor.execute("INSERT INTO personal(id,descripcion,salario) VALUES(?,?,?)",valores)
    print("Se ha agregado con exito un nuevo row")
    con.commit()
    
def actualizar_elemento(con):
    cursor= con.cursor()
    cursor.execute("UPDATE personal SET salario= 1000000 where ID=123")
    print("Se ha actualizado con exito el registro")
    con.commit()
        
#llamamos al metodo y creamos nuestra primera conexion
conexion = sql_connexion()
create_table(conexion)
#usando nuestra conexion hacemos llamado a la funcion create_table
datos1=(1,"mesero",80000)
datos2=(2,"patinador",500000)
datos3=(3,"cocinero",450000)
datos4=(4,"programador",99999999)
datos5=(5,"musico",1564210)

#genero un query se insert values con la lista de datos
insertar_new_row(conexion,datos1)
insertar_new_row(conexion,datos2)
insertar_new_row(conexion,datos3)
insertar_new_row(conexion,datos4)
insertar_new_row(conexion,datos5)

# agregar_varios_registros(conexion,**dict_datos) como puedo enviar varias listas en un mismo parametro / Con un diccionario

def todos_los_registros(con):
    cursor=con.cursor() # mi cursor guarda el resultado de los select
    cursor.execute("SELECT * FROM personal")
    
    # la funcion fetchall() me despliega todo el contenido del cursor 
    resultado_de_query = cursor.fetchall()
    
    #con un for puedo imprimir cada registro del resultado
    for cada_row in resultado_de_query:
        print(cada_row)
    
#esta funcion devuelve todos los registro de mi tabla
todos_los_registros(conexion)