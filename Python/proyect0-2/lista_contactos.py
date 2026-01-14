
import contacto

class ListaContactos:
    #esta clase en si solo es una lista
    def __init__(self):
        self.lista = []

    #agregramos al final el nuevo contacto
    def agregar_contacto_lista(self,contacto:contacto):
        self.lista.append(contacto)


    def buscar_contacto(self,nombre:str):

        for contacto in self.lista:
            if contacto.nombre == nombre:
                return contacto
        return None
    
    def eliminar_contacto(self,contacto:contacto):

        
            self.lista.remove(contacto)
        
        
    def update_numero_contacto(self,contacto:contacto,numero:int):
        if contacto != None:
            contacto.numero = numero
            return True
        return False
    
    def desplegar_contactos(self):
        
        if self.lista != None:

            for i,contacto in enumerate(self.lista):
                print(i+1,contacto )
        else:
            return None
        
    def num_contactos(self):

        return len(self.lista)
        