import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, cost):
        self.edges.setdefault(node1, []).append((node2, cost))
        self.edges.setdefault(node2, []).append((node1, cost))

def astar(graph, start, goal, heuristic):
    frontier = [(0, start)]  # Priority queue of (cost, node)
    came_from = {}  # Parent pointers for reconstructing path
    cost_so_far = {start: 0}  # Cost from start along the best known path

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, current_cost

        for neighbor, cost in graph.edges[current_node]:
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')  # No path found

def euclidean_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Example usage:
# Define a graph
graph = Graph()
graph.add_edge((0, 0), (1, 1), 1)
graph.add_edge((0, 0), (1, 0), 1)
graph.add_edge((1, 0), (1, 1), 1)
graph.add_edge((1, 0), (2, 0), 1)
graph.add_edge((1, 1), (2, 1), 1)
graph.add_edge((2, 0), (2, 1), 1)

# Define heuristic function (Euclidean distance to goal)
def heuristic(node, goal):
    return euclidean_distance(node, goal)

# Find path using A*
start_node = (0, 0)
goal_node = (2, 1)
path, cost = astar(graph, start_node, goal_node, heuristic)

if path:
    print("Shortest path from", start_node, "to", goal_node, ":", path)
    print("Total cost:", cost)
else:
    print("No path found from", start_node, "to", goal_node)
