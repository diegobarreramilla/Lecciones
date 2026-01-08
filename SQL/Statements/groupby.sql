/*Une filas que tienen el mismo valor en una columna*/


SELECT vendedor, SUM(monto)
FROM ventas
GROUP BY vendedor;

---gr