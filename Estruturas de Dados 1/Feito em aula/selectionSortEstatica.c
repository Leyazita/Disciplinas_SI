#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAM 10

/**essa função recebe um vetor e o tamanho dele, depois percorre o vetor e procura o menor elemento,
 se o menor elemento não for o primeiro elemento do vetor, ele troca o menor elemento com o primeiro 
 elemento do vetor, depois ele procura o segundo menor elemento e troca com o segundo elemento do 
 vetor e assim por diante até que o vetor esteja ordenado
**/
void selectionSort(int *vetor, int tam){
    int i, j, min, aux;
    for(i = 0; i < tam - 1; i++){
        min = i;
        for(j = i + 1; j < tam; j++){
            if(vetor[j] < vetor[min]){
                min = j;
            }
        }
        if(i != min){
            aux = vetor[i];
            vetor[i] = vetor[min];
            vetor[min] = aux;
        }
    }
}

//essa função preenche o vetor com números aleatórios
void preencheVetor(int *vetor, int tam){
    int i;
    srand(time(NULL));
    for(i = 0; i < tam; i++){
        vetor[i] = rand() % 100;
    }
}

//essa função imprime o vetor
void imprimeVetor(int *vetor, int tam){
    int i;
    for(i = 0; i < tam; i++){
        printf("%d ", vetor[i]);
    }
    printf("\n");
}


//no main a gente testa esse vetor
int main(){
    int vetor[TAM];
    preencheVetor(vetor, TAM);
    printf("Vetor desordenado: ");
    imprimeVetor(vetor, TAM);
    selectionSort(vetor, TAM);
    printf("Vetor ordenado: ");
    imprimeVetor(vetor, TAM);
    return 0;
}