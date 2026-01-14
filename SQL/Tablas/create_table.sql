---crear una tabla en una base datos

create table participantes(
    ---nombre atributo - tipo de dato y constrains
    id int NOT NULL AUTO_INCREMENT,
    nombre varchar(50) NOT NULL,
    edad int,
    boletos int NOT NULL default 1,
    pais varchar(15) NOT NULL,
    UNIQUE(nombre) ---unico
    PRIMARY KEY(id) ---identificador
    CHECK edad > 17 ---no deja agregar datos que tengan edad menor a 18

)