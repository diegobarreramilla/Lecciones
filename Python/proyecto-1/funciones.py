#numero de veces que dara la vuelt

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
