#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct disciplina
{
    int codDisc;
    char nomeDisc[50];
    int blocoDisc;
    int cargaHDisc;
    struct disciplina *esq, *dir;
} Disciplina;

typedef struct curso
{
    int codCurso;
    char nomeCurso[40];
    int qtdCursos;
    int num_semanas;
    Disciplina *raizArvDisc;
    struct curso *dir, *esq;
} Curso;

Disciplina *inserirDadosDisc(int codDisc, char nome[], int blocoDisc, int carga) {
    Disciplina *novaDisc = (Disciplina*) malloc (sizeof(Disciplina));
    novaDisc->codDisc = codDisc;
    strcpy(novaDisc->nomeDisc, nome);
    novaDisc->blocoDisc = blocoDisc;
    novaDisc->cargaHDisc = carga;
    novaDisc->esq = NULL;
    novaDisc->dir = NULL;
    return novaDisc;
}

int verificarCodDisc( Disciplina *raizArvDisc, int codDisc)
{   
    int sim = 0;
    if (raizArvDisc != NULL){
        if (raizArvDisc->codDisc == codDisc){
            printf("Codigo ja existe!\n");
            sim = 1;
        } else {
            if (codDisc < raizArvDisc->codDisc){
                verificarCodDisc(raizArvDisc->esq, codDisc);
            } else {
                verificarCodDisc(raizArvDisc->dir, codDisc);
            }
        }
    }
    return sim;
}

void inserirDisciplina(Disciplina **raizArvDisc, Disciplina *novaDisc) {
    if (*raizArvDisc == NULL) {
        *raizArvDisc = novaDisc;
    } else if (novaDisc->codDisc < (*raizArvDisc)->codDisc) {
        inserirDisciplina(&((*raizArvDisc)->esq), novaDisc);
    } else {
        inserirDisciplina(&((*raizArvDisc)->dir), novaDisc);
    }
}

void imprimirDadoDisc(Disciplina *raizArvDisc) {
    if (raizArvDisc != NULL){
        imprimirDadoDisc(raizArvDisc->esq);
        printf("Codigo: %d\n", raizArvDisc->codDisc);
        printf("Nome: %s\n", raizArvDisc->nomeDisc);
        printf("Bloco: %d\n", raizArvDisc->blocoDisc);
        printf("Carga horaria: %d\n\n", raizArvDisc->cargaHDisc);
        imprimirDadoDisc(raizArvDisc->dir);
    }
}

int imprimirArvDiscCurso(Curso *raizArvCurso, int codCurso) {

    int achou = 0;
    if (raizArvCurso != NULL) {
        if(codCurso < raizArvCurso->codCurso)
            achou = imprimirArvDiscCurso(raizArvCurso->esq, codCurso);

        if (raizArvCurso->codCurso == codCurso){
            imprimirDadoDisc(raizArvCurso->raizArvDisc);
            achou = 1;
        }
        if(codCurso > raizArvCurso->codCurso)
            achou = imprimirArvDiscCurso(raizArvCurso->dir, codCurso);

        return (achou);
    }
}

void buscarDisc(Disciplina *raizArvDisc, int codDisc) {
    if (raizArvDisc != NULL){
        if (raizArvDisc->codDisc == codDisc){
            printf("Codigo: %d\n", raizArvDisc->codDisc);
            printf("Nome: %s\n", raizArvDisc->nomeDisc);
            printf("Bloco: %d\n", raizArvDisc->blocoDisc);
            printf("Carga horaria: %d\n\n", raizArvDisc->cargaHDisc);
        } else {
            if (codDisc < raizArvDisc->codDisc){
                buscarDisc(raizArvDisc->esq, codDisc);
            } else {
                buscarDisc(raizArvDisc->dir, codDisc);
            }
        }
    }
}

void imprimirDadosDisc(Curso *raizArvCurso, int codCurso, int codDisc){
    if (raizArvCurso != NULL){
        if (raizArvCurso->codCurso == codCurso){
            buscarDisc(raizArvCurso->raizArvDisc, codDisc);
        } else {
            if (codCurso < raizArvCurso->codCurso){
                imprimirDadosDisc(raizArvCurso->esq, codCurso, codDisc);
            } else {
                imprimirDadosDisc(raizArvCurso->dir, codCurso, codDisc);
            }
        }
    }
}

