
class MisProductos():

    def __init__(self):
        self.productos = [
                {"nombre": "laptop", "precio":800, "cantidad":5},
                {"nombre": "mouse", "precio":40, "cantidad":10},
                {"nombre": "monitor", "precio":400, "cantidad":3},
            ]

  
    def busca_producto(self, name):
        for dictionario in self.productos:
            if dictionario['nombre']==name:
                return dictionario

    
    def actualiza_producto(self,id_name,nom,prec,cant):
        producto = self.busca_producto(id_name)

        nombre = nom
        precio = prec
        cantidad = cant

        if producto==None:
            return None
        else:
            producto['nombre']= nombre
            producto['precio']= precio
            producto['cantidad']= cantidad
            return "Producto actualizado!"
    
    def elimina_producto(self,id_name):
        producto = self.busca_producto(id_name)
        self.productos.pop(self.productos.index(producto))
        return "Producto eliminado!"


