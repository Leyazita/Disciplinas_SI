#include "score.h"
#include "cliente.h"

float calcular_escore(int entregas_efetuadas, int entregas_nao_efetuadas) {
    float score = 5.0 * entregas_efetuadas + 3.0 * entregas_efetuadas + 2.0 * entregas_efetuadas;
    score -= 0.8 * entregas_nao_efetuadas;
    return score;
}
