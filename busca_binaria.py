def busca_binaria(lista, alvo):
    esq = 0
    direita = len(lista)-1

    while esq <=direita:
        meio = (esq +direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esq = meio+1
        else:
            direita = meio-1
    return -1

if __name__ == "__main__":
    lista = [1,2,3,4,5,6]
    print(busca_binaria(lista,4))

