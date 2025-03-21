#include <stdio.h>
#include <stdlib.h>
#include "string.h"

//ler string

char* ler(char* str)
{
    int i;
    for (i = 0; str[i] != '\0'; i++)
    {
        printf("%c", str[i]);
    }
    printf("\n");
    return str;
}
char *concatenar(char *str1, char *str2)
{
    int i, j;
    char *str3 = (char *)malloc(sizeof(char) * (tamanho(str1) + tamanho(str2) + 1));
    // aqui eu uso o tamanho da string 1 e 2 para alocar o tamanho da string 3
    for (i = 0; i < tamanho(str1); i++)
    {
        str3[i] = str1[i]; // aqui eu copio a string 1 para a string 3
    }
    for (j = 0; j < tamanho(str2); j++)
    {
        str3[i + j] = str2[j]; // aqui eu copio a string 2 para a string 3 a partir do ultimo elemento da string 1
    }
    str3[i + j] = '\0'; //aqui eu defino o ultimo elemento da string 3 como '\0'
    return str3;
}
int tamanho(char *str)
{
    int i;
    for (i = 0; str[i] != '\0'; i++); // aqui eu conto quantos elementos tem na string

    return i;
}
int iguais(char *str1, char *str2)
{
    int i;
    if (tamanho(str1) != tamanho(str2))
        return 0; // se as strings tiverem tamanhos diferentes, elas não são iguais
    for (i = 0; i < tamanho(str1); i++)
    {
        if (str1[i] != str2[i]) 
            return 0;
    }
    return 1;
}