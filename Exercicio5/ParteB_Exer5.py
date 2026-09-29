import time

def mochila_dinamica(itens, capacidade):
    quantidade = len(itens)
    tabela = [
        [0] * (capacidade + 1)
        for _ in range(quantidade + 1)
    ]
    estados = 0

    for indice in range(1, quantidade + 1):
        _, peso, valor = itens[indice - 1]

        for capacidade_atual in range(capacidade + 1):
            estados += 1

            if peso > capacidade_atual:
                tabela[indice][capacidade_atual] = ( tabela[indice - 1][capacidade_atual] )
            else:
                sem_item = tabela[indice - 1][capacidade_atual]
                com_item = ( valor + tabela[indice - 1][capacidade_atual - peso] )

                tabela[indice][capacidade_atual] = max( sem_item, com_item, )

    return tabela[quantidade][capacidade], estados

def main():
    caminho = "/dados/mochila.txt"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        quantidade, capacidade = map( int, arquivo.readline().split(),)

        itens = []

        for _ in range(quantidade):
            nome, peso, valor = arquivo.readline().split()
            itens.append((nome, int(peso), int(valor)))

    inicio = time.perf_counter()

    valor_maximo, estados = mochila_dinamica( itens, capacidade, )

    tempo = time.perf_counter() - inicio

    print("\n===== PROGRAMACAO DINAMICA =====")
    print(f"Valor maximo: {valor_maximo}")
    print(f"Estados calculados: {estados}")
    print(f"Tempo de execucao: {tempo:.6f} segundos")

if __name__ == "__main__":
    main()