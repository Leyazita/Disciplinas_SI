#include <stdio.h>
#include <stdlib.h>

int lerElementosVetor(int *vetor, int tamanho)
{
    int i;
    for(i=0; i < tamanho; i++)
    {
        printf("Digite o elemento %d: ", i+1);
        scanf("%d", &vetor[i]);
    }
}

int PrintVetor(int *vetor, int tamanho)
{
    int i;
    for(i=0; i < tamanho; i++)
    {
        printf("Elemento %d: %d ", i+1, vetor[i]);
    }
}

int main()
{
    int tamanho;
    int *vetor;
    
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);
    vetor = (int*) malloc(tamanho * sizeof(int));
    lerElementosVetor(vetor, tamanho);
    PrintVetor(vetor, tamanho);
    free(vetor);

    return 0;
}