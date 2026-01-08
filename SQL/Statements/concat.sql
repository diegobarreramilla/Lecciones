/*
hace cadenas de texto para poder leer mejor datos de la tala

*/

select concat("Nombre: ",nombre," Tiene ",edad," anios", ' es menor de edad') from alumnos where edad < 18


---Nombre: Diego Barrera Milla Tiene 17 anios es menor de edad

select concat("Nombre: ",nombre," Tiene ",edad," anios", ' es menor de edad') as "Infomacion legal" from alumnos where edad < 18

/*
podemos cambiar el nombre de la columna temporal para
desplegar informacion mas efectiva
 */