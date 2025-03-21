#include <stdio.h>
#include <stdlib.h>
#include "operacoes.h"

//Abra o terminal e digite: gcc -o saida operacoes.c estrutura.c
//Ele vai ser criado assim que você digitar o comando no terminal
//A "saida" será um arquivo chamado saida.exe, eu escolhi esse nome, mas pode ser qualquer um
//Depois digite: ./saida.exe no terminal

int main ()
{
    float x =87, y = 65;
    printf("Soma: %.2f", soma(x,y));
    printf("Subtrair: %.2f", subtracao(x,y));
    printf("Multiplicar: %.2f", multiplicacao(x,y));
    printf("Dividir: %.2f", divisao(x,y));
    return 0;
}
//acaba pelo amor de Deus