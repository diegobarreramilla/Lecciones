/*Une filas que tienen el mismo valor en una columna*/


SELECT vendedor, SUM(monto)
FROM ventas
GROUP BY vendedor;

---selecciona el nombre, suma edad de alumnos y unira los que tengan el mismo nombre
select nombre,sum(edad) from alumnos group by nombre 

---gr