#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

#define MAX_VERTICES 100
#define INF -1e9

typedef struct {
    int vertice;
    float confiabilidade;
} Aresta;

typedef struct {
    Aresta arestas[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} Grafo;

void bellmanFord(Grafo *grafo, int verticeInicial, float dist[], int verticeAnterior[]) {
    // Inicializa as distâncias e vértices anteriores
    for (int i = 0; i < grafo->numVertices; i++) {
        dist[i] = INF; // Inicializa as distâncias com um valor muito baixo
        verticeAnterior[i] = -1; // Inicializa o vetor de vértices anteriores com -1
    }
    
    dist[verticeInicial] = 0; // Define a distância até o vértice inicial como 0
    
    // Relaxamento das arestas
    for (int count = 0; count < grafo->numVertices - 1; count++) {
        for (int vAtual = 0; vAtual < grafo->numVertices; vAtual++) {
            for (int vDestino = 0; vDestino < grafo->numVertices; vDestino++) {
                float confiabilidade = grafo->arestas[vAtual][vDestino].confiabilidade; // Obtém a confiabilidade da aresta entre vertice atual e o de destino
                
                // Verifica se a confiabilidade é válida e se a nova distância é melhor
                if (confiabilidade >= 0 && dist[vAtual] + log(confiabilidade) > dist[vDestino]) {
                    dist[vDestino] = dist[vAtual] + log(confiabilidade); // Atualiza a nova distância para vertice destino
                    verticeAnterior[vDestino] = vAtual; // Marca o vertice atual como vértice anterior do vertice destino
                }
            }
        }
    }
}

void imprimirCaminho(int verticeAnterior[], int vertice) {
    if (verticeAnterior[vertice] != -1) {
        imprimirCaminho(verticeAnterior, verticeAnterior[vertice]);
        printf(" -> ");
    }
    printf("%d", vertice);
}


int main() {
    Grafo grafo;
    int numVertices, numArestas;
    
    printf("Digite o numero de vertices: ");
    scanf("%d", &numVertices);
    
    grafo.numVertices = numVertices;
    
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            grafo.arestas[i][j].confiabilidade = -1;
        }
    }
    
    printf("Digite o numero de arestas: ");
    scanf("%d", &numArestas);
    
    for (int i = 0; i < numArestas; i++) {
        int vAtual, vDestino;
        float confiabilidade;
        
        printf("Digite a aresta %d (vAtual - vDestino - confiabilidade): ", i + 1);
        scanf("%d %d %f", &vAtual, &vDestino, &confiabilidade);
        
        grafo.arestas[vAtual][vDestino].confiabilidade = confiabilidade;
    }
    
    int verticeInicial, verticeFinal;
    
    printf("Digite o vertice inicial: ");
    scanf("%d", &verticeInicial);
    
    printf("Digite o vertice final: ");
    scanf("%d", &verticeFinal);
    
    float dist[MAX_VERTICES];
    int verticeAnterior[MAX_VERTICES];
    
    bellmanFord(&grafo, verticeInicial, dist, verticeAnterior);
    
    if (dist[verticeFinal] > INF) {
        printf("Caminho mais confiavel de %d para %d: ", verticeInicial, verticeFinal);
        imprimirCaminho(verticeAnterior, verticeFinal);
        printf("\n");
        printf("Confiabilidade: %.4f\n", exp(dist[verticeFinal]));
    } else {
        printf("Nenhum caminho confiavel de %d para %d.\n", verticeInicial, verticeFinal);
    }
    
    return 0;
}

