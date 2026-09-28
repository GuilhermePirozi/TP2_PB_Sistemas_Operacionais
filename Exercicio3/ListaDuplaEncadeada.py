import time

class No:
    def __init__(self, valor):
        self.anterior = None
        self.valor = valor
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.inicio

        if self.inicio is None:
            self.fim = novo
        else:
            self.inicio.anterior = novo

        self.inicio = novo

    def inserir_final(self, valor):
        novo = No(valor)
        novo.anterior = self.fim

        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo

        self.fim = novo

    def buscar(self, valor):
        atual = self.inicio

        while atual is not None:
            if atual.valor == valor:
                return atual

            atual = atual.proximo

        return None

    def remover(self, valor):
        atual = self.buscar(valor)

        if atual is None:
            return False

        if atual.anterior is None:
            self.inicio = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual.proximo is None:
            self.fim = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior

        return True

    def listar_inicio_fim(self):
        valores = []
        atual = self.inicio

        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo

        return " -> ".join(valores)

    def listar_fim_inicio(self):
        valores = []
        atual = self.fim

        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.anterior

        return " -> ".join(valores)

def medir_busca(lista, valor):
    inicio = time.perf_counter()
    lista.buscar(valor)
    return time.perf_counter() - inicio

def main():
    lista = ListaDuplamenteEncadeada()

    for valor in [10, 20, 30, 40, 50]:
        lista.inserir_final(valor)

    lista.remover(30)

    print(lista.listar_inicio_fim())
    print(lista.listar_fim_inicio())

    teste = ListaDuplamenteEncadeada()

    for valor in range(1, 100001):
        teste.inserir_final(valor)

    tempo_inicio = medir_busca(teste, 10)
    tempo_meio = medir_busca(teste, 50000)
    tempo_final = medir_busca(teste, 99990)

    print()
    print(f"Busca proxima ao inicio: {tempo_inicio:.9f} segundos")
    print(f"Busca proxima ao meio: {tempo_meio:.9f} segundos")
    print(f"Busca proxima ao final: {tempo_final:.9f} segundos")

if __name__ == "__main__":
    main()