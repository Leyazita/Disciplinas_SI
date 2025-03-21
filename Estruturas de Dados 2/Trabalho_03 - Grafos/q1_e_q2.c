#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
#include<time.h>

#define NumVertices 81 //total de vertices
#define NumArestas 3


typedef struct vertice 
{   int Num;
    int Pinos;
    int Arestas[NumArestas];
}Vertice;

int LerVertices(Vertice Vertices[])
{   FILE *Arq = fopen("hanoi.csv", "r");
    int aux = 0;
    if(Arq != NULL)
    {   int i = 0;
        char VetLinha[50];
        int Vertices_lidos;
        int Pinos_lidos;
        char Arestas_lidas[10];
        while(fgets(VetLinha, sizeof(VetLinha), Arq)){
            
            sscanf(VetLinha, "%d,%d,\"%9[^\"]\"\n", &Vertices_lidos, &Pinos_lidos, Arestas_lidas);
            Vertices[i].Num = Vertices_lidos;
            Vertices[i].Pinos = Pinos_lidos;
            char *Aux = strtok(Arestas_lidas, ",");
            int j = 0;
            while(Aux != NULL && j < NumArestas)
            {
                Vertices[i].Arestas[j] = atoi(Aux);
                Aux = strtok(NULL, ",");
                j++;
            }
            while(j < NumArestas)
            {
                Vertices[i].Arestas[j] = -1;
                j++;
            }
            i++;
        }
    }else
        aux+=1;
    fclose(Arq);
    return aux;
}

int ImprimirVertices(Vertice Vertices[])
{   int aux = 0;
    if(Vertices != NULL)
    {
        for(int i = 0; i < NumVertices; i++)
        {
            printf("Numero do Vertice: %d\n", Vertices[i].Num);
            printf("Pinos: %d\n", Vertices[i].Pinos);
            printf("Arestas: ");
            for(int j = 0; j < NumArestas; j++)
            {
                printf("%d ", Vertices[i].Arestas[j]);
            }
            printf("\n");
            aux++;
        }   
    }else
        aux+=1;
    return aux;
}

int InesrirMatriz(int Matriz[][NumVertices], Vertice Vertices[])
{   int aux = 0;
    int i, j, cont;
    if(Vertices != NULL)
    {
        for(i = 0; i < NumVertices; i++)
        {   for(j = 0; j < NumVertices; j++)
            {   cont = 0;
                Matriz[i][j] = 0;
                while(Vertices[i].Arestas[cont] != -1 && cont < NumArestas)
                {   if(Vertices[i].Arestas[cont] - 1 == j){
                        Matriz[i][j] = 1;
                    }
                    cont++;
                }            
            }
        }
    }else
        aux+=1;
    return aux;
}

void ImprimeMatriz(int MatAdjc[][NumVertices]) {
    int i, j;

    for (i = 0; i < NumVertices; i++) {
        for (j = 0; j < NumVertices; j++) {
            printf("%d ", MatAdjc[i][j]);
        }
        printf("\n");
    }
}

int Dijkstra(int Matriz[][NumVertices], int src, int resultado) { //retorna o vetor dist
    int dist[NumVertices];
    int visited[NumVertices];

    for (int i = 0; i < NumVertices; i++) {
        dist[i] = INT_MAX;
        visited[i] = 0;
    }

    dist[src] = 0;

    for (int count = 0; count < NumVertices - 1; count++) {
        int u = -1;
        
        for(int i = 0; i < NumVertices; i++) {
            //printf("\nAquiiiii\n");
            if (!visited[i] && (u == -1 || dist[i] < dist[u])) {
                u = i;
            }
        }
        visited[u] = 1;

        for(int j = 0; j < NumVertices; j++) {
            if(!visited[j] && Matriz[u][j] && dist[u] != INT_MAX && dist[u] + Matriz[u][j] < dist[j]) {
                dist[j] = dist[u] + Matriz[u][j];
            }
        }
    }
    //printf("Menor caminho de %d para %d: %d\n", src, resultado, dist[resultado]);
    if(dist[resultado] == INT_MAX)
        dist[resultado] = -1;
    return dist[resultado];
}
int BellmanFord(int Matriz[][NumVertices], int src, int resultado) {
    int dist[NumVertices];

    for (int i = 0; i < NumVertices; i++) {
        dist[i] = INT_MAX;
    }

    dist[src] = 0;

    for (int count = 0; count < NumVertices - 1; count++) {
        for (int u = 0; u < NumVertices; u++) {
            for (int v = 0; v < NumVertices; v++) {
                if (Matriz[u][v] && dist[u] != INT_MAX && dist[u] + Matriz[u][v] < dist[v]) {
                    dist[v] = dist[u] + Matriz[u][v];
                }
            }
        }
    }
    if(dist[resultado] == INT_MAX)
        dist[resultado] = -1;
    return dist[resultado];
}

void imprimirMenu() {
    printf("----- Menu -----\n");
    printf("1. Ler e Imprimir Vertices\n");
    printf("2. Calcular Menor Caminho usando Dijkstra\n");
    printf("3. Calcular Menor Caminho usando Bellman-Ford\n");
    printf("4. Imprimir Matriz de Adjacencia\n");
    printf("0. Sair\n");
    printf("Escolha uma opcao: ");
}


int main() {
    Vertice Vertices[NumVertices];
    int Matriz[NumVertices][NumVertices];
    int inicio = 1;
    int aux = 0;

    while (1) {
        imprimirMenu();
        
        int opcao;
        scanf("%d", &opcao);
        printf("\n");
        switch (opcao) {
            case 1:
                aux = LerVertices(Vertices);
                if (aux == 0) {
                    printf("Vertices lidos com sucesso!\n");
                    ImprimirVertices(Vertices);
                } else {
                    printf("Erro ao ler vertices.\n");
                }
                break;

            case 2:
                aux = InesrirMatriz(Matriz, Vertices);
                if (aux == 0) {
                    printf("Matriz de adjacencia criada com sucesso!\n");
                    int x = Dijkstra(Matriz, inicio - 1, NumVertices - 1);
                    printf("Menor caminho de %d para %d usando Dijkstra: %d\n", inicio, NumVertices, x);
                } else {
                    printf("Erro ao criar matriz de adjacencia.\n");
                }
                break;

            case 3:
                aux = InesrirMatriz(Matriz, Vertices);
                if (aux == 0) {
                    printf("Matriz de adjacencia criada com sucesso!\n");
                    int y = BellmanFord(Matriz, inicio - 1, NumVertices - 1);
                    printf("Menor caminho de %d para %d usando Bellman-Ford: %d\n", inicio, NumVertices, y);
                } else {
                    printf("Erro ao criar matriz de adjacencia.\n");
                }
                break;
            case 4:
                aux = InesrirMatriz(Matriz, Vertices);
                if (aux == 0) {
                    printf("Matriz de adjacencia criada com sucesso!\n");
                    ImprimeMatriz(Matriz);  
                } else {
                    printf("Erro ao criar matriz de adjacencia.\n");
                }
                break;

            case 0:
                printf("Saindo do programa.\n");
                return 0;

            default:
                printf("Opcao invalida. Escolha uma opcao valida.\n");
        }
    }

    return 0;
}

