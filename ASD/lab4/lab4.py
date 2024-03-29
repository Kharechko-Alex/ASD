from random import randint
import matplotlib.pyplot as plt
import networkx as nx

# function of generating random graph
def create_graph(length: int) -> list:
    adjacency_matrix = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            buff = randint(0, 1)
            if j > i:
                adjacency_matrix[i][j] = buff
                adjacency_matrix[j][i] = buff
            else:
                continue
    return adjacency_matrix


def print_matrix(matrix: list):
    for i in range(len(matrix)):
        print(*matrix[i])


matrix1 = create_graph(7)
matrix2 = create_graph(10)
print("Matrix 1:")
print_matrix(matrix1)
print("Matrix 2:")
print_matrix(matrix2)


# creating adjacency list from list of adjacency for drawing plot
def create_adjacency_list(matrix: list) -> dict:
    dictionary = {}
    buff_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                buff_list.append(chr(65+j))
        dictionary[chr(65+i)] = sorted(list(set(buff_list)))
        buff_list.clear()
    return dictionary


dictionary1 = create_adjacency_list(matrix1)
dictionary2 = create_adjacency_list(matrix2)
# --- incident matrix ---
for x in dictionary1:
    print(x, ":", dictionary1.get(x))

# init of Graph class object
graph1 = nx.Graph()
for node, neighbors in dictionary1.items():
    graph1.add_node(node)
    for neighbor in neighbors:
        graph1.add_edge(node, neighbor)
graph2 = nx.Graph()
for node, neighbors in dictionary2.items():
    graph2.add_node(node)
    for neighbor in neighbors:
        graph2.add_edge(node, neighbor)

# drawing graph
pos = nx.spring_layout(graph1)
nx.draw(graph1, pos, with_labels=True, font_color='white')
plt.show()
pos = nx.spring_layout(graph2)
nx.draw(graph2, pos, with_labels=True, font_color='white')
plt.show()


# counting distance using wave algorithm
def wave_distance(dictionary: dict, start: str, end: str):
    distances = {node: float('inf') for node in dictionary}
    distances[start] = 0
    queue = [start]
    previous_nodes = {node: None for node in dictionary}
    while queue:
        current_node = queue.pop(0)
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.reverse()
            return distances[end], path
        for neighbor in dictionary[current_node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_node] + 1
                previous_nodes[neighbor] = current_node
                queue.append(neighbor)
    return float('inf'), None

visited = []
for start_point in dictionary1.keys():
    for end_point in dictionary1.keys():
        if (start_point, end_point) not in visited and (end_point, start_point) not in visited:
            visited.append((start_point, end_point))
            print(f'distance between {start_point} and {end_point} : {wave_distance(dictionary1, start_point, end_point)}')

print("\n------Graph 2------\n")
visited = []
for start_point in dictionary2.keys():
    for end_point in dictionary2.keys():
        if (start_point, end_point) not in visited and (end_point, start_point) not in visited:
            visited.append((start_point, end_point))
            print(f'distance between {start_point} and {end_point} : {wave_distance(dictionary2, start_point, end_point)}')
