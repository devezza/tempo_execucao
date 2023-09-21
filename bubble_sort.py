def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(0,tam-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

if __name__ == "__main__":
    lista = [2,3,4,1,5,2]
    bubble_sort(lista)
    print(lista)