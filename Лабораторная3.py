import networkx as nx
n = 40
p = 0.67

G = nx.erdos_renyi_graph(n, p, seed=42)

theoretical_avg_degree = (n - 1) * p

degrees = [d for node, d in G.degree()]
empirical_avg_degree = sum(degrees) / n

print("--- Сравнение средних степеней вершины ---")
print(f"Теоретическое значение (по формуле) : {theoretical_avg_degree:.4f}")
print(f"Эмпирическое значение (из графа)   : {empirical_avg_degree:.4f}")

deviation = abs(theoretical_avg_degree - empirical_avg_degree)
print(f"Абсолютное отклонение               : {deviation:.4f}")
