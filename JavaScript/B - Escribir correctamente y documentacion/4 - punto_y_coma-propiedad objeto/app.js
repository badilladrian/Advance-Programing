var tienda = {
    nombre: "Tienda las 4 esquinas", //se pueden definir
    calcular: function(costo1, costo2) {
        return costo1 + costo2;
    }, //fuciones en las propiedades de un objeto
    saludar: function() {
        var mensaje = "Hola ";
        return mensaje;
    }
};

var btnSaludar = document.getElementById("btnSaludar");
//y podemos llamar la funcion dentro de un objeto sin haber definido
//la funcion por fuera del mismo
btnSaludar.addEventListener('click', function() {
    console.log(tienda.saludar());
});