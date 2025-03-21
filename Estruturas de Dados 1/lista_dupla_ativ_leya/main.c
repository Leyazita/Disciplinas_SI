#include <stdio.h>
#include <stdlib.h>

#include "listadinamicasimples.h"

int main(int argc, char const *argv[])
{
	Conta *listaContas = criarLista();

	int opcao;
	do{
		printf("1 - Inserir no inicio\n");
		printf("2 - Inserir no fim\n");
		printf("3 - Remover do inicio\n");
		printf("4 - Remover do fim\n");
		printf("5 - Imprimir\n");
		printf("6 - Sair\n");
		scanf("%d", &opcao);
		switch(opcao){
			case 1:
				listaContas = inserir(listaContas);
				break;
			case 2:
				listaContas = inserirFim(listaContas);
				break;
			case 3:
				int num_conta;
				printf("Num da conta a ser removida - ");
				scanf("%d", &num_conta);

				listaContas = remover(listaContas, num_conta);
				break;
			case 4:
				listaContas = removerFim(listaContas);
				break;
			case 5:
				imprimir(listaContas);
				break;
			case 6:
				printf("Saindo...\n");
				break;
			default:
				printf("Opcao invalida\n");
				break;
		}
	}while(opcao != 6);

	liberarLista(listaContas);
	

	return 0;
}