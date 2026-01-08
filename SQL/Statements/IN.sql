/*encontrar todos las 
instancias que contenga un valor
 especifico en una columna*/ 



---ejemplos, muestra todos los alumos que tenga su edad = 17 y 15
select * from alumnos where edad in(17,15)

/*ejemplo donde muestra los usuarios 
que se llamen de esa forma, no case sensitive*/

select * from alumnos where nombre in('diego barrera milla', 'ivan riggo')