var misFuncionesAdrian = {
    alCuadrado: function(num1) {
        return num1 ** 2;
    },
    divMod: function(num1) {
        return num1 % 2;
    }
}

/*para moder importar mi propio modulo a otros JS
utilizo el modulo integrado moodule con la propiedad exports
y le asigno a este, mi modulo!*/

module.exports = misFuncionesAdrian;

/* QUE ES NODE JS:
Node. js is a server-side platform built on Google Chrome's Javascript Engine
 (V8 Engine) which compiles Javascript code into Machine code. 
 Node.js uses an event-driven, non-blocking I/O model that makes 
 it lightweight and efficient.*/