// rota.c
#include <stdlib.h>
#include "rota.h"
#include "cliente.h"

Rota *criar_rota(Cliente *cliente) {
    Rota *rota = (Rota *)malloc(sizeof(Rota));
    rota->cliente = cliente;
    rota->proximo = NULL;
    return rota;
}

void inserir_rota(Rota **head, Rota *rota) {
    if (*head == NULL) {
        *head = rota;
        return;
    }

    Rota *ultimo = *head;
    while (ultimo->proximo != NULL) {
        ultimo = ultimo->proximo;
    }

    ultimo->proximo = rota;
}

Rota *remover_rota(Rota **head) {
    if (*head == NULL) {
        return NULL;
    }

    Rota *rota = *head;
    *head = rota->proximo;
    rota->proximo = NULL;
    return rota;
}

void destruir_rota(Rota *rota) {
    if (rota == NULL) {
        return;
    }

    destruir_cliente(rota->cliente);
    free(rota);
}

