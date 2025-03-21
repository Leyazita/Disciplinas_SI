typedef struct conta Conta;

Conta *criarLista();//criar a lista com valor inicial NULL
Conta *inserirInicio(Conta *lista);//inserir elemento em qq lugar de acordo com o valor informado pelo usuario, essa ordem deve ser Crescente
Conta *inserirFim(Conta *lista);//inserir elemento em qq lugar de acordo com o valor informado pelo usuario, essa ordem deve ser Crescente
Conta *inserirOrdenado(Conta *lista);//inserir elemento em qq lugar de acordo com o valor informado pelo usuario, essa ordem deve ser Crescente
Conta *remover(Conta *lista, int valor);//remover um elemento com Info == valor
Conta *buscar(Conta *lista, int valor);//buscar um elemento com info == valor
Conta *alterar(Conta *lista, int oldValue, int newValue); //alterar um elemento com info == valor
int listaVazia(Conta *lista);//verificar se a lista está vazia
void mostrarLista(Conta *lista); // mostar os elementos da lista
void liberarLista(Conta *lista); // liberar memoria alocada