void buscarDiscBlocos(Disciplina *raizArvDisc, int blocoDisc, int codDisc) {
    if (raizArvDisc != NULL){
        if (raizArvDisc->blocoDisc == blocoDisc){
            printf("\nDados da raizArvDisc:\nCodigo: %d\nNome: %s\nBloco: %d\nCarga horaria: %d\n\n", raizArvDisc->codDisc, raizArvDisc->nomeDisc, raizArvDisc->blocoDisc, raizArvDisc->blocoDisc);
        }
        buscarDiscBlocos(raizArvDisc->esq, blocoDisc, codDisc);
        buscarDiscBlocos(raizArvDisc->dir, blocoDisc, codDisc);
    }
}

void imprimirDisciplinasBloco(Curso *raizArvCurso, int blocoDisc, int codCurso) {
    if (raizArvCurso != NULL){
        if (raizArvCurso->codCurso == codCurso){
            buscarDiscBlocos(raizArvCurso->raizArvDisc, blocoDisc, raizArvCurso->raizArvDisc->codDisc);
        } else {
            if (codCurso < raizArvCurso->codCurso){
                imprimirDisciplinasBloco(raizArvCurso->esq, blocoDisc, codCurso);
            } else {
                imprimirDisciplinasBloco(raizArvCurso->dir, blocoDisc, codCurso);
            }
        }
    }
}

void buscarDiscCargaH(Disciplina *raizArvDisc, int cargaHDisc, int codDisc) {
    if (raizArvDisc != NULL){
        if (raizArvDisc->cargaHDisc == cargaHDisc){
            printf("\nDados da raizArvDisc:\nCodigo: %d\nNome: %s\nBloco: %d\nCarga horaria: %d\n\n", raizArvDisc->codDisc, raizArvDisc->nomeDisc, raizArvDisc->blocoDisc, raizArvDisc->cargaHDisc);
        }
        buscarDiscCargaH(raizArvDisc->esq, cargaHDisc, codDisc);
        buscarDiscCargaH(raizArvDisc->dir, cargaHDisc, codDisc);
    }
}

void imprimirDisCargaHoraria(Curso *raizArvCurso, int codCurso, int cargaHDisc) {
    if (raizArvCurso != NULL){
        if (raizArvCurso->codCurso == codCurso){
            buscarDiscCargaH(raizArvCurso->raizArvDisc, cargaHDisc, raizArvCurso->raizArvDisc->codDisc);
        } else {
            if (codCurso < raizArvCurso->codCurso){
                imprimirDisCargaHoraria(raizArvCurso->esq, codCurso, cargaHDisc);
            } else {
                imprimirDisCargaHoraria(raizArvCurso->dir, codCurso, cargaHDisc);
            }
        }
    }
}

void buscarFolhaDisc(Disciplina **ultimo, Disciplina *folha){
    if ((*ultimo)->dir == NULL){
        (*ultimo)->dir = folha;
    } else {
        buscarFolhaDisc(&((*ultimo)->dir), folha);
    }
}

