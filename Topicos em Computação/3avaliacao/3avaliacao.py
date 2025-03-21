import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, cohen_kappa_score

# Carregar os dados
data_path = 'global-data-on-sustainable-energy.csv'
df = pd.read_csv(data_path, decimal=',')

# Remover colunas desnecessárias
columns_to_drop = ['Entity', 'Year', 'Latitude', 'Longitude']
df_numeric = df.drop(columns=columns_to_drop)

# Tratar valores NaN
imputer = SimpleImputer(strategy='mean')
df_numeric = pd.DataFrame(imputer.fit_transform(df_numeric), columns=df_numeric.columns)

# Separar características e rótulo
target_column = 'Access to electricity (% of population)'
X = df_numeric.drop(columns=[target_column])
y = df_numeric[target_column]

# Categorizar a participação de energia renovável
def categorize_renewable_share(share):
    if share < 30:
        return 'Baixa'
    elif share < 60:
        return 'Média'
    else:
        return 'Alta'

y_classification = y.apply(categorize_renewable_share)

# Dividir a base de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_classification, test_size=0.20, random_state=42)

# Dividir a base de dados de teste em teste e validação
X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.20, random_state=42)

# Função para calcular métricas de desempenho
def calculate_metrics(y_true, y_pred, y_prob=None):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    roc_auc = roc_auc_score(LabelBinarizer().fit_transform(y_true), y_prob, multi_class='ovr') if y_prob is not None else None
    kappa = cohen_kappa_score(y_true, y_pred)
    return accuracy, precision, recall, roc_auc, kappa

# Validação cruzada com k-folds = 5
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Inicializar os algoritmos
id3 = DecisionTreeClassifier(random_state=42)
rf = RandomForestClassifier(random_state=42)
svm = SVC(random_state=42, probability=True)
mlp = MLPClassifier(random_state=42, max_iter=10000)

# Lista de algoritmos e cenários
algorithms = [id3, rf, svm, mlp]
scenarios = ['Sem normalização e sem seleção de características',
             'Com normalização, sem seleção de características',
             'Com seleção de características, sem normalização',
             'Com normalização e seleção de características']

# Inicializar o scaler e o seletor
scaler = StandardScaler()
selector = SelectKBest(score_func=f_classif, k=10)

# DataFrame para armazenar resultados
results_df = pd.DataFrame(columns=['Cenário', 'Algoritmo', 'Acurácia', 'Precisão', 'Recall', 'ROC AUC', 'Kappa'])

# Função para adicionar resultados ao DataFrame
def add_results_to_df(scenario, algorithm, metrics):
    results_df.loc[len(results_df)] = [scenario, algorithm, *metrics]

# Função para treinar e avaliar um modelo
def train_and_evaluate_model(scenario, X_train, X_val, y_train, y_val):
    for alg in algorithms:
        alg.fit(X_train, y_train)
        y_pred = alg.predict(X_val)
        y_prob = alg.predict_proba(X_val) if hasattr(alg, 'predict_proba') else None
        metrics = calculate_metrics(y_val, y_pred, y_prob)
        add_results_to_df(scenario, alg.__class__.__name__, metrics)
        print(f"{scenario} - {alg.__class__.__name__}: {metrics}")

# Cenário 1: Sem normalização e sem seleção de características
train_and_evaluate_model(scenarios[0], X_train, X_val, y_train, y_val)

# Cenário 2: Com normalização, sem seleção de características
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
train_and_evaluate_model(scenarios[1], X_train_scaled, X_val_scaled, y_train, y_val)

# Cenário 3: Com seleção de características, sem normalização
X_train_selected = selector.fit_transform(X_train, y_train)
X_val_selected = selector.transform(X_val)
train_and_evaluate_model(scenarios[2], X_train_selected, X_val_selected, y_train, y_val)

# Cenário 4: Com normalização e seleção de características
X_train_scaled_selected = selector.fit_transform(X_train_scaled, y_train)
X_val_scaled_selected = selector.transform(X_val_scaled)
train_and_evaluate_model(scenarios[3], X_train_scaled_selected, X_val_scaled_selected, y_train, y_val)

# Validação cruzada para cada algoritmo e cenário
for alg in algorithms:
    for i, (train_index, val_index) in enumerate(kf.split(X)):
        X_train_fold, X_val_fold = X.iloc[train_index], X.iloc[val_index]
        y_train_fold, y_val_fold = y_classification.iloc[train_index], y_classification.iloc[val_index]
        
        # Cenário 1
        alg.fit(X_train_fold, y_train_fold)
        y_pred_fold = alg.predict(X_val_fold)
        y_prob_fold = alg.predict_proba(X_val_fold) if hasattr(alg, 'predict_proba') else None
        metrics = calculate_metrics(y_val_fold, y_pred_fold, y_prob_fold)
        add_results_to_df(f"CV {i+1} - {scenarios[0]}", alg.__class__.__name__, metrics)
        
        # Cenário 2
        X_train_fold_scaled = scaler.fit_transform(X_train_fold)
        X_val_fold_scaled = scaler.transform(X_val_fold)
        alg.fit(X_train_fold_scaled, y_train_fold)
        y_pred_fold = alg.predict(X_val_fold_scaled)
        y_prob_fold = alg.predict_proba(X_val_fold_scaled) if hasattr(alg, 'predict_proba') else None
        metrics = calculate_metrics(y_val_fold, y_pred_fold, y_prob_fold)
        add_results_to_df(f"CV {i+1} - {scenarios[1]}", alg.__class__.__name__, metrics)
        
        # Cenário 3
        X_train_fold_selected = selector.fit_transform(X_train_fold, y_train_fold)
        X_val_fold_selected = selector.transform(X_val_fold)
        alg.fit(X_train_fold_selected, y_train_fold)
        y_pred_fold = alg.predict(X_val_fold_selected)
        y_prob_fold = alg.predict_proba(X_val_fold_selected) if hasattr(alg, 'predict_proba') else None
        metrics = calculate_metrics(y_val_fold, y_pred_fold, y_prob_fold)
        add_results_to_df(f"CV {i+1} - {scenarios[2]}", alg.__class__.__name__, metrics)
        
        # Cenário 4
        X_train_fold_scaled_selected = selector.fit_transform(X_train_fold_scaled, y_train_fold)
        X_val_fold_scaled_selected = selector.transform(X_val_fold_scaled)
        alg.fit(X_train_fold_scaled_selected, y_train_fold)
        y_pred_fold = alg.predict(X_val_fold_scaled_selected)
        y_prob_fold = alg.predict_proba(X_val_fold_scaled_selected) if hasattr(alg, 'predict_proba') else None
        metrics = calculate_metrics(y_val_fold, y_pred_fold, y_prob_fold)
        add_results_to_df(f"CV {i+1} - {scenarios[3]}", alg.__class__.__name__, metrics)

# Salvar resultados em CSV
results_df.to_csv('3avaliacao.csv', index=False)
print("Experimentos concluídos. Resultados salvos em '3avaliacao.csv'.")
