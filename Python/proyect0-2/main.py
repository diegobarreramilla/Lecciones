

import lista_contactos
import contacto

principal = lista_contactos.ListaContactos()

opc = -1
while True:
    

    print("\n[1] Agregar contacto" )
    print("[2] Editar contacto" )
    print("[3] Elimianr contacto" )
    print("[4] Mostrar contactos" )
    print("[5] Buscar contacto" )
    print("[0] Salir del programa" )
    opc = int(input("INtroduzca la opcion: "))



    if opc == 1:
        nombre = input("\nIntroduzca el nombre del contacto: ")
        numero = int(input("\nIntroduzca el numero: "))

        contacto_nuevo = contacto.contacto(nombre,numero)
        principal.agregar_contacto_lista(contacto_nuevo)


    elif opc == 2:
        
        nombre_editar = input("\nIntroduzca el nombre del contacto al que cambiara el numero: ")
        contacto_editar = principal.buscar_contacto(nombre_editar)
        

        if  contacto_editar in principal.lista:
            nuevo_numero = int(input("\nIntroduzca el numero nuevo:"))
            principal.update_numero_contacto(contacto_editar,nuevo_numero)
        else:
            print("\nEl contacto no existe ")
            
        
    elif opc == 3:
        nombre_eliminar = input("\nIntroduzca el nombre del contacto que desee eliminar: ")
        contacto_eliminar = principal.buscar_contacto(nombre_eliminar)

        if contacto_eliminar in principal.lista:
            principal.eliminar_contacto(contacto_eliminar)
            print("\nEl contacto fue eliminado")
        else:
            print("\nEl contacto no existe")

    elif opc == 4:
        print("\n")
        
        principal.desplegar_contactos()


    elif opc == 5:
        nombre_buscar = input("Introduzca el nombre del contacto a buscar: ")
        contacto_buscar = principal.buscar_contacto(nombre_buscar)

        if contacto_buscar != None:
            print("\nSi existe\nNombre: ",contacto_buscar.nombre," Numero: ", contacto_buscar.numero)
        else:
            print("\nEl contact no existe")
    




    if opc == 0:
        break