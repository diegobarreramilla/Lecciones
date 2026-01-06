def agregar_contacto(lista_contactos: list,nombre:str,numero:int):

    contacto ={"Nombre":nombre,"Numero":numero}
    lista_contactos.append(contacto)

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

    for i in range(len(lista_contactos)):


        print(lista_contactos[i]["Nombre"] , lista_contactos[i]["Numero"])


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
                    
         


    