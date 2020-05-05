SELECT
FROM
WHERE

INSERT into _table (columns)
VALUES (valores per columns)

INSERT INTO _table
SET column=value

DELETE 
FROM 
WHERE 
LIMIT; --Para definir cuantos

ALTER --database config
PRIVILEGES 

UPDATE --value inside table
SET 

LIKE--%final  inicia%
AND

ORDER BY _field_ asc--default/desc

SELECT tabla1.columna,
tabla1.columna,
tabla2.* FROM tabla1
INNER JOIN tabla2 ON tabla1.colum = tabla2.colum --match de ambas tablas
LEFT JOIN -- todos de tabla1 y los que match con tabla2 y NULL donde no
RIGHT JOIN --todos de tabla2 y los que match con tabla1 y NULL donde no
OUTER JOIN --TODOS los datos de ambas tablas Y MUESTRA LOS NULLS DONDE NO!
--el ON es necesario para indicar que estamos comparando!

AS -- alias en cualquier resultado

--Ejemplo! Despliega los nombres de ambas tablas donde la se intersecan mediante ID
SELECT
  E.Nombre as 'Empleado',
  D.Nombre as 'Departamento'
FROM Empleados E
JOIN Departamentos D
ON E.DepartamentoId = D.Id

