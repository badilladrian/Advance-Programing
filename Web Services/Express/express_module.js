//importo el modulo express
var express = require('express');

//inicializo express() y lo guardo en un objeto
var app = express();

//creo mi servidor desde el objeto app y le asigno el puerto
//necesita una function para recibir las peticiones HTTP
var server = app.listen(3500, function() {});


/* por cada vez que se escuche una peticion, vamos a enrutar
el trafico a diferentes direcciones. Esto se realiza con un Router()*/
app.all('/', function(request, response) {
    response.send("He recibido tu request!");
})

//al definir el metodo de la app asi capturo relativo al HTTP method
app.get('/about', function(request, response) {
    response.send("Info About the page!");
})

//POST
app.post('/about', function(request, response) {
    response.send("Info About the page!");
})


//PUT
app.put('/about', function(request, response) {
    response.send("Info About the page!");
})


//DELETE
app.delete('/about', function(request, response) {
    response.send("Info About the page!");
})