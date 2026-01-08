--cambia elnombre de un campo SOLO para la consulta que realicemos 

/* Este statement pide la edad, nombre y su id pero lo cambia
de nombre durante la ejecucuion para gacerlo mas sencillo de 
entender durante la misma
*/

select edad,nombre,Alumno_id as 'ID' from alumnos where edad is not null

