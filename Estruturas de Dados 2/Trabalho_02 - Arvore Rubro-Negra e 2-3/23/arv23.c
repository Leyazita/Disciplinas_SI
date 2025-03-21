#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "arv23.h"

void inserirLinha(Linhas **no, int linha){
    if(*no == NULL){
        *no = (Linhas*) malloc(sizeof(Linhas));

        if(*no != NULL){
            (*no)->linha = linha;
            (*no)->prox = NULL;
        }
    }else
        inserirLinha(&((*no)->prox), linha);
}

Info *criaInfo(char *palavra, Linhas *lista, int linha){

    Info *info;
    info = (Info*) malloc(sizeof(Info)); 

    info->palavra = (char*) malloc((strlen(palavra) + 1) * sizeof(char));
    strcpy(info->palavra, palavra);

    if(lista == NULL){
        info->ListaNum = NULL;
        inserirLinha(&(info->ListaNum), linha);
    }else{
        info->ListaNum = lista;
    }
    return info;
}

Arv23 *criaNo(Info *info, Arv23 *noEsq, Arv23 *noCentro) {
    Arv23 *no = (Arv23*) malloc(sizeof(Arv23)); 

    no->info1 = info; 
    no->numInfo = 1;
    no->esq = noEsq;
    no->centro = noCentro;
    no->dir = NULL;

    return no;
}

void adicionaNo(Arv23 **raiz, Info *info, Arv23 *filho) {
    
    if(strcmp(info->palavra, (*raiz)->info1->palavra) > 0){
        (*raiz)->info2 = info;
        (*raiz)->dir = filho;
    }else{
        (*raiz)->info2 = (*raiz)->info1;
        (*raiz)->info1 = info; 

        (*raiz)->dir = (*raiz)->centro;
        (*raiz)->centro = filho;
    }
    (*raiz)->numInfo = 2;
}

Arv23 *quebraNo(Arv23 **raiz, Arv23 *filho, Info *info, Info **infoSobe) {
    Arv23 *maiorNo;
    maiorNo = NULL;

    if (strcmp(info->palavra, (*raiz)->info2->palavra) > 0) {
        *infoSobe = (*raiz)->info2;
        maiorNo = criaNo(info, (*raiz)->dir, filho);
    } 
    
    else if (strcmp(info->palavra, (*raiz)->info1->palavra) < 0) {
        *infoSobe = (*raiz)->info1;
        maiorNo = criaNo((*raiz)->info2, (*raiz)->centro, (*raiz)->dir);
        
        (*raiz)->info1 = info;
        (*raiz)->centro = filho;
    }

    else {
        *infoSobe = info;
        maiorNo = criaNo((*raiz)->info2, filho, (*raiz)->dir);  
    }

    (*raiz)->numInfo = 1;
    (*raiz)->info2 = NULL;
    (*raiz)->dir = NULL; 

    return maiorNo;
}

int folha(Arv23 *raiz){
    int achou = 0;

    if(raiz->esq == NULL)
        achou = 1;
    
    return achou;
}

Arv23 *inserePalavra(Arv23 **raiz, char *palavra, int linha, Arv23 *pai, Info **infoSobe){
    Arv23 *maiorNo;

    if(*raiz == NULL){ 
        *raiz = criaNo(criaInfo(palavra, NULL, linha), NULL, NULL);
    }else{

        if(folha(*raiz)){
            if((*raiz)->numInfo == 1){
                adicionaNo(raiz, criaInfo(palavra, NULL, linha), NULL);
                maiorNo = NULL;
            }else{
                maiorNo = quebraNo(raiz, NULL, criaInfo(palavra, NULL, linha), infoSobe);

                if(pai == NULL){
                    *raiz = criaNo(*infoSobe, *raiz, maiorNo);
                    maiorNo = NULL;
                }
            }
        }else{
            
            if(strcmp(palavra, (*raiz)->info1->palavra) < 0)   
                maiorNo = inserePalavra(&((*raiz)->esq), palavra, linha, *raiz, infoSobe);
            
            else if(((*raiz)->numInfo == 1) || ((*raiz)->numInfo == 2 && strcmp(palavra, (*raiz)->info2->palavra) < 0))
                maiorNo = inserePalavra(&((*raiz)->centro), palavra, linha, *raiz, infoSobe);
            
            else
                maiorNo = inserePalavra(&((*raiz)->dir), palavra, linha, *raiz, infoSobe);   

            if(maiorNo != NULL){
                if((*raiz)->numInfo == 1){
                    adicionaNo(raiz, *infoSobe, maiorNo);
                    maiorNo = NULL;
                }else{
                    maiorNo = quebraNo(raiz, maiorNo, *infoSobe, infoSobe);
                    if(pai == NULL){
                        *raiz = criaNo(*infoSobe, *raiz, maiorNo);
                        maiorNo = NULL;
                    }
                }
            }
        }
    }
    return maiorNo;
}

