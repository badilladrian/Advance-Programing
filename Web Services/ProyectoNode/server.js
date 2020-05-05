var http = require('http');

/*creo un server con el modulo, y recibe un eventListener
voy a definir parametros de request y response
siendo que el primer parametro es:IncomingMessage
y el segundo es el ServerRespose. */
var server = http.createServer(function(request, response) {

    response.writeHead(200, { 'Content-type': 'text/html' });
    response.write("Respuesta para la direccion: " + request.url);

    console.log("peticion web!");
})

//que puerto esta escuchando eventos
server.listen(3000);

//Al correrse el JS
console.log("Ejecutando el Servidor NodeJS!");