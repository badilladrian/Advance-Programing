from marshmallow import Schema, fields, post_load

class MyObject:
    def __init__(self, identifier, name):
        self.identifier=identifier
        self.name = name
    def __repr__(self):
        description = "ID: {0} / {1}".format(self.identifier,self.name)
        return description

#this class inherites Schema
class MyObjectSchema(Schema):
    identifier = fields.Integer()
    name = fields.String()

    @post_load
    def create_object(self, data, **kwargs):
        return MyObject(**data)


#ask values
name, identifier = input("Ingrese nombre y ID: ").split()

#Dict to store the data to map
input_data = {
    "name": name,
    "identifier": identifier
    }

#obj = MyObject(21,"Adrian")
#objet = MyObject(ID=input_data["id"], name=input_data["name"])
#if we use the above approach the Int could be a string 

#schema object to then deserialize Complex -> Simple
schema = MyObjectSchema()

#Deserialize the data structure:
product = schema.load(data=input_data)

print(product)

#Now lets serialize the Simple -> Complex
complexObj = schema.dump(product)

print(complexObj)