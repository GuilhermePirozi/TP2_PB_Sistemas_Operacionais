import time

def partition(numeros, inicio, fim):
    meio = (inicio + fim) // 2
    numeros[meio], numeros[fim] = numeros[fim], numeros[meio]

    pivo = numeros[fim]
    indice = inicio - 1

    for atual in range(inicio, fim):
        if numeros[atual] <= pivo:
            indice += 1
            numeros[indice], numeros[atual] = (
                numeros[atual],
                numeros[indice],
            )

    numeros[indice + 1], numeros[fim] = (
        numeros[fim],
        numeros[indice + 1],
    )

    return indice + 1

def quickselect(numeros, inicio, fim, posicao):
    while inicio <= fim:
        posicao_pivo = partition(numeros, inicio, fim)

        if posicao_pivo == posicao:
            return numeros[posicao_pivo]

        if posicao < posicao_pivo:
            fim = posicao_pivo - 1
        else:
            inicio = posicao_pivo + 1

    raise ValueError("Posicao invalida")

def main():
    caminho = "/dados/numeros.txt"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        numeros = [int(valor) for valor in arquivo.read().split()]

    inicio = time.perf_counter()

    milesimo_menor = quickselect( numeros, 0, len(numeros) - 1, 999, )

    tempo = time.perf_counter() - inicio

    print(f"1000o menor numero: {milesimo_menor}")
    print(f"Tempo de execucao: {tempo:.6f} segundos")

if __name__ == "__main__":
    main()