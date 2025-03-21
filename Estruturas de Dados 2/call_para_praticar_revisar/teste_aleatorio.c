#include <stdio.h>
#include <stdlib.h>
//desenhar e explicar o que esta acontecendo na memoria
struct arv {
    int info;
    struct arv *dir, *esq;
};

struct raiz {
    struct arv *raiz;
};

void atribui(struct raiz **raizavb, struct arv *node);

int main() {
    typedef struct arv arvB;
    typedef struct raiz raizA;

    raizA *raizAbb = (raizA*) malloc(sizeof(raizA));
    arvB *newNode = (arvB*) malloc(sizeof(arvB));

    newNode->info = 2;
    newNode->dir = NULL;
    newNode->esq = NULL;

    atribui(&raizAbb, newNode);

    free(newNode);
    free(raizAbb);

    return 0;
}

void atribui(struct raiz **raizavb, struct arv *node) {
    (*raizavb)->raiz = node;

    printf("%d\n", (*raizavb)->raiz->info);
}
