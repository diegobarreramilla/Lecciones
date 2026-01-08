def agregar_contacto(lista_contactos: list,nombre:str,numero:int):


    if existe_contacto(lista_contactos,nombre,numero) == 0:
        contacto ={"Nombre":nombre,"Numero":numero}
        lista_contactos.append(contacto)
    else:
        print("\nEL contacto ya existe\n")

def eliminar_contacto(lista_contactos:list,nombre_eliminar: str):


    for i in range(len(lista_contactos)):
        
        #si en la posicion que va en la clave nombre es igual
        if nombre_eliminar == lista_contactos[i]["Nombre"]:
            #eliminar el numero 
            lista_contactos.pop(i)

            return 1
    return 0

def mostrar_lista(lista_contactos:list):
    print("\nNombre ----- Numero\n")

    for contacto in lista_contactos:


        print(contacto["Nombre"] , contacto["Numero"])
    print("\n")


def buscar_contacto(Lista_contactos: list, nombre: str):

    for i in range(len(Lista_contactos)):
        if Lista_contactos[i]["Nombre"] == nombre:
            return 1
    return -1


def editar_contacto(lista_contactos:list,contacto:str):

  
        for i in range(len(lista_contactos)):
            if(lista_contactos[i]["Nombre"] == contacto):
                nuevo_numero = int(input("\nIntroduzca el nuevo numero de contacto: "))
                lista_contactos[i]["Numero"] = nuevo_numero
                return 1
        return 0
                    
def existe_contacto(lista_contactos: list,nombre:str,numero:int):

    for i in range(len(lista_contactos)):
        if nombre == lista_contactos[i]["Nombre"] or numero == lista_contactos[i]["Numero"]:
            return 1
    return 0     


    