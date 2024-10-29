import heapq

def dijkstra(graph, start):
    # ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # купа в нас буде з кортежами (відстань, вершина)
    # поки що єдина відстань, яку ми знаємо, це 0 до самої ж себе (початкової вершини)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # беремо найменший елемент купи
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # пропускаємо, якщо не можемо зробити краще відстань
        if current_distance > distances[current_vertex]:
            continue
            
        # оновлюємо відстані до сусідів поточної вершини у кладемо їх у купу
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

start = 'A'
shortest_distances = dijkstra(graph, start)
print(f"Найкоротші шляхи з {start}:")
for vertex, distance in shortest_distances.items():
    print(F"From {start} to {vertex}: {distance}")