void removerDisciplina(Disciplina **raizArvDisciplinas,int codDisc)
{
    if (*raizArvDisciplinas != NULL){
        Disciplina *aux;
        if((*raizArvDisciplinas)->codDisc == codDisc){
            if((*raizArvDisciplinas)->esq == NULL && (*raizArvDisciplinas)->dir == NULL){
                free(*raizArvDisciplinas);
                (*raizArvDisciplinas) = NULL;
            }
            //Se tiver apenas um filho
            else if((*raizArvDisciplinas)->esq == NULL || (*raizArvDisciplinas)->dir == NULL){
                Disciplina *endFilho;
                if (    (*raizArvDisciplinas)->esq == NULL){
                    endFilho = (*raizArvDisciplinas)->dir;
                } else {
                    endFilho = (*raizArvDisciplinas)->esq;
                }
                aux = *raizArvDisciplinas;
                *raizArvDisciplinas = endFilho;
                free(aux);
                aux = NULL;
            } else { 
                // Dois Filhos
                Disciplina *filho;
                if ((*raizArvDisciplinas)->esq->dir == NULL){
                    filho = (*raizArvDisciplinas)->esq;
                    filho->dir = (*raizArvDisciplinas)->dir;
                } else {
                    filho = (*raizArvDisciplinas)->esq;
                    buscarFolhaDisc(&((*raizArvDisciplinas)->esq), (*raizArvDisciplinas)->dir);
                }
                aux = *raizArvDisciplinas;
                *raizArvDisciplinas = filho;
                free(aux);
                aux = NULL;
            }
        }
        else if (codDisc < (*raizArvDisciplinas)->codDisc){
            removerDisciplina(&(*raizArvDisciplinas)->esq,codDisc);
        }
        else {
            removerDisciplina(&(*raizArvDisciplinas)->dir,codDisc);
        }
    }
}
                   
void excluirDisc(Curso **raizArvCurso, int codDisc, int codCurso){
    if (*raizArvCurso != NULL){
        if ((*raizArvCurso)->codCurso == codCurso){
            removerDisciplina(&(*raizArvCurso)->raizArvDisc, codDisc);
        }
        else if (codCurso < (*raizArvCurso)->codCurso){
            excluirDisc(&(*raizArvCurso)->esq, codDisc, codCurso);
        }
        else {
            excluirDisc(&(*raizArvCurso)->dir, codDisc, codCurso);
        }
    }
}

Curso *inserirDadosCurso(int codigo, char nomeCurso[], int qtdCursos, int num_semanas) {
    Curso *novoCurso = (Curso*) malloc(sizeof(Curso));
    novoCurso->codCurso = codigo;
    strcpy(novoCurso->nomeCurso, nomeCurso);
    novoCurso->qtdCursos = qtdCursos;
    novoCurso->num_semanas = num_semanas;
    novoCurso->raizArvDisc = NULL;
    novoCurso->esq = NULL;
    novoCurso->dir = NULL;
    return novoCurso;
}

void inserirCurso(Curso **raizArvCurso, Curso *novoCurso) {
    if (*raizArvCurso == NULL)
        *raizArvCurso = novoCurso;
    else if (novoCurso->codCurso < (*raizArvCurso)->codCurso){
        inserirCurso(&((*raizArvCurso)->esq), novoCurso);
    } else {
        inserirCurso(&((*raizArvCurso)->dir), novoCurso);
    }
}

Curso *buscarCurso(Curso *raizArvCurso, int codCurso) {
    if (raizArvCurso == NULL || raizArvCurso->codCurso == codCurso) {
        return raizArvCurso;
    }
    if (codCurso < raizArvCurso->codCurso) {
        return buscarCurso(raizArvCurso->esq, codCurso);
    } else {
        return buscarCurso(raizArvCurso->dir, codCurso);
    }
}

void imprimirArvCursos(Curso *raizArvCurso) {
    if (raizArvCurso != NULL){
        imprimirArvCursos(raizArvCurso->esq);
        printf("Dados:  \n");
        printf("Codigo do curso: %d\n", raizArvCurso->codCurso);
        printf("Nome do curso %s\n", raizArvCurso->nomeCurso);
        printf("Quantidade de blocos: %d\n", raizArvCurso->qtdCursos);
        printf("Numero de semanas: %d\n", raizArvCurso->num_semanas);
        imprimirArvCursos(raizArvCurso->dir);
    }
}

void imprimirDadosCurso(Curso *raizArvCurso, int codCurso) {
    if (raizArvCurso != NULL){
        if (raizArvCurso->codCurso == codCurso){
            printf("Dados:  \n");
            printf("Codigo do curso: %d\n", raizArvCurso->codCurso);
            printf("Nome do curso %s\n", raizArvCurso->nomeCurso);
            printf("Quantidade de blocos: %d\n", raizArvCurso->qtdCursos);
            printf("Numero de semanas: %d\n", raizArvCurso->num_semanas); 
        } else {
            if (codCurso < raizArvCurso->codCurso){
                imprimirDadosCurso(raizArvCurso->esq, codCurso);
            } else {
                imprimirDadosCurso(raizArvCurso->dir, codCurso);
            }
        }
    }
}

