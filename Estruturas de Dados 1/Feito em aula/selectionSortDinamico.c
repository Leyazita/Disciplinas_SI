#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAM 10

typedef struct No{
    int valor; 
    struct No *prox;     
}No;

void selectionSort(No *cabeca)
{
    No *aux, *aux2, *min; //variaveis auxiliares para ajudar a encontrar o menor elemento a cada passo
    int aux3;
    for(aux = cabeca; aux != NULL; aux = aux->prox){  //aqui percorre o vetor ate que o ponteiro aux aponte para NULL
        min = aux; //aqui o ponteiro min aponta para o primeiro elemento do vetor, o atual por enquanto é o menor
        for(aux2 = aux->prox; aux2 != NULL; aux2 = aux2->prox){ //aqui percorre o vetor a partir do segundo elemento
            if(aux2->valor < min->valor){ //entao em cada passo ele compara o valor do elemento atual com o valor do menor elemento
                min = aux2; //se o valor do elemento atual for menor que o valor do menor elemento, o ponteiro min aponta para o elemento atual
            }
        }
        if(aux != min){  //se o valor atual for diferente do menor elemento, significa que o menor 
        //elemento não é o primeiro elemento do vetor. 
        //Então troca o valor do menor elemento com o valor do primeiro elemento do vetor
            aux3 = aux->valor;
            aux->valor = min->valor;
            min->valor = aux3;
            //Então troca o valor do menor elemento com o valor do primeiro elemento do vetor
        }
    }
}

//essa função preenche o vetor com números aleatórios
void preencheVetor(No *cabeca)
{
    No *aux;
    int i;

    srand(time(NULL));
    for(aux = cabeca, i = 0; aux != NULL; aux = aux->prox, i++)
    {
        aux->valor = rand() % 100;
    }
}

//essa função imprime o vetor
void imprimeVetor(No *cabeca)
{
    No *aux;
    for(aux = cabeca; aux != NULL; aux = aux->prox){
        printf("%d ", aux->valor);
    }
    printf("\n");
}

int main()
{
    No *cabeca, *aux;
    int i;
    cabeca = (No*)malloc(sizeof(No));
    aux = cabeca;

    for(i = 0; i < TAM - 1; i++){
        aux->prox = (No*)malloc(sizeof(No));
        aux = aux->prox;
    }
    aux->prox = NULL;

    preencheVetor(cabeca);
    printf("Desordenado: ");
    imprimeVetor(cabeca);
    selectionSort(cabeca);
    printf("Ordenado: ");
    imprimeVetor(cabeca);

    //aqui é so pra liberar a memoria
    aux = cabeca;
    while(aux != NULL) {
        No *temp = aux->prox; //o temp serve para guardar o proximo elemento do vetor, 
        //para que a gente possa liberar a memoria do elemento atual
        // Isso é feito para garantir que o ponteiro para o próximo nó
        // da lista não seja perdido antes que possa ser usado para liberar a memória do nó atual.
        free(aux);
        aux = temp;
    }
    return 0;
}
