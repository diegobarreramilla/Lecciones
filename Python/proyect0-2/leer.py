def leer_entero(msg):
    while True:
        try:
             return int(input(msg))
        except:
            print("\nDebe ser un ENTERO")

def leer_texto(msg):
    
   while True:
       texto = input(msg)
       if texto != "" :
           return texto