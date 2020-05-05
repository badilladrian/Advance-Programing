# Python code for accessing attributes of class 
class emp: 
    name='Harsh'
    salary='25000'
    def show(self): 
        print (self.name)
        print (self.salary)

e1 = emp() 
# Use getattr instead of e1.name 
print (getattr(e1,'name'))
  
# returns true if object has attribute 
print (hasattr(e1,'name'))
  
# sets an  attribute  
setattr(e1,'height',152) 
  
# returns the value of attribute name height 
print (getattr(e1,'height')) 
  
# delete the attribute 
delattr(emp,'salary')


# Python code for accessing methods using static method 
class test: 
    @staticmethod
    def square(x): 
        test.result = x*x 
  
# object 1 for class 
t1=test() 
  
# object 2 for class 
t2 = test() 
t1.square(2) 
  
# printing result for square(2) 
print (t1.result)
t2.square(3) 
  
# printing result for square(3) 
print (t2.result)
  
# printing the last value of result as we declared the method static 
print (t1.result)


# Python code for Accessing attributes and methods 
# of one class in another class  
  
class ClassA(): 
    def __init__(self): 
        self.var1 = 1
        self.var2 = 2
  
    def methodA(self): 
        self.var1 = self.var1 + self.var2 
        return self.var1 
  
class ClassB(ClassA): 
    def __init__(self, class_a): 
        self.var1 = class_a.var1 
        self.var2 = class_a.var2 
  
object1 = ClassA() 
# updates the value of var1 
summ = object1.methodA() 
  
# return the value of var1 
print (summ)
  
# passes object of classA 
object2 = ClassB(object1) 
  
# return the values carried by var1,var2 
print (object2.var1)
print (object2.var2)


class Dog:
    """    
    Requires:
    legs - Legs so that the dog can walk.
    color - A color of the fur.
    """
    #the __init__ method of a Class
    #is always run at creation of new instance
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
        

    def bark(self):
        bark = "bark " * 2
        return bark


if __name__ == "__main__":
    dog = Dog(4, "brown")
    bark = dog.bark()
    print(bark)
    #Class DocString
    print(dog.__doc__)