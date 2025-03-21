#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int*)malloc(sizeof(int));
    *ptr = 42;

    //free(ptr);

    int valor = *ptr;
    printf("Valor: %d\n", valor);

    return 0;
}