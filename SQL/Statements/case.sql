---case para delimitar ciertos escenarios encuantoa os datos que contamos
---evalua a toda la tabla  y crea una columna nueva
select *, ---seleccionamos todo 
case 
	when edad >15 then "Es apto" ---condicion
    else "no es apto" ---else
    end as aptitud ---alias del resultado para mejor legibilidad 
    from alumnos  --- de que tabla sacaremos la info

select * ,  
case 
	when edad >15 and promedio > 95.00 then "Es apto" 
    else "no es apto"
    end as aptitud
    from alumnos
    where nombre like "%Valeria%" --agregamos u where y un like para buscra un alumno en especifico