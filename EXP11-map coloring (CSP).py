class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # List of variable names
        self.domains = domains      # Dictionary mapping variables to domains
        self.constraints = constraints  # List of constraint functions

    def is_consistent(self, var, value, assignment):
        for constraint in self.constraints:
            if not constraint(var, value, assignment):
                return False
        return True

    def backtrack_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment  # Solution found
        var = next(v for v in self.variables if v not in assignment)
        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None  # No solution found

# Example usage:
if __name__ == "__main__":
    # Define variables (regions) and their domains (colors)
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['R', 'G', 'B'] for var in variables}

    # Define constraints (adjacent regions cannot have the same color)
    def constraint_function(var, value, assignment):
        adjacent_regions = {'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
                            'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'SA', 'V'], 'V': ['SA', 'NSW', 'T'],
                            'T': ['V']}
        for adjacent in adjacent_regions[var]:
            if adjacent in assignment and value == assignment[adjacent]:
                return False
        return True

    constraints = [constraint_function]

    # Solve the map coloring problem using CSP
    map_coloring = MapColoringCSP(variables, domains, constraints)
    solution = map_coloring.backtrack_search()

    if solution:
        print("Map coloring solution:")
        for var, color in solution.items():
            print(f"{var}: {color}")
    else:
        print("No solution found.")
