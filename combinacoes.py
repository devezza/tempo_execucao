def combinacoes(conjunto):
    if len(conjunto) == 0:
        return [[]]
    sem_primeiro = combinacoes(conjunto[1:])
    com_primeiro = []
    for comb in sem_primeiro:
        com_primeiro.append([conjunto[0]]+ comb)
    return sem_primeiro + com_primeiro

if __name__ == "__main__":
    print(combinacoes([1,2,3,4]))