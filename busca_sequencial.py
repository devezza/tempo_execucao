def busca_sequencial(lista, valor):
    for i in lista:
        if i == valor:
            return i
    return -1
if __name__ == "__main__":
    lista = [1,2,3,4]
    res = busca_sequencial(lista,3)
    print(res) 