#ALGORITMOS DE ORDENAMIENTO

#numero de veces que dara la vuelta

def bubble_sort(list):
    for i in range(len(list)):
    #indice que seguiremos
    #-1 por que no queremos comprar el ultimo con nada y -i por que ya estaria ordenado lo demas
        for j in range(len(list)-1 -i):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list



def insertion_sort(list):

    
    for i in range(1,len(list)):

        actual = list[i]
        anterior_ordenado= i-1

        while anterior_ordenado >= 0 and list[anterior_ordenado] > actual:
            list[anterior_ordenado+1] = list[anterior_ordenado]
            anterior_ordenado -= 1
            list[anterior_ordenado + 1] = actual
    return list
            


