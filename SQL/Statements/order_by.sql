---ordenar deacuerdo a uno de los atributos 


Select nombre,edad from alumnos order by edad

---Da el nombre y edadd de los alumnos ordenada por la edad

---Ordenar de manera DESCENDENTE Y ASCENDENTE

Select Alumno_id,nombre,salon from alumnos order by edad DESC

Select Alumno_id,nombre,salon from alumnos order by edad ASC


--- Dame todo de los alumnoes que edad = 17 y ordenalos por nombre de manera ascendete
Select * from alumnos where edad =17 order by nombre ASC