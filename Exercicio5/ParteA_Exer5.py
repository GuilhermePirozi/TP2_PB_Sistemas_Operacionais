import time

def mochila_recursiva(itens, indice, capacidade, metricas):
    metricas["chamadas"] += 1

    if indice == len(itens) or capacidade == 0:
        return 0

    _, peso, valor = itens[indice]

    if peso > capacidade:
        return mochila_recursiva( itens, indice + 1, capacidade, metricas, )

    sem_item = mochila_recursiva( itens, indice + 1, capacidade, metricas, )

    com_item = valor + mochila_recursiva( itens, indice + 1, capacidade - peso, metricas, )

    return max(sem_item, com_item)

def main():
    caminho = "/dados/mochila.txt"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        quantidade, capacidade = map(
            int,
            arquivo.readline().split(),
        )

        itens = []

        for _ in range(quantidade):
            nome, peso, valor = arquivo.readline().split()
            itens.append((nome, int(peso), int(valor)))

    metricas = {"chamadas": 0}

    inicio = time.perf_counter()

    valor_maximo = mochila_recursiva( itens, 0, capacidade, metricas, )

    tempo = time.perf_counter() - inicio

    print("\n===== SOLUCAO RECURSIVA =====")
    print(f"Valor maximo: {valor_maximo}")
    print(f"Chamadas recursivas: {metricas['chamadas']}")
    print(f"Tempo de execucao: {tempo:.6f} segundos")

if __name__ == "__main__":
    main()