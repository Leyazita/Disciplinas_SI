#include <stdio.h>

int soma_entre_valores(int a, int b)
{
    if (a == b)
    {
        return a;
    }
    else
    {
        return a + soma_entre_valores(a + 1, b);
    }
}

int main ()
{
    int a, b;
    printf("Digite o primeiro valor: ");
    scanf("%d", &a);
    printf("Digite o segundo valor: ");
    scanf("%d", &b);

    printf("A soma dos valores entre %d e %d eh: %d", a, b, soma_entre_valores(a, b));
    return 0;
}