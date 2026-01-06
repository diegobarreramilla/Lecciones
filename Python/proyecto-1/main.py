#ejercicio de practica 
#lista de contactos
import funciones

opc  = -1

#lista de contactos que contendra un dict generico
lista_contactos = []





while True:

    print("[1] Agregar contacto")
    print("[2] Eliminar contacto")
    print("[3] Editar informacion de contacto")
    print("[4] Mostra lista de contactos")
    print("[5] Buscar contacto")
    print("[0] Salir ")
    opc = int(input("Introduzca la opcion a realizar: "))

    if opc == 1:

        nombre = input("\nIntoduzca el nombre del nuevo contacto a agregar: \n")
        numero = int(input("\nIntroduzca el numero del nuevo contacto\n"))
        funciones.agregar_contacto(lista_contactos,nombre,numero)

    if opc == 2:
        contacto_eliminar = input("Introduzca el nombre del contacto que desee eliminar: ")

        if funciones.eliminar_contacto(lista_contactos,contacto_eliminar) == 1:
            print("Se elimino corectamente el contacto");
        else:
            print("El contacto no existe")

    if opc == 3:
        funciones.mostrar_lista(lista_contactos)
        contacto_modificar = input("introduzca el nombre del contacto a elimiar")

        if funciones.editar_contacto(lista_contactos,contacto_modificar) == 1:
            print("\nSe hizo el cambio\n")
        else:
            print("\nEl contacto no existe\n")



    if opc == 4:
        funciones.mostrar_lista(lista_contactos)

    if opc == 5:

        contacto_buscar = input("Introduzca el nombre del contacto que desea buscar: ")

        encontrado = funciones.buscar_contacto(lista_contactos,contacto_buscar)

        if encontrado == 1:
            print("\nEl contacto existe")
        elif encontrado == -1 :
            print("\nEl contacto no existe")

    if opc == 0:
        break
        







