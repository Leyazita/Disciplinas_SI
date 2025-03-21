#include <stdio.h>

int inteiros_positivos_descrescente (int k)
{
    if (k <= 0)
    {
        return 1;
    }
    else
    {
        printf("%d ", k);
        inteiros_positivos_descrescente(k - 1);
    }
}

int main()
{
    int n;
    printf("Digite um numero: ");
    scanf("%d", &n);

    inteiros_positivos_descrescente(n);
    return 0;
}