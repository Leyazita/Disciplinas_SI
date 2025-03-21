#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int num_conta;
    char nome[20];
    struct no *proximo;
} No;

typedef struct {
    No * inicio;
    No *fim;
} Lista;

void insirir_inicio(Lista *lista, int num)
{
    No * novo = malloc(sizeof(No));
    if(novo){
        novo -> num_conta = num;
        novo -> proximo = lista ->inicio;
    }
}

