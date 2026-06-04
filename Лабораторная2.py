import networkx as nx 

G = nx.Graph() 
edges = [(0, 1), (0, 2), (0, 3)] 
G.add_edges_from(edges) 


eigen_centrality = nx.eigenvector_centrality_numpy(G) 

print("--- Меры центральности в собственных векторах ---") 
for node, centrality in sorted(eigen_centrality.items()): 
    print(f"Узел {node}: {centrality:.4f}") 

values = list(eigen_centrality.values()) 
central_val = eigen_centrality[0] 
ray_vals = [eigen_centrality[1], eigen_centrality[2], eigen_centrality[3]] 

print("\n--- Проверка условий ---") 
print(f"Три периферийных узла имеют одинаковую центральность? {all(x == ray_vals[0] for x in ray_vals)} (Значение: {ray_vals[0]:.4f})") 
print(f"Центральный узел имеет центральность больше остальных? {central_val > ray_vals[0]} (Значение: {central_val:.4f})")
