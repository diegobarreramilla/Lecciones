---Nos ayuyda a encontrar datos con atributos especificos 

Select * from alumnos where edad = 17 
---De toda la informacion de  los alumnos dame los que edad = 17

Select salon from alumnos where edad = 17 
---Da solo el salon del alumoo que tenga edad = 17



---agregamos el uso de operadores logicos 
Select * from alumnos where edad = 17 or edad = 15


Select * from alumnos where edad = 17 and edad = 15

Select * from alumnos where  not edad = 17 

---Buscar en rangos
Select * from alumnos where promedio >= 90.00 and promedio <= 95.00
