var suma = 2 + 3;

var nueva_suma = 20 + 45;

var resultado = suma + nueva_suma;

console.log(resultado);

function suma(datoA, datoB) {
    var resultado = datoA + datoB;
    return resultado;
}

suma(2, 3);

var resultado = suma(suma(2, 3), suma(20, 45));

//suma(5, 65)
console.log(resultado)