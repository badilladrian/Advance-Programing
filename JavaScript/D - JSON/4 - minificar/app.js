var tienda = { nombre: "Tienda las 4 esquinas", calcular: function(n, a) { return n + a }, saludar: function() { return "Hola " } },
    btnSaludar = document.getElementById("btnSaludar");
btnSaludar.addEventListener("click", function() { console.log(tienda.saludar()) });
//podemos usar compresores de codigo
console.log("Nuestro código ha sido minimizado");
console.log(tienda.nombre);
console.log(tienda.calcular(20, 32));
console.log(tienda.saludar());