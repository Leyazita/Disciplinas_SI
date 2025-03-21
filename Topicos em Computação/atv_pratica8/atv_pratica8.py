import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, cohen_kappa_score

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

# Normalização
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=0.95)  
X_pca = pca.fit_transform(X_normalized)

# Função para avaliação do modelo
def evaluate_model(X_train, y_train, X_test, y_test, n_splits, hidden_layers):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    metrics = {'accuracy': [], 'precision': [], 'recall': [], 'f1': [], 'auc': [], 'kappa': []}

    for train_index, val_index in kf.split(X_train):
        X_train_fold, X_val = X_train[train_index], X_train[val_index]
        y_train_fold, y_val = y_train.iloc[train_index], y_train.iloc[val_index]

        mlp = MLPClassifier(hidden_layer_sizes=hidden_layers, max_iter=10000, random_state=42)
        mlp.fit(X_train_fold, y_train_fold)
        y_pred = mlp.predict(X_test)
        y_prob = mlp.predict_proba(X_test)

        metrics['accuracy'].append(accuracy_score(y_test, y_pred))
        metrics['precision'].append(precision_score(y_test, y_pred, average='weighted'))
        metrics['recall'].append(recall_score(y_test, y_pred, average='weighted'))
        metrics['f1'].append(f1_score(y_test, y_pred, average='weighted'))
        metrics['auc'].append(roc_auc_score(y_test, y_prob, multi_class='ovr'))
        metrics['kappa'].append(cohen_kappa_score(y_test, y_pred))

    means = {f'{key}_mean': np.mean(values) for key, values in metrics.items()}
    stds = {f'{key}_std': np.std(values) for key, values in metrics.items()}
    
    return means, stds

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y_classification, test_size=0.2, random_state=42)
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y_classification, test_size=0.2, random_state=42)

# Configurações dos experimentos
layer_settings = [((10, 5), '2 Layers'), ((50, 30, 10), 'Many Layers')]
kf_settings = [(5, '5 Folds'), (50, '50 Folds')]

# Execução dos experimentos
results = {}

# Testes sem PCA
for hidden_layers, layer_label in layer_settings:
    for n_splits, kf_label in kf_settings:
        key = f'No PCA_{kf_label}_{layer_label}'
        means, stds = evaluate_model(X_train, y_train, X_test, y_test, n_splits=n_splits, hidden_layers=hidden_layers)
        results[key] = {**means, **stds}

# Testes com PCA
for hidden_layers, layer_label in layer_settings:
    for n_splits, kf_label in kf_settings:
        key = f'PCA_{kf_label}_{layer_label}'
        means, stds = evaluate_model(X_train_pca, y_train_pca, X_test_pca, y_test_pca, n_splits=n_splits, hidden_layers=hidden_layers)
        results[key] = {**means, **stds}

# Exibir resultados
results_df = pd.DataFrame(results).T
print(results_df)

# Salvar resultados em CSV
results_df.to_csv('results.csv', index_label='Configuração')
