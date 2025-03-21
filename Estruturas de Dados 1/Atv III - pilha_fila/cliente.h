#ifndef CLIENTE_H
#define CLIENTE_H

typedef struct cliente Cliente;
typedef

struct cliente {
    char nome[100];
    char endereco[100];
    int tentativas_entrega;
    Cliente *proximo;
};

Cliente *criar_cliente(char *nome, char *endereco);
void adicionar_cliente(Cliente **cabeca, Cliente *novo_cliente);
Cliente *procurar_cliente(Cliente *cabeca, char *endereco);
void remover_cliente(Cliente **cabeca, Cliente *cliente);
void imprimir_clientes(Cliente *cabeca);

#endif
