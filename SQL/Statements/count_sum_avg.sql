/*statement que cuneta cuantas instancias o 
filas cuentas con una columna o atributo en especifico*/

select count(edad) form alumnos

--- da el valo int que le pertence a la operacion

/*
statement que suma los valores de las columnas de todas las instancias
*/

select sum(edad) from alumnos 

---da el valor de la suma de todas las edades registradas


select avg(edad) from alumnos