void imprimirCursosBlocosIguais(Curso *raizArvCurso, int qtdBlocos) {
    if (raizArvCurso != NULL){
        if (raizArvCurso->qtdCursos == qtdBlocos){
            printf("Codigo do curso: %d\n", raizArvCurso->codCurso);
            printf("Nome do curso %s\n", raizArvCurso->nomeCurso);
            printf("Quantidade de blocos: %d\n", raizArvCurso->qtdCursos);
            printf("Numero de semanas: %d\n", raizArvCurso->num_semanas);
        }
        imprimirCursosBlocosIguais(raizArvCurso->esq, qtdBlocos);
        imprimirCursosBlocosIguais(raizArvCurso->dir, qtdBlocos);
    }
}

void buscarFolhaCurso(Curso **ultimo, Curso *filho) {
    if (*ultimo) {
        buscarFolhaCurso(&((*ultimo)->dir), filho);
    } else {
        (*ultimo) = filho;
    }
}

void excluirCurso(Curso **raizArvCurso, int codCurso) {
    if (*raizArvCurso != NULL) {
        Curso *aux;
        if ((*raizArvCurso)->codCurso == codCurso) {
            if ((*raizArvCurso)->raizArvDisc == NULL) {
                if ((*raizArvCurso)->esq == NULL && (*raizArvCurso)->dir == NULL) {
                    free(*raizArvCurso);
                    *raizArvCurso = NULL;
                } else if ((*raizArvCurso)->esq == NULL || (*raizArvCurso)->dir == NULL) {
                    Curso *endFilho;
                    if ((*raizArvCurso)->esq == NULL) {
                        endFilho = (*raizArvCurso)->dir;
                    } else {
                        endFilho = (*raizArvCurso)->esq;
                    }
                    aux = *raizArvCurso;
                    *raizArvCurso = endFilho;
                    free(aux);
                    aux = NULL;
                } else { // Dois Filhos
                    Curso *filho;
                    aux = *raizArvCurso;
                    filho = (*raizArvCurso)->esq;
                    buscarFolhaCurso(&((*raizArvCurso)->esq), (*raizArvCurso)->dir);
                    *raizArvCurso = filho;
                    free(aux);
                    aux = NULL;
                }
            }
        } else if (codCurso < (*raizArvCurso)->codCurso) {
            excluirCurso(&(*raizArvCurso)->esq, codCurso);
        } else {
            excluirCurso(&(*raizArvCurso)->dir, codCurso);
        }
    }
}


