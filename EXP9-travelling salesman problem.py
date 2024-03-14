import itertools

def distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def total_distance(points_order, points):
    """Calculate the total distance of a route."""
    total = 0
    num_points = len(points_order)
    for i in range(num_points):
        total += distance(points[points_order[i]], points[points_order[(i+1) % num_points]])
    return total

def traveling_salesman_brute_force(points):
    """Brute force solution to the Traveling Salesman Problem."""
    num_points = len(points)
    min_distance = float('inf')
    best_route = None
    
    for perm in itertools.permutations(range(num_points)):
        d = total_distance(perm, points)
        if d < min_distance:
            min_distance = d
            best_route = perm
    
    return min_distance, best_route

# Example usage:
# Define points (cities) as (x, y) coordinates
points = [(0, 0), (1, 2), (3, 1), (2, 3)]

# Solve the TSP using brute force
min_distance, best_route = traveling_salesman_brute_force(points)

print("Shortest route:", best_route)
print("Shortest distance:", min_distance)
