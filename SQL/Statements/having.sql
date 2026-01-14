---filtra grupos junto con group by, usa funciones de agregacion

---selecciona el cliente y suma sus operaciones de la tabla ventas
---y junta cada operacion para el mismo cliente
---lo hace para lo que su suma total sea mayor a 1000
SELECT cliente, SUM(precio) AS total
FROM ventas
GROUP BY cliente
HAVING SUM(precio) > 1000;