int main() {
    srand(time(NULL));

    Curso  *arvCursos = NULL;
    Curso *aux = NULL;

    int cod_curso, num_semanas, qtd_blocos, cod_disc, bloco_curso, cargaHDisc, bloco_dis;
    char nomeCurso[100], nome_dis[100];

    int opcao = -1;

    do
    {
        printf("\nMenu\n");
        printf("1 - Inserir curso\n");
        printf("2 - Inserir disciplinas\n");
        printf("3 - Imprimir arvore de cursos\n");
        printf("4 - Imprimir dados de um curso\n");
        printf("5 - Imprimir cursos com a mesma quantidade de blocos\n");
        printf("6 - Imprimir arvore de disciplinas pelo codigo\n");
        printf("7 - Imprimir dados de um disciplina\n");
        printf("8 - Imprimir as disciplinas de um determinado blocoDisc\n");    
        printf("9 - Imprimir disciplinas com a mesma carga horaria\n");
        printf("10 - Excluir uma disciplina\n");
        printf("11 - Excluir um curso\n");
        printf("12 - Encerrar\n");

        printf("Digite a opcao: ");
        scanf("%d", &opcao);

        switch (opcao){
            case 1:
                printf("Digite o codigo do curso: ");
                scanf("%d", &cod_curso);
                if (buscarCurso(arvCursos, cod_curso) != NULL)
                {
                    printf("Codigo ja existe!\n");
                    break;   
                }
                printf("Nome do curso: ");
                scanf("%s", nomeCurso);
                printf("Quantidade de blocos: ");
                scanf("%d", &qtd_blocos);
                printf("Numero de semanas: ");
                scanf("%d", &num_semanas);
                inserirCurso(&arvCursos, inserirDadosCurso(cod_curso, nomeCurso, qtd_blocos, num_semanas));
                break;
                
            case 2:
                printf("Digite o codigo do curso: ");
                scanf("%d", &cod_curso);
                aux = buscarCurso(arvCursos, cod_curso);
                if (aux != NULL) {
                    printf("Digite o codigo da disciplina: ");
                    scanf("%d", &cod_disc);
                    if (verificarCodDisc(aux->raizArvDisc, cod_disc) == 1){
                        break;
                    }
                    printf("Nome da disciplina: ");
                    scanf("%s", nome_dis);
                    printf("Bloco da disciplina: ");
                    scanf("%d", &bloco_dis);
                    printf("Carga hoararia da disciplina: ");
                    scanf("%d", &cargaHDisc);
                     if (cargaHDisc % aux->num_semanas != 0){
                        printf("Carga horaria invalida!\n");
                        break;
                    }
                    inserirDisciplina(&aux->raizArvDisc, inserirDadosDisc(cod_disc, nome_dis, bloco_dis, cargaHDisc));
                } else {
                    printf("Curso nao encontrado :/");
                }
                break;

            case 3:
                imprimirArvCursos(arvCursos);
                printf("==================================\n");
                break;

            case 4:
                printf("Digite o codigo do curso: ");
                scanf("%d", &cod_curso);
                imprimirDadosCurso(arvCursos, cod_curso);
                printf("==================================\n");
                break;

            case 5:
                printf("Digite a quantidade de blocos: ");
                scanf("%d", &qtd_blocos);
                imprimirCursosBlocosIguais(arvCursos, qtd_blocos);
                printf("==================================\n"); 
                break;

            case 6:
                printf("Digite o codigo do curso: ");
                scanf("%d", &cod_curso);
                imprimirArvDiscCurso(arvCursos, cod_curso); 
                printf("==================================\n");
                break;

            case 7:
                printf("Digite o codigo da disciplina: ");
                scanf("%d", &cod_disc);
                printf("\nDigite o codigo do curso: ");
                scanf("%d", &cod_curso);
                imprimirDadosDisc(arvCursos, cod_curso, cod_disc);
                printf("==================================\n");
                break;

            case 8:
                printf("Digite o bloco da disciplina: ");
                scanf("%d", &bloco_curso);
                printf("\nDigite o codigo do curso: ");
                scanf("%d", &cod_curso);
                imprimirDisciplinasBloco(arvCursos, bloco_curso, cod_curso); 
                printf("==================================\n");
                break;

            case 9:
                printf("Digite o codigo do curso: ");
                scanf("%d", &cod_curso);
                printf("\nDigite a carga horaria: ");
                scanf("%d", &cargaHDisc);
                imprimirDisCargaHoraria(arvCursos, cod_curso, cargaHDisc); 
                printf("==================================\n");
                break;

            case 10:
                printf("Digite o codigo da disciplina: \n");
                scanf("%d", &cod_disc);
                printf("Digite o codigo do curso: \n");
                scanf("%d", &cod_curso);
                excluirDisc(&arvCursos, cod_disc, cod_curso);
                printf("==================================\n");
                break;

            case 11:
                printf("Digite o codigo do curso: \n");
                scanf("%d", &cod_curso);
                excluirCurso(&arvCursos, cod_curso);
                printf("==================================\n");
                break;
            
            case 12:
                printf("Encerrando...\n");
                break;

            default:
            printf("Essa opcao nao existe\n");
                break;
        }
    } while (opcao != 12);
    return 0;
}