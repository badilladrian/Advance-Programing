from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init my flask app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#Database creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'mydb.db')

#Init SQLAlchemy
database = SQLAlchemy(app)

#Init Marshmallow
marshmallow = Marshmallow(app)

#To create DBA
"""python shell-> from file import database

REPL:
from marshmallow_rest import database
database.create_all()
from marshmallow_rest import Device, Sensor
cpu = Device(name='CPU',latency=1.15)       
ram = Device(name='RAM', latency=3.15)
database.session.add_all([cpu,ram])
database.session.commit()
healthy_fan=Sensor(name='Fan', device_ID=2)
procesor=Sensor(name='I6', device_ID=1)     
database.session.commit()


"""

#Define my class Models
class Device(database.Model):
   ID = database.Column(database.Integer, primary_key=True)
   name = database.Column(database.String(100))
   latency = database.Column(database.Float)

   """def __init__(self, name, latency):
       self.name = name
       self.latency=latency"""

class Sensor(database.Model):
   ID = database.Column(database.Integer, primary_key=True)
   name = database.Column(database.String(50))
   device_ID = database.Column(database.Integer, database.ForeignKey('device.ID')) #FOREIGNKEY
   device = database.relationship('Device', backref= 'sensor') #RELATIONSHIP

#We define Device Schema
#this works to parse from obj Model (SQLAlchemy)
#to a readable JSON obj
class DeviceSchema(marshmallow.Schema):
    class Meta:
        model = Device


#Init Schema
device_schema = DeviceSchema()#if just one instance
devices_schema = DeviceSchema(many=True)#if multiply instances

#Routing
@app.route('/')
def index():
    #the device model itself is not JSON serialiazable
    first_device = Device.query().filter_by(name="CPU") #take the first from table
    print(first_device)
    device_data = device_schema.dump(first_device) #deserialize
    return jsonify({'Device':device_data})
 

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

@app.route('/device/<int:ID>', methods=['GET'])
def fetch_one():
    devices = Device.query.all()
    #now devices has all the models
    devices_data = devices_schema.dump(devices) #deserialize

    return jsonify({'Device':devices_data})

#Run server
if __name__ == '__main__':
    app.run(debug=True)
