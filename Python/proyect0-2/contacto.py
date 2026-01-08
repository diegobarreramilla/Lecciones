class contacto:
    
    def __init__(self,nombre:str,numero:int):
        self.nombre = nombre
        
        self.numero = numero

    def __str__(self):
        return f" Nombre: {self.nombre} | Numero: {self.numero}"
    
    


