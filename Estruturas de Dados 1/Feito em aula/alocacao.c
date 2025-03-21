#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *vt1;
    int m, n, i;

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &m);

    vt1 = (int *) malloc(m * sizeof(int)); // faço a alocacao dinamica pra definir o tamanho do vetor

    for(i = 0; i < m; i++) //usuario escolhe o tamanho do vetor
    {
        vt1[i] = rand() % 100; //preencho o vetor com numeros aleatorios
        printf("%d\n", vt1[i]);
    }
}