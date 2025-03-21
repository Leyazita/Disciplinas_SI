#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>


//lista encadeada para armazenar as linhas
typedef struct Linhas{
    int num_linha;
    struct Linhas *prox;
}Linhas;

typedef struct ArvRB{
    char info[50];
    int cor; //0 = vermelho, 1 = preto
    struct ArvRB *esq, *dir;
    Linhas *linhas;
}ArvRB;

ArvRB *criaArvRB(char *palavra, int num_linha){
    ArvRB *novo = (ArvRB*)malloc(sizeof(ArvRB));
    strcpy(novo->info, palavra);
    novo->cor = 0;
    novo->esq = NULL;
    novo->dir = NULL;
    novo->linhas = (Linhas*)malloc(sizeof(Linhas));
    novo->linhas->num_linha = num_linha;
    novo->linhas->prox = NULL;
    return novo;
}

ArvRB *rotEsq(ArvRB *raiz){
    ArvRB *aux = raiz->dir;
    raiz->dir = aux->esq;
    aux->esq = raiz;
    aux->cor = raiz->cor;
    raiz->cor = 0;
    return aux;
}

ArvRB *rotDir(ArvRB *raiz){
    ArvRB *aux = raiz->esq;
    raiz->esq = aux->dir;
    aux->dir = raiz;
    aux->cor = raiz->cor;
    raiz->cor = 0;
    return aux;
}

void trocaCor(ArvRB *raiz){
    if(raiz->esq->cor == 0 && raiz->dir->cor == 0){
        raiz->cor = 0;
        raiz->esq->cor = 1;
        raiz->dir->cor = 1;
    }
}

int cor(ArvRB *raiz){
    int auxC;
    //se for null, é preto
    if(raiz == NULL){
        auxC = 1;
    }
    else{
        auxC = raiz->cor;
    }
    return auxC;          
}

Linhas *criaLinhas(int num_linha){
    Linhas *novaL = (Linhas*)malloc(sizeof(Linhas));
    novaL->num_linha = num_linha;
    novaL->prox = NULL;
    return novaL;
}

Linhas *insereLinhas(Linhas *linhas, int num_linha){
    if(linhas == NULL){ //se a lista estiver vazia, cria uma nova
        linhas = criaLinhas(num_linha);
    }
    else{ //se não, insere no final
        Linhas *aux = linhas;
        while(aux->prox != NULL){
            aux = aux->prox;
        }
        aux->prox = criaLinhas(num_linha);
    }
    return linhas;
}

ArvRB *insereNo(ArvRB *raiz, char *palavra, int linha){
    if(raiz == NULL){
        raiz = criaArvRB(palavra, linha);
    }else{
        if(strcmp(palavra, raiz->info) < 0){ //se a palavra for menor que a raiz, insere na esquerda
            raiz->esq = insereNo(raiz->esq, palavra, linha);
        }
        else if(strcmp(palavra, raiz->info) > 0){ //se a palavra for maior que a raiz, insere na direita
            raiz->dir = insereNo(raiz->dir, palavra, linha);
        }
        else{ //se a palavra for igual a raiz, insere na lista de linhas
            raiz->linhas = insereLinhas(raiz->linhas, linha);
        }
    }
    //se a raiz da esquerda for preta e a da direita for vermelha, rotaciona a esquerda
    if(cor(raiz->dir) == 0 && cor(raiz->esq) == 1){
        raiz = rotEsq(raiz);
    }
    //se a raiz da esquerda e a esquerda da esquerda forem vermelhas, rotaciona a direita
    if(cor(raiz->esq) == 0 && cor(raiz->esq->esq) == 0){
        raiz = rotDir(raiz);
    }
    //se a raiz da esquerda e a da direita forem vermelhas, troca a cor
    if(cor(raiz->esq) == 0 && cor(raiz->dir) == 0){
        trocaCor(raiz);
    }
    return raiz;
}

ArvRB *insereArvRB(ArvRB *raiz, char *palavra, int linha){
    raiz = insereNo(raiz, palavra, linha);
    // a raiz sempre é preta
    if(raiz != NULL){
        raiz->cor = 1;
    }
    return raiz;
}

