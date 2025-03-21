#include <stdio.h>
// Biblioteca necessária para medição
#include <time.h>

int main()
{
    
// Variáveis tipo "clock_t" são usadas para armazenar os valores de clock antes e após a operação a ser medida.

    clock_t inicio, fim;

// Variáveil para armazenar o tempos

    double tempo;

// clock() é uma função que marca um momento da medição

    inicio = clock();

// tudo que será medido deve ficar entre as variáveis inicio e fim

    printf("Hello World\n");
    printf("Hello World\n");
    printf("Hello World\n");
    printf("Hello World\n");

    fim = clock();
        
/*
CLOCKS_PER_SEC é uma constante que representa o número de clocks por segundo e pode variar dependendo do SO e da implementação do compilador.
Por padrão, CLOCKS_PER_SEC é geralmente definido como 1000000 (1 milhão), o que significa que o relógio medido pela função clock() é baseado em microssegundos (1/1.000.000 de segundo)

*/ 
    

    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("%f\n", tempo);

    return 0;
}


