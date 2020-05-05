var objeto_tienda = {
    nombre: "Tienda de Software",
    calcular_total: function(costo1, costo2) {
        return costo1 + costo2;
    },
    saludar_usuario: function() {
        var mensaje = "Hola ";
        return mensaje;
    }
};

var btnSaludar = document.getElementById("btnSaludar");

btnSaludar.addEventListener('click', function() {
    console.log(objeto_tienda.saludar_usuario());
});