void insereOuAtualizaPalavra(Arv23 **raiz, char *palavra, int linha, Arv23 *pai, Info **infoSobe){
    Info *aux;
    aux = NULL;
    buscaPalavra(*raiz, palavra, &aux);

    if(aux == NULL){
        inserePalavra(raiz, palavra, linha, NULL, infoSobe);
    }else{
        inserirLinha(&(aux->ListaNum), linha);
    }
}

//funcao para ler o arquivo

void imprimirLista(Linhas *no){
    if(no != NULL){
        printf("%d ", no->linha);
        imprimirLista(no->prox);
    }
}

void imprimirInfo(Info *info){
    if(info != NULL){
        printf("%s, linhas: ", info->palavra);
        imprimirLista(info->ListaNum);
        printf("\n");
    }
}

void imprimirArv(Arv23 *raiz){
    if(raiz != NULL){
        printf("\nInfo 1:\n");
        imprimirInfo(raiz->info1);
        if(raiz->numInfo == 2){
            printf("Info 2:\n");
            imprimirInfo(raiz->info2);
        }
        imprimirArv(raiz->esq);
        imprimirArv(raiz->centro);
        imprimirArv(raiz->dir);
    }
}

Info *buscaPalavra(Arv23 *raiz, char *palavra, Info **aux){

    if(raiz != NULL){
        if(strcmp(palavra, raiz->info1->palavra) == 0)
            *aux = raiz->info1;
        if(raiz->numInfo == 2){
            if(strcmp(palavra, raiz->info2->palavra) == 0)
                *aux = raiz->info2;
        }
        
        if(strcmp(palavra, raiz->info1->palavra) < 0)   
            buscaPalavra(raiz->esq, palavra, aux);
        
        else if((raiz->numInfo == 1) || (raiz->numInfo == 2 && strcmp(palavra, raiz->info2->palavra) < 0))
            buscaPalavra(raiz->centro, palavra, aux);

        else
            buscaPalavra(raiz->dir, palavra, aux);
    }
}


//Remoção baseada no codigo do Nelson
void MaiorInfoRemoveEsq(Arv23 **raiz, Arv23** PaiMaior, Arv23** MaiorInfoRemove, int LocalInfo) {
    if (MaiorInfoRemove != NULL) {
        if ((*MaiorInfoRemove)->esq == NULL) {
            char *aux;
            aux = (char *) malloc(sizeof(char) * 50);
            strcpy(aux, "NOT FOUND");

            if (LocalInfo == 1) {
                strcpy(aux, (*raiz)->info1->palavra);

                if ((*MaiorInfoRemove)->numInfo == 2) {
                    strcpy((*raiz)->info1->palavra, (*MaiorInfoRemove)->info2->palavra);
                    strcpy((*MaiorInfoRemove)->info2->palavra, aux);
                }
                else {
                    strcpy((*raiz)->info1->palavra, (*MaiorInfoRemove)->info1->palavra);
                    strcpy((*MaiorInfoRemove)->info1->palavra, aux);
                }

            }
            else if (LocalInfo == 2) {
                strcpy(aux, (*raiz)->info2->palavra);

                if ((*MaiorInfoRemove)->numInfo == 2) {
                    strcpy((*raiz)->info2->palavra, (*MaiorInfoRemove)->info2->palavra);
                    strcpy((*MaiorInfoRemove)->info2->palavra, aux);
                }
                else {
                    strcpy((*raiz)->info2->palavra, (*MaiorInfoRemove)->info1->palavra);
                    strcpy((*MaiorInfoRemove)->info1->palavra, aux);
                }

            }

            remover23(PaiMaior, MaiorInfoRemove, aux);
        }
        else {
            if ((*MaiorInfoRemove)->numInfo == 2) {
                MaiorInfoRemoveEsq(raiz, MaiorInfoRemove, &((*MaiorInfoRemove)->dir), LocalInfo);
            }
            else if ((*MaiorInfoRemove)->numInfo == 1) {
                MaiorInfoRemoveEsq(raiz, MaiorInfoRemove, &((*MaiorInfoRemove)->centro), LocalInfo);
            }
        } 
    }
    Redistribui(MaiorInfoRemove, PaiMaior);
}

