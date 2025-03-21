#include <stdio.h>

float juros_compostos(float valor_inicial, int meses, float juros)
{
    if (meses == 0)
    {
        return valor_inicial;
    }
    else
    {
        valor_inicial += valor_inicial * (juros/100);
        meses -= 1;
        return juros_compostos(valor_inicial, juros, meses);
    }
}

int main()
{
    float valor_inicial = 0, juros = 0;
    int meses;

    printf("Digite o valor inicial: ");
    scanf("%f", &valor_inicial);
    printf("Digite o numero de meses: ");
    scanf("%d", &meses);
    printf("Digite o juros: ");
    scanf("%f", &juros);

    printf("O valor final eh: %.2f\n", juros_compostos(valor_inicial, meses, juros));
    return 0;
}