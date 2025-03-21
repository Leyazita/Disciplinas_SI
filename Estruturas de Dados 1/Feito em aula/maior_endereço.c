#include <stdio.h>
#include <stdlib.h>

// leia dois valores inteiors e compare os endereços e retorne o conteudo de maior valor

int main()
{
    int a, b, *aa = &a, *bb = &b;
    printf("Digite o primeiro valor: ");
    scanf("%d", &a);
    printf("Digite o segundo valor: ");
    scanf("%d", &b);

    printf("%d\n", &a);
    printf("%d\n", &b);
    printf("-----------\n");
    printf("%d\n", aa);
    printf("%d\n", bb);

    if(&a > &b)
    {
        printf("O maior valor eh: %d", aa);
    }
    else
    {
        printf("O maior valor eh: %d", bb);
    }

    printf("endereco: %d\n%d", &a, &b);
}
