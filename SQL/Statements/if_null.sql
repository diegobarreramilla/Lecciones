---esta funcon reemplazxa el valor de null por algun valor que determinemos nosotros

select *  ,ifnull(edad,0) from alumnos
        ---si la edad es null pone 0