void imprimeLinhas(Linhas *raizLinhas) {
    if (raizLinhas != NULL) { //se a lista não estiver vazia, imprime a linha 
        printf("%d ", raizLinhas->num_linha);
        imprimeLinhas(raizLinhas->prox); //chama a função para imprimir o resto da lista
    }
}

void atualizaArquivo(ArvRB *raiz, FILE *arq) {
    if (raiz != NULL) {
        atualizaArquivo(raiz->esq, arq);
        fprintf(arq, "%s\n", raiz->info);
        atualizaArquivo(raiz->dir, arq);
    }
}

void leArquivo(ArvRB **raiz, char *nomeArq) {
    FILE *arq;
    char palavra[50];
    int linha = 1;
    arq = fopen(nomeArq, "r+");
    if (arq == NULL) {
        printf("Erro ao abrir o arquivo!\n");
    } else {
        while (fscanf(arq, "%s", palavra) != EOF) {
            *raiz = insereArvRB(*raiz, palavra, linha);
            linha++;
        }
        
        // Atualiza o arquivo com as palavras adicionadas
        rewind(arq); // Volta para o início do arquivo
        atualizaArquivo(*raiz, arq);
    }
    fclose(arq);
}


void buscarPalavra(ArvRB *raiz, char *palavra){
    if(raiz != NULL){
        if(strcmp(palavra, raiz->info) < 0){ //se a palavra for menor que a raiz, busca na esquerda
            buscarPalavra(raiz->esq, palavra);
        }
        else if(strcmp(palavra, raiz->info) > 0){ //se a palavra for maior que a raiz, busca na direita
            buscarPalavra(raiz->dir, palavra);
        }
        else{ //se a palavra for igual a raiz, imprime a lista de linhas
            imprimeLinhas(raiz->linhas);
        }
    }
}

//Imprimir uma palavra e as linhas do texto em que ela aparece
void imprimePalavra(ArvRB *raiz, char *palavra){
    printf("A palavra de busca: %s ", palavra);
    buscarPalavra(raiz, palavra);
    printf("\n");
}

//imprime palavras em ordem alfabética e o numero das linhas
void imprimeArvRB(ArvRB *raiz) {
    if (raiz != NULL) {
        imprimeArvRB(raiz->esq);
        printf("Palavra: %-15s | Linhas: ", raiz->info);
        imprimeLinhas(raiz->linhas);
        printf("\n");
        imprimeArvRB(raiz->dir);
    }
}

ArvRB *imprimirArveCores(ArvRB *raiz){
    if(raiz != NULL){
        printf("Palavra: %-15s | Cor: %d\n", raiz->info, raiz->cor);
        imprimirArveCores(raiz->esq);
        imprimirArveCores(raiz->dir);
    }
}

int main(){


    ArvRB *raiz = NULL;
    char palavra[50]; //, nomeArq[50];
    int opcao, linha;

    //printf("Digite o nome do arquivo: ");
    //scanf("%s", nomeArq);
    char nomeArq[] = "palavras.txt";
    leArquivo(&raiz, nomeArq);

    do{
        printf("1 - Inserir uma palavra em uma linha\n");
        printf("2 - Imprimir uma palavra e as linhas do texto em que ela aparece\n");
        printf("3 - Imprimir a arvore\n");
        printf("4 - Remover uma palavra\n");
        printf("5 - Conferir cores\n");
        printf("6 - Sair\n");
        printf("Digite a opcao: ");
        scanf("%d", &opcao);
        switch(opcao){
            case 1:
                 printf("Digite a palavra: ");
                scanf("%s", palavra);
                printf("Digite a linha: ");
                scanf("%d", &linha);
                raiz = insereArvRB(raiz, palavra, linha);
                break;
            case 2:
                printf("Digite a palavra: ");
                scanf("%s", palavra);
                imprimePalavra(raiz, palavra);
                break;
            case 3:
                imprimeArvRB(raiz);
                break;
            /**case 4:
                printf("Digite a palavra: ");
                scanf("%s", palavra);
                //tem q fazer ainda
                break;**/
            case 5:
                imprimirArveCores(raiz);
                break;
            case 6:
                printf("Saindo...\n");
                break;
            default:
                printf("Opcao invalida!\n");
                break;
        }
    }while(opcao != 6);


    //busca cada palavra e mostrar o tempo de busca

    return 0;
}