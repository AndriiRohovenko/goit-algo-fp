import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def array_to_min_heap(arr):
    heapq.heapify(arr)
    return arr

def create_heap_tree(arr):
    """Функція для побудови бінарного дерева з мін-купи (масиву)."""
    nodes = [Node(key) for key in arr]  # Створення вузлів для кожного елемента

    # Побудова дерева з масиву
    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]
    
    return nodes[0]

def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root, search=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if search == "dfs":
        dfs_colors = {}
        dfs_colors = dfs_visualize(tree_root, dfs_colors, total_steps=len(tree.nodes))
        colors = [dfs_colors[node_id] for node_id in tree.nodes()]  # Colors for DFS traversal
    elif search == "bfs":
        bfs_colors = bfs_visualize(tree_root, total_steps=len(tree.nodes))
        colors = [bfs_colors[node_id] for node_id in tree.nodes()]  # Colors for BFS traversal
    else:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Node labels

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color(index):
    # Generate color based on index (for differentiation in visualization)
    r = hex(int(25 + index * 10) % 256)[2:].zfill(2)
    g = hex(int(200 - index * 10) % 256)[2:].zfill(2)
    b = hex(int(100 + index * 20) % 256)[2:].zfill(2)
    return '#' + r + g + b

def dfs_visualize(root, colors, total_steps):
    visited = set()
    stack = [root]
    step = 0

    while stack and step < total_steps:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(step)  # Assign a color based on the step
            step += 1
            
            # Add children to stack in reverse order to visit left child first
            if node.right and node.right not in visited:
                stack.append(node.right)
            if node.left and node.left not in visited:
                stack.append(node.left)

    # Optional: Assign a color to unvisited nodes
    for unvisited_node in stack:
        colors[unvisited_node.id] = "lightgray"

    return colors

def bfs_visualize(root, total_steps=1):
    visited = set()
    queue = [root]
    colors = {}
    step = 0

    while queue and step < total_steps:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(step)  # Assign a color based on the step
            step += 1
            
            # Add children to queue in order to visit level by level
            if node.left and node.left not in visited:
                queue.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)

    return colors

arr = [0, 4, 5, 10, 1, 3]
min_heap = array_to_min_heap(arr)
root = create_heap_tree(min_heap)
draw_tree(root, "dfs")
draw_tree(root, "bfs")