#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// free usa quando nao quer armazenar a memoria (calloc)
// malloc usa quando quer armazenar a memoria (malloc)

/**void preencher(int *v, int tam)
{
    for(int i = 0; i < tam; i++)
    {
        v[i] = rand() % 100;
    }
}**/

void maiorMenor(int *maior, int *menor, int qnt)
{
    int valor = 0;
    printf("Digite o valor: ");
    scanf("%d", &valor);

    *maior = valor;
    *menor = valor;

    for(int i = 1; i < qnt; i++)
    {
        scanf("%d", &valor);
        if(valor > *maior)
        {
            *maior = valor;
        }
        if(valor < *menor)
        {
            *menor = valor;
        }
    }
}

int main()
{
    srand(time(NULL));

    int maior, menor, qnt;
    printf("Digite a quantidade de valores: ");
    scanf("%d", &qnt);
    maiorMenor(&maior, &menor, qnt);
    printf("maior = %d\n", maior);
    printf("menor = %d\n", menor);

    /**int x = 5, *v;
    //int x, *v;

    scanf("%d", &x);
    //v = (int *) malloc(x * sizeof(int)); // alocar e não inicializar
    v = (int *) calloc(x, sizeof(int)); // alocar e inicializar com 0

    if(v == NULL)
    {
        exit(1);
    }
    int menor = v[0];
    for(int i = 0; i < x; i++)
    {
        //v[i] = rand() % 100;
        scanf("%d", &v[i]);

        if(v[i] < menor)
        {
            menor = v[i];
        }
    }
    printf("menor = %d", menor);**/

    return 0;
}