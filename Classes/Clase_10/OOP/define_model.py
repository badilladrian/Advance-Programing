#model class

# Python code for accessing attributes of class 
class Model: 
    #global attributes
    name='Harsh'
    salary='25000'

    #self prints
    def show(self): 
        print (self.name)
        print (self.salary)

    """All the methods () of a Python Class needs self is a parameter.
    Unless the metod is static. In which case is no needed.
    There are Python integrated functions:
    getattr() 
    hasattr() 
    setattr()
    & delattr()"""
    def get_name(self):
        print (getattr(self,'name'))

    def get_salary(self):
        print (getattr(self,'salary'))


ejemplo = Model();
ejemplo.show()
ejemplo.get_name();
ejemplo.get_salary();
