#include <stdio.h>


Conta *inserir(Conta *lista)
{
    Conta *novo = (Conta*)malloc(sizeof(Conta));
    novo -> num_conta = rand()% 100 +10;
    scanf("%i", &novo->saldo);
    scanf("%i", &novo->titular);

    if (lista == NULL)
        novo ->proximo = novo;
    else
        aux = lista;
        while(aux -> proximo)

}