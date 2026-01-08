--Identificar los usuarios que continene null en alguna columna 

---ejmeplo null en edad y mandar notificacion a usuario de rellenar el campo

Select * from alumnos where edad is null

---delimitar los usuario que si tienen algo diferente a null en cierta columna

select * from alumnos where correo is not null