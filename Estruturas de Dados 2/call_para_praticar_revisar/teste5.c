#include <stdio.h>

/***Desafio: Soma dos Dígitos Recursiva
Escreva uma função recursiva soma_digitos(int n)
 que recebe um número inteiro n como parâmetro e retorna a soma de seus dígitos.***/

void soma_digitos(int *soma, int n)
{
    
    int ultimo_digito, resto;
    
    if (n <= 10) // se for igual ou menor que 10, significa q so tem um digito, n da pra somar com ngm
    {            // 1 + 0 = 1, muda nd
        *soma += n;
    }
    else
    {
        ultimo_digito = n % 10; //pega o ultimo digito, ex: 123/10 = 12,3, sobra 3
        resto = n/10; //remove o ultimo, ex: 123/10 = 12, 12/10 = 1 (ja q é inteiro descarta oq vem dps da virgula)
        soma_digitos(soma, resto);
        *soma += ultimo_digito; //chama a funcao e soma oq sobrou
    }   
}

int main()
{
    int digitos = 0, soma = 0;

    printf("Informe o numero: \n");
    scanf("%d", &digitos);

    soma_digitos(&soma, digitos);
    printf("A soma foi de: %d \n", soma);

    return 0;

}



