---Quiere decir que contine o que se parece

---Da toda la info de los alumnos que en su nombre contenga Barrera y los ordena por id
Select * from alumnos where nombre like "%Barrera%" order by Alumno_id

--- '%' = quiere decir que hay algo o antes o depues que no nos interesa en la busqueda


---Muestra toda la info de los alumnos que su promedio inicie con un 9
---No le importa lo que sigue despues del 9 solo que lo contenga al principio
---Apesar de que el promedio es un DECIMAL() se usa "", para el &
Select * from alumnos where promedio like "9%" order by promedio DESC
