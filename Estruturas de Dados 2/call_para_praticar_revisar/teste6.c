#include <stdio.h>
#include <string.h> 
#include <stdlib.h>


struct arv
{
    int info;
    struct arv *esq, *dir;
};


struct raiz
{
    struct arv *raiz;
};


void inserirNo(struct arv **raiz, int valor)
{
    if (*raiz == NULL)
    {
        *raiz = (struct arv*) malloc(sizeof(struct arv));
        (*raiz)->info = valor;
        (*raiz)->esq = NULL;
        (*raiz)->dir = NULL;
    }
    else
    {
        if (valor < (*raiz)->info)
        {
            inserirNo(&(*raiz)->esq, valor);
        }
        else
        {
            inserirNo(&(*raiz)->dir, valor);
        }
    }
}

void removerNo(struct arv **raiz, int valor)
{
    if(*raiz == NULL)
    {
        printf("Valor nao encontrado\n");
    }
    
    else if (valor < (*raiz)->info)
    {
        removerNo(&(*raiz)->esq, valor);
    }
    else if (valor > (*raiz)->info)
    {
        removerNo(&(*raiz)->dir, valor);
    }
    else 
    {
        if ((*raiz)->esq == NULL && (*raiz)->dir == NULL)
        {
            free(*raiz);
            (*raiz) = NULL;
        }
        else if ((*raiz)->esq == NULL || (*raiz)->dir == NULL)
        {
            struct arv *aux = *raiz;
            if ((*raiz)->esq == NULL)
            {
                (*raiz) = (*raiz)->dir;
            }
            else
            {
                (*raiz) = (*raiz)->esq;
            }
            free(aux);
        }
        else 
        {
            if ((*raiz)->esq != NULL && (*raiz)->dir != NULL) 
            {
                struct arv *aux = (*raiz)->esq;
                while (aux->dir != NULL)
                {
                    aux = aux->dir;
                }
                (*raiz)->info = aux->info;
                aux->info = valor;
                removerNo(&(*raiz)->esq, valor);
            }
        }

    }

}

void imprimirArvore(struct arv *raiz)
{
    if (raiz != NULL)
    {
        printf("%d\n", raiz->info);
        imprimirArvore(raiz->esq);
        imprimirArvore(raiz->dir);
    }  
}

int main ()
{ 
    struct raiz *raizArv = (struct raiz*) malloc(sizeof(struct raiz));
    raizArv->raiz = NULL;

    inserirNo(&raizArv->raiz, 10);
    inserirNo(&raizArv->raiz, 5);
    inserirNo(&raizArv->raiz, 15);
    inserirNo(&raizArv->raiz, 14);
    inserirNo(&raizArv->raiz, 16);

    printf("Arvore antes da remocao: \n");
    imprimirArvore(raizArv->raiz);
  
    //printf("Depois da remocao da folha: \n");
    //removerNo(&raizArv->raiz, 14);
    //imprimirArvore(raizArv->raiz);

    //printf("Depois da remocao do no com 1 filho: \n");
    //removerNo(&raizArv->raiz, 15);
    //imprimirArvore(raizArv->raiz);
    
    printf("Depois da remocao do no com 2 filhos: \n");
    removerNo(&raizArv->raiz, 10);
    imprimirArvore(raizArv->raiz);

    //printf("Valor da raiz: %d\nValor dir: %d\nValor esq: %d\n", raizArv->raiz->info, raizArv->raiz->dir->info, raizArv->raiz->esq->info);

    return 0;
}
