from flask import Flask, jsonify, request, make_response
from products import MisProductos
import jwt, datetime

#needed imports

#object server
app = Flask(__name__)

app.config['SECRET_KEY']= 'mykey'
#aqui tengo la lista de mis productos de mi DBA 
controller_productos = MisProductos()

#routing methods
#default entry
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"FLASK":"APP!"})


#ping to test the server
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"Message":"Pong!"})


#to retrieve the product_list
@app.route('/productos', methods=['GET'])
def getProductos():
    return jsonify({"Message": "La lista de productos!",
                    "Products":controller_productos.productos})


#to retrieve an specific element due dynamic value
@app.route('/productos/<string:id_nombre>', methods=['GET'])
def getProductosById(id_nombre):
    #Utilizamos el busca_producto() para devolver el producto
    producto = controller_productos.busca_producto(id_nombre)

    #si el producto no es encontrado
    if producto==None:
        return jsonify({"Message":"Producto no existente!"})

    #si el producto es encontrado
    return jsonify({"Producto":producto})

#to add product
@app.route('/productos', methods=['POST'])
def addProduct():
    #capturo los datos enviados en el request POST
    new_product = {"nombre": request.json['nombre'], 
                    "precio": request.json['precio'], 
                    "cantidad": request.json['cantidad']}

    #agrego el producto a mi objeto productos                    
    controller_productos.productos.append(new_product)

    #de ser exitoso, devuelvo exito
    return jsonify({"Message":"Se ha agregado el producto!",
                        "Producto":new_product})


#to update product
@app.route('/productos/<string:id_nombre>', methods=['PUT'])
def editProduct(id_nombre):
    #buscamos el producto
    producto = controller_productos.busca_producto(id_nombre)

   #si el producto no es encontrado
    if producto==None:
        return jsonify({"Message":"Producto no existente!"})
    else:
        #guardamos los valores originales para comparar
        nombre=producto['nombre']
        precio=producto['precio']
        cantidad=producto['cantidad']
        datos_originales = (nombre,precio,cantidad)

        nom =  request.json['nombre']
        prec = request.json['precio']
        cant = request.json['cantidad']

    #envia parametros para actualizar al controlador desde el request
        resultado = controller_productos.actualiza_producto(id_nombre,
                                          str(nom),int(prec),int(cant))

        if resultado != None:
            #si el producto es encontrado
            return jsonify({"Message":resultado,
                            "Datos Originales" : datos_originales,
                            "Producto Actualizado" : producto})


#to delete product
@app.route('/productos/<string:id_nombre>', methods=['DELETE'])
def deleteProduct(id_nombre):
    producto = controller_productos.busca_producto(id_nombre)
    if producto!=None:
        #si el producto existe, entonces procedemos a eliminarlo
        resultado=controller_productos.elimina_producto(id_nombre)
        
        return jsonify({"Message":resultado,
                                "Producto" : producto})


#default entry
@app.route('/unprotected', methods=['GET'])
def unprotected():
    return jsonify({"FLASK":"APP!"})


#default entry
@app.route('/protected', methods=['GET'])
def protected():
    return jsonify({"FLASK":"APP!"})


#default entry
@app.route('/login', methods=['GET'])
def login():
    objeto_authen = request.authorization

    if objeto_authen and objeto_authen.password == 'password':

        token = jwt.encode({
            'user': objeto_authen.username, 
            'exp':datetime.datetimeutcnow() + datetime.timedelta(seconds=30)
            }, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could verify!',401, {'WWW-Authenticate':'Basic realm="Login Required"'})


#metodo main
if __name__== '__main__':
    app.run(debug=True,port=4000)

