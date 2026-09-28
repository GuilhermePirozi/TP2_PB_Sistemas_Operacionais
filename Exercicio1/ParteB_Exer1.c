#include <ctype.h>
#include <dirent.h>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

#define _POSIX_C_SOURCE 200809L
#define DIRETORIO "/dados/arquivos"
#define MAX_ARQUIVOS 1000

typedef struct {
    char nome[256];
    long linhas;
    long palavras;
} Resultado;

int contar_palavras(const char *linha) {
    int palavras = 0;
    int dentro_palavra = 0;

    for (int i = 0; linha[i] != '\0'; i++) {
        if (isspace((unsigned char) linha[i])) {
            dentro_palavra = 0;
        } else if (!dentro_palavra) {
            palavras++;
            dentro_palavra = 1;
        }
    }

    return palavras;
}

void processar_arquivo(Resultado *resultado) {
    char caminho[512];
    char *linha = NULL;
    size_t tamanho = 0;

    snprintf(caminho, sizeof(caminho), "%s/%s",
             DIRETORIO, resultado->nome);

    FILE *arquivo = fopen(caminho, "r");

    if (arquivo == NULL) {
        printf("Erro ao abrir: %s\n", resultado->nome);
        return;
    }

    while (getline(&linha, &tamanho, arquivo) != -1) {
        resultado->linhas++;
        resultado->palavras += contar_palavras(linha);
    }

    free(linha);
    fclose(arquivo);
}

int main(void) {
    DIR *diretorio = opendir(DIRETORIO);

    if (diretorio == NULL) {
        printf("Nao foi possivel abrir %s\n", DIRETORIO);
        return 1;
    }

    Resultado resultados[MAX_ARQUIVOS] = {0};
    struct dirent *entrada;
    int quantidade = 0;

    while (quantidade < MAX_ARQUIVOS &&
           (entrada = readdir(diretorio)) != NULL) {
        if (entrada->d_name[0] != '.') {
            snprintf(resultados[quantidade].nome, 256,
                     "%s", entrada->d_name);
            quantidade++;
        }
    }

    closedir(diretorio);

    double inicio = omp_get_wtime();

    #pragma omp parallel for
    for (int i = 0; i < quantidade; i++) {
        processar_arquivo(&resultados[i]);
    }

    double tempo = omp_get_wtime() - inicio;

    for (int i = 0; i < quantidade; i++) {
        printf("%s\n", resultados[i].nome);
        printf("Linhas: %ld\n", resultados[i].linhas);
        printf("Palavras: %ld\n\n", resultados[i].palavras);
    }

    printf("Tempo total: %.6f segundos\n", tempo);

    return 0;
}