void Redistribui(Arv23 **raiz, Arv23 **pai) {
    if (*raiz != NULL)
        if ((*raiz)->numInfo == 0) {
            if (pai != NULL) {
                if ((*raiz) == ((*pai)->dir)) {
                    if ((*pai)->centro->numInfo == 2) {
                        (*raiz)->info1 = (*pai)->info2;
                        (*raiz)->numInfo = 1;
                        (*pai)->info2 = (*pai)->centro->info2;
                        (*pai)->centro->numInfo = 1;
                        (*raiz)->esq = (*pai)->centro->dir;
                        (*pai)->centro->dir = NULL;
                    }
                    else if ((*pai)->centro->numInfo == 1) {
                        (*raiz)->info2 = (*pai)->info2;
                        (*raiz)->dir = (*raiz)->centro;
                        (*raiz)->info1 = (*pai)->centro->info1;
                        (*raiz)->numInfo = 2;
                        (*pai)->numInfo = 1;
                        (*raiz)->centro = (*pai)->centro->centro;
                        (*raiz)->esq = (*pai)->centro->esq;
                        free((*pai)->centro);
                        (*pai)->centro = (*raiz);
                        (*pai)->dir = NULL;
                    }
                }
                else if ((*raiz) == (*pai)->centro) {
                    if ((*pai)->esq->numInfo == 2) {
                        (*raiz)->info1 = (*pai)->info1;
                        (*raiz)->numInfo = 1;
                        (*pai)->info1 = (*pai)->esq->info2;
                        (*pai)->esq->numInfo = 1;
                        (*raiz)->esq = (*pai)->esq->dir;
                        (*pai)->esq->dir = NULL;
                    }
                    else if ((*pai)->esq->numInfo == 1) {
                        if ((*pai)->numInfo == 2) {
                            (*raiz)->info2 = (*pai)->info1;
                            (*raiz)->info1 = (*pai)->esq->info1;
                            (*raiz)->numInfo = 2;
                            (*raiz)->dir = (*raiz)->centro;
                            (*raiz)->centro = (*pai)->esq->centro;
                            (*raiz)->esq = (*pai)->esq->esq;
                            free((*pai)->esq);
                            (*pai)->esq = (*raiz);
                            (*pai)->info1 = (*pai)->info2;
                            (*pai)->numInfo = 1;
                            (*pai)->centro = (*pai)->dir;
                            (*pai)->dir = NULL;
                        }
                        else if ((*pai)->numInfo == 1) {
                            (*raiz)->info2 = (*pai)->info1;
                            (*raiz)->info1 = (*pai)->esq->info1;
                            (*raiz)->numInfo = 2;
                            (*pai)->numInfo = 0;
                            (*raiz)->dir = (*raiz)->centro;
                            (*raiz)->centro = (*pai)->esq->centro;
                            (*raiz)->esq = (*pai)->esq->esq;
                            free((*pai)->esq);
                            (*pai)->esq = NULL;
                        }
                    }
                }
                else if ((*raiz) == (*pai)->esq) {
                    if ((*pai)->centro->numInfo == 2) {
                        (*raiz)->info1 = (*pai)->info1;
                        (*raiz)->numInfo = 1;
                        (*pai)->info1 = (*pai)->centro->info1;
                        (*pai)->centro->numInfo = 1;
                        (*pai)->centro->info1 = (*pai)->centro->info2;
                        (*raiz)->esq = (*raiz)->centro;
                        (*raiz)->centro = (*pai)->centro->esq;
                        (*pai)->centro->esq = (*pai)->centro->centro;
                        (*pai)->centro->centro = (*pai)->centro->dir;
                        (*pai)->centro->dir = NULL;
                    }
                    else if ((*pai)->centro->numInfo == 1) {
                        if ((*pai)->numInfo == 2) {
                            (*raiz)->info1 = (*pai)->info1;
                            (*raiz)->info2 = (*pai)->centro->info1;
                            (*raiz)->numInfo = 2;
                            (*raiz)->esq = (*raiz)->centro;
                            (*raiz)->centro = (*pai)->centro->esq;
                            (*raiz)->dir = (*pai)->centro->centro;
                            (*pai)->info1 = (*pai)->info2;
                            (*pai)->numInfo = 1;
                            free((*pai)->centro);
                            (*pai)->centro = (*pai)->dir;
                            (*pai)->dir = NULL;
                        }
                        else if ((*pai)->numInfo == 1) {
                            (*raiz)->info1 = (*pai)->info1;
                            (*raiz)->esq = (*raiz)->centro;
                            (*raiz)->info2 = (*pai)->centro->info1;
                            (*raiz)->centro = (*pai)->centro->esq;
                            (*raiz)->dir = (*pai)->centro->centro;
                            (*pai)->numInfo = 0;
                            (*raiz)->numInfo = 2;
                            free((*pai)->centro);
                            (*pai)->centro = (*raiz);
                            (*pai)->esq = NULL;
                        }
                    }
                }
            }
            else if (pai == NULL) {
                (*raiz) = (*raiz)->centro;
            }  
        }
}

