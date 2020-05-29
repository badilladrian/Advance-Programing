from marshmallow import Schema, fields, post_load, ValidationError, validate, validates

"""VALIDATION ONLY HAPPENS WHEN DESERIALIZE"""

class MyObject:
    def __init__(self, identifier, name, supplier):
        self.identifier=identifier
        self.name = name
        self.supplierEmail = supplier

    def __repr__(self):
        description = "ID: {0} / {1}".format(self.identifier,self.name)
        return description




#this class inherites Schema
class MyObjectSchema(Schema):
    identifier = fields.Integer()
    name = fields.String(validate=validate.Length(max=7))#sent that the arg to validate is validate() and can't be beyond 7
    supplierEmail = fields.Email()
    location = fields.String(required=True) # while show this missing

    #custom validation
    @validates('identifier')
    def validation_identificator(self, ident):
        if (ident*-1)>0:
            raise ValidationError("The ID can't be negative!")

    @post_load
    def create_object(self, data, **kwargs):
        return MyObject(**data)


#ask values
name, identifier, email = input("Ingrese nombre,ID,Email: ").split(",")

#Dict to store the data to map to Obj
input_data = { #this is my complex object
    "name": name,
    "identifier": identifier,
    "supplierEmail": email,
    }

#obj = MyObject(21,"Adrian")
#objet = MyObject(ID=input_data["id"], name=input_data["name"])
#if we use the above approach the Int could be a string and
#there is no validation.

"""Using Marshmallow beyond serielize and deserialize,
we can add set of -rules= in the schema definition"""
try:
    #schema object to then deserialize Complex -> Simple
    schema = MyObjectSchema()
    #Deserialize the data structure:
    product = schema.load(input_data)
    #print(product)

    #Now lets serialize the Simple -> Complex
    complexObj = schema.dump(product)
    print(complexObj)


except ValidationError as error:
    print("This is wrong:" ,error)
    print("This is correct:", error.valid_data)

