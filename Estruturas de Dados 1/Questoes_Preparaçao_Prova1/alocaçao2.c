#include <stdio.h>
#include <stdlib.h>

int* alocarMemoria (int tamanho)
{
    int *vetor;
    vetor = (int*) malloc(tamanho * sizeof(int));
    return vetor;
}

void printVetor(int *vetor, int tamanho)
{
    int i;
    for(i=0; i < tamanho; i++)
    {
        printf("Elemento %d: %d \n", i+1, vetor[i]);
    }
}

void liberarMemoria(int *vetor)
{
    free(vetor);
}


int main()
{
    int tamanho, *vetor;

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);

    vetor = alocarMemoria(tamanho);
    for (int i = 0; i < tamanho; i++)
    {
        printf("Digite o elemento %d: ", i+1);
        scanf("%d", &vetor[i]);
    }

    printVetor(vetor, tamanho);
    liberarMemoria(vetor);

    return 0;
}