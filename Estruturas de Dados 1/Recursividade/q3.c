#include <stdio.h>

int soma_inteiros_positivos(int k)
{
    if (k <= 0)
    {
        return 0;
    }
    else
    {
        return k + soma_inteiros_positivos(k - 1);
    }
}

int main()
{
    int n;
    printf("Digite um numero: ");
    scanf("%d", &n);

    printf("A soma dos inteiros positivos de 1 a %d eh: %d", n, soma_inteiros_positivos(n));
    return 0;
}