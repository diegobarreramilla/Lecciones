---editar la estructura de un atbal directamnete
                    ---agregar una columna
alter table alumnos add apellido varchar(50)


                    ---renombrar una columna
alter table alumnos rename apellido to surname 

                    ---modificar una columna especifica
alter table alumnos modify column nombre varchar(100)

                    ---elimina unaa columna completa
alter table alumnos drop column nombre 