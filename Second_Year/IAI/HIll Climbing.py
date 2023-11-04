import random
# Define the objective function to be optimized
def objective_function(x, y):
    return x**2 + y**2

# Define the Hill Climbing algorithm
def hill_climbing(initial_point, step_size, objective_function):
    current_point = initial_point
    while True:
        neighbors = [(current_point[0]+step_size, current_point[1]),
            (current_point[0]-step_size, current_point[1]),
            (current_point[0], current_point[1]+step_size),
            (current_point[0], current_point[1]-step_size)]
        neighbor_values = [objective_function(*neighbor) for neighbor in neighbors]
        best_neighbor_value = min(neighbor_values)
        if best_neighbor_value < objective_function(*current_point): current_point = neighbors[neighbor_values.index(best_neighbor_value)]
        else:
            return current_point

# Set the initial point and step size
initial_point = (random.uniform(-10, 10), random.uniform(-10, 10))
step_size = 0.1

# Find the minimum of the objective function using Hill Climbing
minimum_point = hill_climbing(initial_point, step_size, objective_function)
print("Minimum point: {}".format(minimum_point))
print("Minimum value: {}".format(objective_function(*minimum_point)))