void remover23(Arv23 **pai, Arv23 **raiz, char *palavra) {
    if (*raiz != NULL) {
        if (strcmp(palavra, (*raiz)->info1->palavra) == 0) {
            if (folha(*raiz)) {
                if ((*raiz)->numInfo == 2) {
                    (*raiz)->info1 = (*raiz)->info2;
                    (*raiz)->numInfo = 1;
                    (*raiz)->info2 = NULL;
                } else if ((*raiz)->numInfo == 1) {
                    (*raiz)->numInfo = 0;
                }
            } else {
                Arv23 *MaiorInfoRemove = (*raiz)->esq;
                Arv23 *PaiMaior = *raiz;
                MaiorInfoRemoveEsq(raiz, &PaiMaior, &MaiorInfoRemove, 1);
            }
        } else if ((*raiz)->numInfo == 2 && strcmp(palavra, (*raiz)->info2->palavra) == 0) {
            if (folha(*raiz)) {
                (*raiz)->numInfo = 1;
                (*raiz)->info2 = NULL;
            } else {
                Arv23 *MaiorInfoRemove = (*raiz)->centro;
                Arv23 *PaiMaior = *raiz;
                MaiorInfoRemoveEsq(raiz, &PaiMaior, &MaiorInfoRemove, 2);
            }
        } else if (strcmp(palavra, (*raiz)->info1->palavra) < 0) {
            remover23(raiz, &((*raiz)->esq), palavra);
        } else if ((*raiz)->numInfo == 1 || ((*raiz)->numInfo == 2 && strcmp(palavra, (*raiz)->info2->palavra) < 0)) {
            remover23(raiz, &((*raiz)->centro), palavra);
        } else {
            remover23(raiz, &((*raiz)->dir), palavra);
        }
    }
    Redistribui(raiz, pai);
}


void LerArqPalavras(Arv23** RaizArv_23, Info** sobe) 
{
    FILE *Arq;
    char BufferPalavra[50];
    int NumLinha; NumLinha = 1;

    Arq = fopen("palavras23.txt", "r");

    if (Arq == NULL) {
        printf("Erro ao abrir o arquivo.\n");
    }

    while (fscanf(Arq, "%s", BufferPalavra) != EOF) {
        insereOuAtualizaPalavra(RaizArv_23, BufferPalavra, NumLinha, NULL, sobe);
        NumLinha++;
    }
    NumLinha = 0;

    fclose(Arq);
}



//fazer o main para testar a remoção e inserçao lendo o arquivo txt
int main()
{
    Arv23* RaizArv_23;
    RaizArv_23 = NULL;
    Info* sobe;
    sobe = NULL;

    clock_t inicio, fim;
    double busca_tempo;
    LerArqPalavras(&RaizArv_23, &sobe);
    //imprimirArv(RaizArv_23);
    //printf("--------------------------\n");
    //testando remocao
   // remover23(NULL, &RaizArv_23, "artigo");
    //printf("Depois da remocao\n");
    //imprimirArv(RaizArv_23);
   // printf("--------------------------\n");
   //fazer menu com  inserçao e remocao
    char palavra[50];
    int opcao;

    return 0;
}