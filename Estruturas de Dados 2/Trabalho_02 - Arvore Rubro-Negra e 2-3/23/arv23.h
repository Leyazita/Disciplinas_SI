typedef struct Linhas Linhas;
struct Linhas{
    int linha;
    Linhas *prox;
};

typedef struct Info Info;
struct Info{
    char *palavra;
    Linhas *ListaNum;
};

typedef struct Arv23 Arv23;
struct  Arv23 {
    Info *info1, *info2;
    int numInfo;
    Arv23 *esq, *centro, *dir;
};

void inserirLinha(Linhas **no, int linha);

Info *criaInfo(char *palavra, Linhas *lista, int linha);

Arv23 *criaNo(Info *info, Arv23 *noEsq, Arv23 *noCentro);

void lerArquivo();

void adicionaNo(Arv23 **raiz, Info *info, Arv23 *filho);

Arv23 *quebraNo(Arv23 **Raiz, Arv23 *filho, Info *info, Info **infoSobe);

Arv23 *inserePalavra(Arv23 **raiz, char *palavra, int linha, Arv23 *pai, Info **infoSobe);

void insereOuAtualizaPalavra(Arv23 **raiz, char *palavra, int linha, Arv23 *pai, Info **infoSobe);

void imprimirLista(Linhas *no);

void imprimirInfo(Info *info);

void imprimirArv(Arv23 *raiz);

Info *buscaPalavra(Arv23 *raiz, char *palavra, Info **aux);

void Redistribui(Arv23 **raiz, Arv23 **pai);

void MaiorInfoRemoveEsq(Arv23 **raiz, Arv23** PaiMaior, Arv23** MaiorInfoRemove, int LocalInfo);

void remover23(Arv23 **pai, Arv23 **raiz, char *palavra);
