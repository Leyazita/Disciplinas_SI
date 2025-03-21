#include <stdio.h>
#include <stdlib.h>

int *menorMaiorMedia(int linha, int coluna, int **mat)
{
	int *vet;
	vet = (int *) malloc(sizeof(int) * 3);
	vet[0] = mat[0][0];
	vet[1] = mat[0][0]; //vetores para auxilar na busca do menor, maior e media
	vet[2] = 0;

	for (int i = 0; i < linha; ++i)
	{
		for (int j = 0; j < coluna; ++j)
		{
			if (mat[i][j] < vet[0])
			{
				vet[0] = mat[i][j];
			}
			if (mat[i][j] > vet[1])
			{
				vet[1] = mat[i][j];
			}
			vet[2] += mat[i][j];
		}
	}
	vet[2] /= (linha * coluna);
	return vet;

}
void exibirvetor(int *vet)
{
	printf("Menor: %d\n", vet[0]);
	printf("Maior: %d\n", vet[1]);
	printf("Media: %d\n", vet[2]);
	
}


int **preencherMatriz(int lin, int col){
	int **mat;
	mat = (int **) calloc(lin, sizeof(int*));
	for (int i = 0; i < lin; ++i)
		{
			mat[i] = (int *) malloc(sizeof(int) * col);
		}	

	for (int i = 0; i < lin; ++i)
	{
		for (int j = 0; j < col; ++j)
		{
			mat[i][j] = rand() % 256;
			//scanf("%d", &mat[i][j]);
		}
	}
	return mat;
}

void mostrarDados(int lin, int col, int **m){
	for (int i = 0; i < lin; ++i)
	{
		for (int j = 0; j < col; ++j)
		{
			printf("%d ", m[i][j]);
		}
		printf("\n");
	}
}
void liberarMemoria(int **m, int t){
	for (int i = 0; i < t; ++i)
	{
		free(m[i]);
	}
	free(m);
}
int main(){
	int **m, lin = 10, col = 5;
	m = preencherMatriz(lin, col);
	mostrarDados(lin, col, m);
	menorMaiorMedia(lin, col, m);
	exibirvetor(menorMaiorMedia(lin, col, m));
	liberarMemoria(m, 10);
	return 0;
}