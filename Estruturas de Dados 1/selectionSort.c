#include <stdio.h>
#include <stdlib.h>

#define MAX 10
//fazer dois exemplos com selection sort, um com lista estatica e outro com lista dinamica (usando ponteiros) e com a cabeça da lista

//exemplo com 

// Selection Sort
void selectionSort(int *vetor);
void exemploListaEstatica();
void exemploListaDinamica();

int main()
{
    exemploListaEstatica();
    exemploListaDinamica();
    return 0;
}

void selectionSort(int *vetor)
{
    int i, j, min, aux;
    for (i = 0; i < MAX - 1; i++)
    {
        min = i;
        for (j = i + 1; j < MAX; j++)
        {
            if (vetor[j] < vetor[min])
                min = j;
        }
        if (i != min)
        {
            aux = vetor[i];
            vetor[i] = vetor[min];
            vetor[min] = aux;
        }
    }
}

void exemploListaEstatica()
{
    int vetor[MAX] = {5, 3, 2, 4, 7, 1, 0, 6, 9, 8};
    int i;
    printf("Lista original: ");
    for (i = 0; i < MAX; i++)
        printf("%d ", vetor[i]);
    printf("\n");
    selectionSort(vetor);
    printf("Lista ordenada: ");
    for (i = 0; i < MAX; i++)
        printf("%d ", vetor[i]);
    printf("\n");
}

void exemploListaDinamica()
{
    int *vetor;
    int i;
    vetor = (int *)malloc(MAX * sizeof(int));
    for (i = 0; i < MAX; i++)
        vetor[i] = MAX - i - 1;
    printf("Lista original: ");
    for (i = 0; i < MAX; i++)
        printf("%d ", vetor[i]);
    printf("\n");
    selectionSort(vetor);
    printf("Lista ordenada: ");
    for (i = 0; i < MAX; i++)
        printf("%d ", vetor[i]);
    printf("\n");
    free(vetor);
}
