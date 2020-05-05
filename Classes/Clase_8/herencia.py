class Humano:
    def __init__(self, nombre, edad):
       self.firstname = nombre
       self.lastname = edad

    def printDatos(self):
       print(self.firstname, self.lastname)

personita = Humano("Pedrom", 89)
personita.printDatos

class Trabajador(Humano):
    pass

class TrabajadorParametrosPropios(Humano):
    def __init__(self, nombre, edad,salario):
        Humano.__init__(self, nombre, edad)
        self.salario=salario
    
    def printDatos(self):
           print("\nVengo del trabajador!: ")

    def printSalary(self):
        print(self.salario)


trabajadorcito = TrabajadorParametrosPropios("Juan",43,956250)
trabajadorcito.printDatos()
trabajadorcito.printSalary()

trabajadorcito.__getattribute__("salario")
trabajadorcito.__setattr__("salario",5000)
trabajadorcito.printSalary()
