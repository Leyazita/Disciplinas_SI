#include <stdio.h>

int exponeciacao(int b, int p)
{
    if(p == 0) // Caso base
    {
        return 1;       // qualquer numero elevado a 0 é 1
    }
    else
    {
        return b * exponeciacao(b, p - 1); // Chamada recursiva
    }
}

int main ()
{
    int base, potencia;

    printf("Digite a base: ");
    scanf("%d", &base);

    printf("Digite a potencia: ");
    scanf("%d", &potencia);

    printf("%d elevado a %d = %d", base, potencia, exponeciacao(base, potencia));
    return 0;
}