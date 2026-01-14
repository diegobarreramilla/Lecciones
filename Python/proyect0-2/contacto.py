class contacto:

    #constructor del objeto
    def __init__(self,nombre:str,numero:int,ubicacion = "Tijuana"):
        #atriubutps del objto
        self.nombre = nombre
        self.numero = numero
        self.ubicacion = ubicacion

    #toString del objeto
    def __str__(self):
        return f" Nombre: {self.nombre} | Numero: {self.numero} | Ubicacion: {self.ubicacion}"
    
    


