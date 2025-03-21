#include <stdio.h>
#include <stdlib.h>

int main(){
    
    int *v = NULL, num = 0, total = 0, count = 0;

    printf("Digite os valores e -1 para sair");
    for(int i = 0; scanf("%d", &num) && num != -1; i++){

        count++;
        v = (int *) realloc(v, sizeof(int) * count);
        v[i] = num; 
    }

    for(int i = 0; i < count; i++){
        total += v[i];
    }

    printf("Media: %.2f", (float)total/count);
    free(v);
    return 0;
}