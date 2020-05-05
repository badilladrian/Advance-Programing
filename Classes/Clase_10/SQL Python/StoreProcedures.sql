--Uso de Procedimientos Almacenados (semana 10)
--9.1. Definición del concepto de procedimiento almacenado en una base de datos relacional.
--Programa almacenado físicamente en una base de datos. 
SELECT 5 * 3 AS result;
https://carto.com/help/working-with-data/sql-stored-procedures/
SELECT *FROM customer;

--STORE PROCEDURES
[ <<label>> ]
[ DECLARE
    declarations ]
BEGIN
    statements;
   ...
END [ label ];
/* Como crear un store procedure
Como ejecutar un store procedure.*/
EXEC procedure_name;
--DO AND CREATE
-
DO
'<<first_block>>
DECLARE
  counter integer := 0;
BEGIN 
    counter := counter + 1;
    RAISE NOTICE ''The current value of counter is %'', counter;
END first_block';
- Se re-emplazan los '' por $$ 
--PRIMER EJEMPLO
DO 
$procedure$ 
DECLARE
   counter    INTEGER := 1;
   first_name VARCHAR(50) := 'John';
   last_name  VARCHAR(50) := 'Doe';
   payment    NUMERIC(11,2) := 20.5;
BEGIN 
   RAISE NOTICE '% % % has been paid % USD', counter, first_name, last_name, payment;
END 
$procedure$;

--STORE PROCEDURE ACTUALIZAR EL LENGUAJE
CREATE PROCEDURE actualizaLenguaje(lenguaje INT)
LANGUAGE SQL
AS 
$$
    UPDATE film 
    SET language_id = lenguaje
    WHERE language_id = 1;
$$;
/* Como formular un store procedure con parametros
Como ejecutar un store procedure con parametros.*/
call actualizalenguaje(3); --this is a comment 

9.2. Explicación de la sintaxis de un procedimiento almacenado en una base de datos relacional.
CREATE OR REPLACE PROCEDURE _nombre_ (parametros type)
LANGUAGE plpgsql or sql 
AS $$ abre === insert query ==== $$; cierra  


/* Creando un store procedure que permite desplegar un mensaje
esta vez utilizamos plpgsql y vemos la diferencia entre
la creacion de la tabla resultado y el contenido en consola.*/
CREATE OR REPLACE PROCEDURE display_message (INOUT mensaje TEXT)
AS $$
BEGIN
RAISE NOTICE 'Procedure Parameter: %', mensaje ;
END;
$$
LANGUAGE plpgsql ;
 --Llamamos el procedimiento almacenado 
call display_message('Mi primera prueba de print');
NOTICE:  Procedure Parameter: Mi primera prueba de print


CREATE PROCEDURE agregarCatergorias(lista_categorias VARCHAR(250))
AS
$procedure$
DECLARE
   categoria VARCHAR(40) := 'start';
   contador INT := 1;
    BEGIN
    WHILE categoria != '' 
        LOOP
        categoria := split_part(lista_categorias,',',contador);
        INSERT INTO category(name)
        VALUES(categoria);
        contador := contador+1;
        END LOOP;
    END;
$procedure$

call agregarCatergorias('micategoria,otracategoria');


9.3. Utilización de funciones en un procedimiento almacenado de una base de datos relacional.
A function is a reusable block of SQL code that returns a scalar value of a set of rows.
CREATE FUNCTION function_name(argument1 type,argument2 type)
RETURNS type AS
BEGIN
  staments;
END;
LANGUAGE 'language_name';

