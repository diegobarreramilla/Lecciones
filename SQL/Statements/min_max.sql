---obtener el maximo y minino de valores de columna de todas las instancias


/*
esto solo da el valor maximo de la edad, no da informacion relacionada
a la instancias que le corresponde, da el valor min o maximo no cuantas veces 
existe en la tabla ni a quien le pertenece se podra buscar facilmente despues
*/
Select max(edad) from alumnos

---resultado = 17 por ejemplo

select min(edad) from alumnos

---resultado = 15 por ejemplo