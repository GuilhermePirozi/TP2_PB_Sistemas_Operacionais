import asyncio
import time
from pathlib import Path

DIRETORIO = Path("/dados/arquivos")

def contar_arquivo(caminho):
    quantidade_linhas = 0
    quantidade_palavras = 0

    with caminho.open("r", encoding="utf-8", errors="replace") as arquivo:
        for linha in arquivo:
            quantidade_linhas += 1
            quantidade_palavras += len(linha.split())

    return caminho.name, quantidade_linhas, quantidade_palavras

async def processar_arquivo(caminho):
    return await asyncio.to_thread(contar_arquivo, caminho)

async def main():
    arquivos = sorted(
        caminho
        for caminho in DIRETORIO.iterdir()
        if caminho.is_file()
    )

    if not arquivos:
        print(f"Nenhum arquivo encontrado em {DIRETORIO}")
        return

    inicio = time.perf_counter()

    tarefas = [
        asyncio.create_task(processar_arquivo(caminho))
        for caminho in arquivos
    ]

    resultados = await asyncio.gather(*tarefas)

    fim = time.perf_counter()

    for nome, linhas, palavras in resultados:
        print(nome)
        print(f"Linhas: {linhas}")
        print(f"Palavras: {palavras}")
        print()

    print(f"Tempo total: {fim - inicio:.2f} segundos")

if __name__ == "__main__":
    asyncio.run(main())