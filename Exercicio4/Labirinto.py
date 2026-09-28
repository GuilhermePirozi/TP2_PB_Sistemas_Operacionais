def localizar(labirinto, simbolo):
    for linha, conteudo in enumerate(labirinto):
        for coluna, valor in enumerate(conteudo):
            if valor == simbolo:
                return linha, coluna

    return None

def percorrer(labirinto, linha, coluna, visitados):
    if labirinto[linha][coluna] == "E":
        return True

    visitados.add((linha, coluna))

    movimentos = [ (-1, 0), (1, 0), (0, -1), (0, 1), ]

    for movimento_linha, movimento_coluna in movimentos:
        nova_linha = linha + movimento_linha
        nova_coluna = coluna + movimento_coluna

        dentro = (
            0 <= nova_linha < len(labirinto)
            and 0 <= nova_coluna < len(labirinto[nova_linha])
        )

        if not dentro:
            continue

        if labirinto[nova_linha][nova_coluna] == "#":
            continue

        if (nova_linha, nova_coluna) in visitados:
            continue

        if percorrer( labirinto, nova_linha, nova_coluna, visitados,):
            if labirinto[linha][coluna] == " ":
                labirinto[linha][coluna] = "."

            return True

    return False

def main():
    caminho = "/dados/labirinto.txt"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        labirinto = [
            list(linha.rstrip("\n"))
            for linha in arquivo
        ]

    inicio = localizar(labirinto, "S")
    saida = localizar(labirinto, "E")

    if inicio is None or saida is None:
        print("Inicio ou saida nao encontrados.")
        return

    encontrou = percorrer( labirinto, inicio[0], inicio[1], set(), )

    print("\n===== LABIRINTO =====")

    for linha in labirinto:
        print("".join(linha))

    if encontrou:
        print("\nCaminho encontrado!")
    else:
        print("\nNenhum caminho encontrado!")

if __name__ == "__main__":
    main()