'''10. Dado um dicionário representando um grafo direcionado, onde as chaves são os vértices e os valores
são listas de vértices adjacentes, crie um algoritmo que retorne o caminho mais curto entre dois
vértices usando o algoritmo de Dijkstra.
Exemplo de entrada: {'A': {'B': 1, 'C': 4}, 'B': {'D': 3}, 'C': {'D': 2}, 'D': {}}, 'A', 'D'
Saída esperada: ['A', 'B', 'D']'''


import heapq

def dijkstra(graph, start, end):
    # Inicialize as distâncias de todos os vértices como infinito e a distância do início como 0.
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Use uma fila de prioridade para manter os vértices não visitados com as menores distâncias na frente.
    queue = [(0, start)]
    
    # Use um dicionário para manter o caminho mais curto para cada vértice visitado.
    shortest_paths = {start: None}
    
    while queue:
        # Obtenha o vértice com a menor distância.
        current_distance, current_vertex = heapq.heappop(queue)
        
        # Se atingirmos o destino, pare.
        if current_vertex == end:
            path = []
            while current_vertex is not None:
                path.append(current_vertex)
                current_vertex = shortest_paths[current_vertex]
            return path[::-1]
        
        # Se ainda não visitamos este vértice, visite e atualize suas distâncias para todos os seus vizinhos.
        if current_distance <= distances[current_vertex]:
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_paths[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))
    
    # Se não encontrarmos o destino, retorne None.
    return None

graph = {'A': {'B': 1, 'C': 4}, 'B': {'D': 3}, 'C': {'D': 2}, 'D': {}}
start = 'A'
end = 'D'

shortest_path = dijkstra(graph, start, end)

print(shortest_path)