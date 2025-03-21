#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOME 50
#define MAX_ENDERECO 100
#define MAX_TELEFONE 15
#define MAX_ROTAS 100

typedef struct Cliente {
    char nome[MAX_NOME];
    char endereco[MAX_ENDERECO];
    char telefone[MAX_TELEFONE];
    struct Cliente *proximo;
} Cliente;

typedef struct Rota {
    Cliente *cliente;
    int tentativas;
    struct Rota *proxima;
} Rota;

typedef struct Devolucao {
    Rota *rota;
    struct Devolucao *proximo;
} Devolucao;

Cliente *primeiro_cliente = NULL;
Rota *primeira_rota = NULL;
Rota *ultima_rota = NULL;
Devolucao *primeira_devolucao = NULL;

void adicionar_cliente(char nome[], char endereco[], char telefone[]) {
    Cliente *novo_cliente = (Cliente *) malloc(sizeof(Cliente));
    strcpy(novo_cliente->nome, nome);
    strcpy(novo_cliente->endereco, endereco);
    strcpy(novo_cliente->telefone, telefone);
    novo_cliente->proximo = primeiro_cliente;
    primeiro_cliente = novo_cliente;
}

void adicionar_rota(Cliente *cliente) {
    Rota *nova_rota = (Rota *) malloc(sizeof(Rota));
    nova_rota->cliente = cliente;
    nova_rota->tentativas = 0;
    nova_rota->proxima = NULL;
    if (primeira_rota == NULL) {
        primeira_rota = nova_rota;
        ultima_rota = nova_rota;
    } else {
        ultima_rota->proxima = nova_rota;
        ultima_rota = nova_rota;
    }
}

void adicionar_devolucao(Rota *rota) {
    Devolucao *nova_devolucao = (Devolucao *) malloc(sizeof(Devolucao));
    nova_devolucao->rota = rota;
    nova_devolucao->proximo = primeira_devolucao;
    primeira_devolucao = nova_devolucao;
}

void remover_rota() {
    if (primeira_rota == NULL) {
        return;
    }
    Rota *rota_removida = primeira_rota;
    primeira_rota = primeira_rota->proxima;
    free(rota_removida);

    if (primeira_rota == NULL) {
        ultima_rota = NULL;
    }
}

int main()
{
    adicionar_cliente("Joao", "Rua 1", "1234-5678");
    adicionar_cliente("Maria", "Rua 2", "8765-4321");
    adicionar_cliente("Jose", "Rua 3", "1357-2468");
    adicionar_cliente("Ana", "Rua 4", "8642-7531");

    adicionar_rota(primeiro_cliente);
    adicionar_rota(primeiro_cliente->proximo);
    adicionar_rota(primeiro_cliente->proximo->proximo);
    adicionar_rota(primeiro_cliente->proximo->proximo->proximo);

    adicionar_devolucao(primeira_rota);
    adicionar_devolucao(primeira_rota->proxima);
    adicionar_devolucao(primeira_rota->proxima->proxima);
    adicionar_devolucao(primeira_rota->proxima->proxima->proxima);

    while (primeira_devolucao != NULL) {
        Devolucao *devolucao_removida = primeira_devolucao;
        primeira_devolucao = primeira_devolucao->proximo;
        free(devolucao_removida);
    }

    while (primeira_rota != NULL) {
        remover_rota();
    }

    while (primeiro_cliente != NULL) {
        Cliente *cliente_removido = primeiro_cliente;
        primeiro_cliente = primeiro_cliente->proximo;
        free(cliente_removido);
    }
}