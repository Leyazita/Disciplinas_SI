from sklearn.tree import DecisionTreeRegressor, plot_tree
import matplotlib.pyplot as plt
import numpy as np

# Dados
S5 = np.array([1, -1, 1, 1, -1, -1, 1, 1, 1, -1])  # Valores de S5
target = np.array([219, 70, 202, 230, 111, 84, 242, 272, 94, 96])  # Valores do target

# Transformar S5 em um formato 2D necessário para o modelo
S5 = S5.reshape(-1, 1)

# Criar e treinar a árvore de decisão
tree = DecisionTreeRegressor(max_depth=1)  # Profundidade máxima 1
tree.fit(S5, target)

# Plotar a árvore de decisão
plt.figure(figsize=(10, 6))
plot_tree(tree, feature_names=["S5"], filled=True, rounded=True, fontsize=10)
plt.title("Árvore de Decisão")
plt.show()
