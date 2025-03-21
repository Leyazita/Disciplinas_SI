#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cliente.h"

Cliente *criar_cliente(char *nome, char *endereco) {
    Cliente *novo_cliente = (Cliente *) malloc(sizeof(Cliente));
    strcpy(novo_cliente->nome, nome);
    strcpy(novo_cliente->endereco, endereco);
    novo_cliente->tentativas_entrega = 0;
    novo_cliente->proximo = NULL;
    return novo_cliente;
}

void adicionar_cliente(Cliente **cabeca, Cliente *novo_cliente) {
    novo_cliente->proximo = *cabeca;
    *cabeca = novo_cliente;
}

Cliente *procurar_cliente(Cliente *cabeca, char *endereco) {
    Cliente *atual = cabeca;
    while (atual != NULL) {
        if (strcmp(atual->endereco, endereco) == 0) {
            return atual;
        }
        atual = atual->proximo;
    }
    return NULL;
}

void remover_cliente(Cliente **cabeca, Cliente *cliente) {
    if (*cabeca == NULL) {
        return;
    }
    if (*cabeca == cliente) {
        *cabeca = cliente->proximo;
        free(cliente);
        return;
    }
    Cliente *anterior = *cabeca;
    while (anterior->proximo != NULL && anterior->proximo != cliente) {
        anterior = anterior->proximo;
    }
    if (anterior->proximo == NULL) {
        return;
    }
    anterior->proximo = cliente->proximo;
    free(cliente);
}

void imprimir_clientes(Cliente *cabeca) {
    Cliente *atual = cabeca;
    while ( atual != NULL ) {
        printf("Nome: %s    Endereco: %s    Tentativas: %d  Proximo: %p \n", atual->nome, atual->endereco, atual->tentativas_entrega, atual->proximo);  
        atual = atual->proximo;
    }
}
