/*Aqui vemos la ejecucion de una clase
en JS, ademas vemos la funcionalidad de herencia mediante
la palabra reservada EXTENDS */

class Car {
    //constructor que recibe la marca
    constructor(brand) {
        this.carname = brand;
    }

    //despliega el atributo carname
    presentarse() {
        return 'Yo soy un: ' + this.carname;
    }
}

//Clase que hereda de CARRO
class Model extends Car {
    constructor(brand, mod) {
            //al definir super() digo que este atributo va a la clase padre
            super(brand);
            //model tiene el modelo del auto
            this.model = mod;
        }
        //una version mas especifica de mostrase llamando al metodo padre ()
    show() {
        return this.presentarse() + ', y mi modelo es: ' + this.model;
    }
}

mi_auto = new Model("Soy la marca del padre!", "Soy el modelo del hijo");

console.log(mi_auto);
console.log(mi_auto.presentarse());
console.log(mi_auto.show());