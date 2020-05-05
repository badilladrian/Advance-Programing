/*Javascript es dinamico
//Lee las expresiones de izq -> dere

function toCelsius(fahrenheit) {
    return (5 / 9) * (fahrenheit - 32);
}

var fahrenheit = 77;
var temperatura = toCelsius(fahrenheit);

var text = "The temperature is " + temperatura + " Celsius\n" +
    "and the function is: " + toCelsius;

console.log(text);

//crea un objecto en modo diccionario, y utilizo una function como propiedad!
var person = {
    firstName: "John",
    lastName: "Doe",
    id: 5566,
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
};

console.log(person);
console.log("\n" + person.fullName());

//cls limpia el cmd

//npm install modulo + npm uninstall modulo /-- + scripts en package automatiza
//para correr usamos npm run init */

let calculos = {
    sumar: function(num1) {
        return num1 + 10;
    },
    multiplicar: function(num1) {
        return num1 * 5;
    }
}

console.log(calculos.multiplicar(7), calculos.sumar(2))

var person1 = {
        fullName: function() {
            return this.firstName + " " + this.lastName;
        }
    }
    //puedo generar funciones dentro de las propiedades de un elemento
    //y llamar otro objecto como parametro para esa propiedad!
    //puedo crear nuevas propiedades asignandoles un valor
person1.edad = 23;
que = person1.edad
console.log(que)

//asi creo un objecto con las propiedades del modulo moment
var moment = require('moment');

/* le asigno el format() y luego to String 
para que imprima le fecha y no el objecto*/
console.log(moment('1993-06-21').format('DD/MM/YY').toString());

/* Si no le asigno un path, el revisara automaticamente
mi carpeta de node_modules la cual es la default*/
var modulo = require('./miModulo');

numero = modulo.alCuadrado(4);
console.log("El resultado de ", 4, "Al cuadrado es: ", numero);


//MODULOS YA INTEGRADOS!
var http, url, path, fs = require('http'),
    require('url'), require('path'), require('fs');

console.log("--------", Math.floor(Math.random() * 100));


//Con nodemon puede reejecutar en cada actualizacion