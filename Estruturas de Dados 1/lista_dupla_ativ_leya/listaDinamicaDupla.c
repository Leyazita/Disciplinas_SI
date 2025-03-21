#include <stdio.h>
#include <stdlib.h>

#include "listadinamicasimples.h"


struct conta{
	float saldo;
	char titular[100];
	int num_conta;
	struct conta *prox, *ant;
};

Conta *criarLista(){
	return NULL;
}

Conta *inserirInicio(Conta *lista){
	Conta *new = (Conta*) calloc(sizeof(Conta),1);
	new->num_conta = rand() % 100 + 10;
	printf("Nome - ");
	scanf("%s", new->titular);
	printf("Saldo - ");
	scanf("%f", &new->saldo);
	new->ant = NULL;
	new->prox = lista;
	if (lista)
		lista->ant = new;
	return new;
}

Conta *inserirFim(Conta *lista) {
	Conta *new = (Conta*) calloc(sizeof(Conta),1), *aux;
	
	new->num_conta = rand() % 100 + 10;
	printf("Nome - ");
	scanf("%s", new->titular);
	printf("Saldo - ");
	scanf("%f", &new->saldo);
	
	if (!lista)//se a lista for vazia o primeiro e o ultimo sao iguais
	{
		new->prox = new;
		new->ant = new;
	}
	else{
		aux = lista;
		while(aux->prox != lista)
			aux = aux->prox;
		aux->prox = new;
		new->prox = lista;
		new->ant = aux;
		lista->ant = new;
	}
	return new;
}

Conta *inserirOrdenado(Conta *lista) {
	Conta *new = (Conta*) calloc(sizeof(Conta),1), *aux;
	
	new->num_conta = rand() % 100 + 10;
	printf("Nome - ");
	scanf("%s", new->titular);
	printf("Saldo - ");
	scanf("%f", &new->saldo);
	
	if (!lista)//se a lista for vazia o primeiro e o ultimo sao iguais
	{
		new->prox = new;
		new->ant = new;
	}
	else{
		aux = lista;
		while(aux->prox != lista && aux->saldo < new->saldo)
			aux = aux->prox;
		if (aux->saldo < new->saldo)
		{
			aux->prox = new;
			new->prox = lista;
			new->ant = aux;
			lista->ant = new;
		}
		else{
			new->prox = aux;
			new->ant = aux->ant;
			aux->ant->prox = new;
			aux->ant = new;
			if (aux == lista)
				lista = new;
		}
	}
	return new;
}

Conta *remover(Conta *lista, int valor) {
	Conta *aux = lista;
	if (lista)
	{
		while(aux->prox != lista && aux->num_conta != valor)
			aux = aux->prox;
		if (aux->num_conta == valor)
		{
			if (aux == lista)
				lista = lista->prox;
			aux->ant->prox = aux->prox;
			aux->prox->ant = aux->ant;
			free(aux);
		}
	}
	return lista;
}

Conta *buscar(Conta *lista, int valor) {
	Conta *aux = lista;
	if (lista)
	{
		while(aux->prox != lista && aux->num_conta != valor)
			aux = aux->prox;
		if (aux->num_conta == valor)
			return aux;
	}
	return NULL;
}

Conta *alterar(Conta *lista, int oldValue, int newValue) {
	Conta *aux = lista;
	if (lista)
	{
		while(aux->prox != lista && aux->num_conta != oldValue)
			aux = aux->prox;
		if (aux->num_conta == oldValue)
			aux->num_conta = newValue;
	}
	return lista;
}

int listaVazia(Conta *lista) {
	return lista == NULL;
}

void mostrarLista(Conta *lista) {
	Conta *aux = lista;
	if (lista)
	{
		do{
			printf("Nome: %s\n", aux->titular);
			printf("Saldo: %.2f\n", aux->saldo);
			printf("Numero da conta: %d\n", aux->num_conta);
			aux = aux->prox;
		}while(aux != lista);
	}
}

void liberarLista(Conta *lista) {
	Conta *aux = lista;
	if (lista)
	{
		while(aux->prox != lista)
		{
			aux = aux->prox;
			free(aux->ant);
		}
		free(aux);
	}
}