#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cliente.h"
#include "rota.h"
#include "score.h"

//testanto as funçoes dos arquivos cliente.c, rota.c e score.c

int main()
{
    //criando um cliente
    Cliente *cliente = criar_cliente("Joao", "Rua 1");
    //criando uma rota
    Rota *rota = criar_rota(cliente);
    //inserindo a rota na lista
    inserir_rota(&rota, rota);
    //removendo a rota da lista
    Rota *rota_removida = remover_rota(&rota);
    //destruindo a rota
    destruir_rota(rota_removida);
    //destruindo o cliente
    //destruir_cliente(cliente);
    //calculando o escore
    float score = calcular_escore(10, 5);
    printf("Escore: %.2f", score);
}

//so da erro nessa desgraça