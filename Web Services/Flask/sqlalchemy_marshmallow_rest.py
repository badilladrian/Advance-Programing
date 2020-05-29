from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init my flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init db
database = SQLAlchemy(app)
#To create DBA
"""python shell-> from file import database
database.create_all()"""

#Init Marshmallow
marshmallow = Marshmallow(app)

#Define my class object
class Device(database.Model):
   id = database.Column(database.Integer, primary_key=True)
   name = database.Column(database.String(100))
   latency = database.Column(database.Float)

   def __init__(self, name, latency):
       self.name = name
       self.latency=latency


#We define Device Schema
#this works to parse from obj Model (SQLAlchemy)
#to a readable JSON obj
class DeviceSchema(marshmallow.Schema):
    class Meta:
        readable_fields = ('id', 'name', 'latency')

#Init Schema
device_schema = DeviceSchema()#if just one instance
devices_schema = DeviceSchema(many=True)#multiply instances

#Routing
@app.route('/device', methods=['POST'])
def create_device():
    #capturing data that comes into the API
    name = request.json['name']
    latency = request.json['latency']
    #new instance of the class Device
    new_device = Device(name,latency)

    #adding it to the DBA
    database.session.add(new_device)
    database.session.commit()

    #veamos el schema
    schem =  device_schema.jsonify(new_device)
    print(schem)

    return schem

@app.route('/devices', methods=['GET'])
def fetch_all():
    devices = Device.query.all()
    #now devices has all the models

    #we need to parsethe response to JSON
    response = devices_schema.dump(devices)
    return jsonify(response)

#Run server
if __name__ == '__main__':
    app.run(debug=True)
