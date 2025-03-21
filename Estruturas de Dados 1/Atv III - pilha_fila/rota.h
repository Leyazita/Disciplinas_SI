// rota.h
#ifndef _ROTA_H_
#define _ROTA_H_

#include "cliente.h"
#include "score.h"

typedef struct Rota {
    Cliente *cliente;
    struct Rota *proximo;
} Rota;

typedef struct Entrega {
  Cliente* cliente;
  int tentativas;
} Entrega;

typedef struct Pilha {
  Entrega* entrega;
  struct Pilha* proximo;
} Pilha;

typedef struct Fila {
  Entrega* entrega;
  struct Fila* proximo;
} Fila;

Rota *criar_rota(Cliente *cliente);
void inserir_rota(Rota **head, Rota *rota);
Rota *remover_rota(Rota **head);
void destruir_rota(Rota *rota);

#endif // _ROTA_H_
