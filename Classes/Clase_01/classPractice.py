class Worker:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


worker1 = Worker('Adrian', 'Badilla', '650000')
worker2 = Worker('Alfredo', 'Chinchilla', '4750000')

#print(worker1)
#print(worker2)

print(worker1.email)
#print(worker2.fullname())

#Todas las funciones de una clase siempre automaticamente reciben SELF como atributo
#razon cual por hay que cambiar ese llamado a la siguiente linea:
print(Worker.fullname(worker1))
