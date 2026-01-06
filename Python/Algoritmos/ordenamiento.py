#Listas implementacion 




# Lista EdD similar a un arreglo pero con mas funcionalidades directas
list = [1,1,5,6,9]

# Tupla EdD no se puede reasignar valores en la tupla
tupla = (12,35,1,41,1)

# Sets EdD no ordenada
my_set = {12,5,25,831,91,12}

# Dicts EdD  EdD de clave y valor que puede almacenar otras EdD

my_dict = {"Nombre":"Diego",
           "Apellido":"Barrera",
           "Edad":"20",
           "Lenguajes": ["python","java","C","SQL"],
           1:1.74}

other_dict = dict.fromkeys(my_dict)





#ordenar la lista con diferentes algortimos
lista_ordenada = funciones.insertion_sort(list)



print(tupla )
print(lista_ordenada)
print( my_set)

del my_dict["Lenguajes"][2]

print(my_dict.items())

other_dict["Nombre"] = "Valeria"
print(other_dict)





