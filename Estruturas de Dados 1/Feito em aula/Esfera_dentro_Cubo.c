#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//funcao que retorna a distancia euclidiana de um ponto
float distancia(int x1, int x2, int y1, int y2, int z1, int z2){
    int diffX, diffY, diffZ;
    diffX = pow(x2 - x1, 2);
    diffY = pow(y2 - y1, 2);
    diffZ = pow(z2 - z1, 2);
    return sqrt(diffX + diffY + diffZ);
}

int ***preencherCubo(int profundidade, int altura, int largura){

    int ***cubo;
    //alocando o espaco de memoria para o CUBO
    cubo = (int ***) malloc(profundidade * sizeof(int **));
    for (int i = 0; i < profundidade; ++i)
        cubo[i] = (int **) malloc(sizeof(int *) * altura);

    for (int i = 0; i < profundidade; ++i)
        for (int j = 0; j < altura; ++j)
            cubo[i][j] = (int *) malloc(sizeof(int) * largura);

    //preenchendo o cubo com valores randomicos de 0 - 255
    for (int i = 0; i < profundidade; ++i)
        for (int j = 0; j < altura; ++j)
            for (int x = 0; x < largura; ++x)
            {
                cubo[i][j][x] = 0;
            }

    //tentando gerar uma esfera dentro do CUBO
    int raio = 6;
    int xc, yc, zc;
    xc = largura / 2;
    yc = altura / 2;
    zc = profundidade / 2;
    for (int z = 0; z < profundidade; ++z){
        for (int y = 0; y < altura; ++y){
            for (int x = 0; x < largura; ++x)
            {
                if (distancia(xc, x, yc, y, zc, z) <= raio)
                {
                    cubo[z][y][x] = 1;
                }

            }
        }
    }

    //retornando o espaco de memoria alocado e preenchido
    return cubo;
}

void mostrarCubo(int largura, int altura, int profundidade, int ***cubo){
	for (int i = 0; i < profundidade; ++i){
		for (int j = 0; j < altura; ++j){
			for (int x = 0; x < largura; ++x)
			{
				printf("%d ", cubo[i][j][x]);
			}
			printf("\n");
		}
		printf("\n");
	}
}

int main(int argc, char const *argv[])
{
    int largura = 15, altura = 15, profundidade = 15;
    

    int ***cubo = preencherCubo(profundidade, altura, largura);
    mostrarCubo(largura, altura, profundidade, cubo);

    return 0;
}
