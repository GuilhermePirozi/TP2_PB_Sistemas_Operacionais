import time

def partition(numeros, inicio, fim, metricas):
    meio = (inicio + fim) // 2
    numeros[meio], numeros[fim] = numeros[fim], numeros[meio]

    pivo = numeros[fim]
    indice = inicio - 1

    for atual in range(inicio, fim):
        metricas["comparacoes"] += 1

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

def quicksort(numeros, inicio, fim, metricas):
    if inicio < fim:
        posicao = partition(numeros, inicio, fim, metricas)

        metricas["chamadas"] += 2

        quicksort(numeros, inicio, posicao - 1, metricas)
        quicksort(numeros, posicao + 1, fim, metricas)

def main():
    caminho = "/dados/numeros.txt"
    metricas = {
        "comparacoes": 0,
        "chamadas": 0,
    }

    with open(caminho, "r", encoding="utf-8") as arquivo:
        numeros = [int(valor) for valor in arquivo.read().split()]

    inicio = time.perf_counter()
    quicksort(numeros, 0, len(numeros) - 1, metricas)
    milesimo_menor = numeros[999]
    tempo = time.perf_counter() - inicio

    print(f"1000o menor numero: {milesimo_menor}")
    print(f"Comparacoes: {metricas['comparacoes']}")
    print(f"Chamadas recursivas: {metricas['chamadas']}")
    print(f"Tempo de execucao: {tempo:.6f} segundos")

if __name__ == "__main__":
    main()