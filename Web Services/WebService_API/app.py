from flask import Flask, jsonify, request
#importamos el framework de Flask
#jsonify genera HTTP objects with JSON object
#request maneja los HTTP objects

#asi importo objectos de otros modulos / scripts
from alumnos import MisProductos

#object server
app = Flask(__name__)

#importo mi objeto MisProductos de alumnos y creo una instancia 
instacia_productos = MisProductos()

#routing methods
#method to test the server
@app.route('/')
def ping():
    return jsonify(
        {
            "Message": "Poooong!"
        }
    )


#metodo para devolver toda la lista de estudiantes
@app.route('/estudiantes', methods=['GET'])
def getAllStudents():
    return jsonify(
        {
            "Message": "Esta es la lista de estudiantes!",
            "Estudiantes": instacia_productos.lista_alumnos
        }
    )


#metodo para devolver un estudiante especifico
@app.route('/estudiantes/<int:id_estud>', methods=['GET'])
def getStudent(id_estud):
    estudiante = instacia_productos.buscar_id(id_estud)
    return jsonify(
        {
            "Message": "La busqueda del estudiante: " + str(id_estud) ,
            "Estudiante": estudiante
        }
    )

#metodo para agregar un nuevo estudiante
@app.route('/estudiantes', methods=['POST'])
def agregarStudent():
    #creo un objecto diccionario estudiante
    estudiante = {"id_alumno": None, "nombre": None}

    #capturo el JSON dentro del request del client
    estudiante['id_alumno']= request.json['id_estudiante'] #PUEDEN PERSONALIZAR EL KEY NAME DEL JSON DEL LADO DEL CLIENT
    #guardo sus valores dentro de los keys de mi objecto estudiante
    estudiante['nombre']= request.json['nombre_estudiante']

    #agrego mi objecto nuevo a lista de mi instancia
    instacia_productos.lista_alumnos.append(estudiante)

    return jsonify(
        {
            "Message": "Un nuevo estudiante ha sido agregado!",
            "Dato": estudiante
        }
    )


@app.route('/actualizar/<int:id_estud>', methods=['PUT'])
def actualizaEstudiante(id_estud):
    #primero busco si el objecto en cuestion existe
    estudiante = instacia_productos.buscar_id(id_estud)
    print(estudiante)
    #si el objeto no existe
    if estudiante ==None:
        #devuelvo un mensaje indicando None
            return jsonify(
        {
            "Message": "El estudiante ha actualizar: " + str(id_estud) + " NO existe."
        }
    )
    else:
        #creo objetos con los nuevos valores para enviar como *parametros
        new_id = request.json['id_estudiante']
        new_name = request.json['nombre_estudiante']

        #recibo el resultado(str) de la funcion actualizar_alumno(*valores)
        resultado = instacia_productos.actualizar_alumno(id_estud, new_id, new_name)
        estudiante = instacia_productos.buscar_id(new_id)

        return jsonify(
        {
            "Message": resultado,
            "Dato": estudiante
        }
    )

    


@app.route('/estudiantes/<int:id_estud>', methods=['DELETE'])
def deleteEstudiante(id_estud):
    estudiante = instacia_productos.buscar_id(id_estud)

    #si el objeto no existe
    if estudiante ==None:
        #devuelvo un mensaje indicando None
            return jsonify(
        {
            "Message": "El estudiante ha eliminar: " + str(id_estud) + " NO existe."
        }
    )
    else:
        #
        resultado = instacia_productos.eliminar_alumno(id_estud)
        return jsonify(
            {
                "Message": resultado,
                "Dato": "Eliminamos a: " + str(estudiante)
            }
        )



if __name__=='__main__':
    app.run(debug=True, port=4000)