#include <stdio.h>

int valor_No_vetor(int vetor[], int t, int valor)
{
    if (t == 0)
    {
        return -1;
    }
    else
    {
        if (vetor[t] == valor)
        {
            return vetor[t];
        }
        else
        {
            return valor_No_vetor(vetor, t - 1, valor);
        }
    }
}

int main()
{
    int vetor[] = {1, 2, 3, 4, 5};
    int tamanho = 5;
    int valor = 3;

    printf("%d", valor_No_vetor(vetor, tamanho, valor));
    return 0;
}