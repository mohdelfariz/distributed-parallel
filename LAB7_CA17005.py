from ortools.linear_solver import pywraplp

# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

# Create data (Two nodes with 6 tasks)
costs = [
    [5, 0, 4, 6, 5, 4],
    [10, 2, 4, 3, 2, 0]
]
num_workers = len(costs)
num_tasks = len(costs[0])

# Create the variables
# x[i, j] is an array of 0-1 variables, which will be 1
# if worker i is assigned to task j.
x = {}
for i in range(num_workers):
    for j in range(num_tasks):
        x[i, j] = solver.IntVar(0, 1, '')

# Create the constraints
# Each worker is assigned to at most 1 task.
for i in range(num_workers):
    solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)

# Each task is assigned to exactly one worker.
for j in range(num_tasks):
    solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)

# Create objective function
objective_terms = []
for i in range(num_workers):
    for j in range(num_tasks):
        objective_terms.append(costs[i][j] * x[i, j])
solver.Minimize(solver.Sum(objective_terms))

# Invoke the solver
status = solver.Solve()

# Print the solution
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('Total cost = ', solver.Objective().Value(), '\n')
    for i in range(num_workers):
        for j in range(num_tasks):
            # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
            if x[i, j].solution_value() > 0.5:
                print('Worker %d assigned to task %d.  Cost = %d' %
                      (i, j, costs[i][j]))

# LAB ASSIGNMENT 5

interTask = [[0, 6, 4, 0, 0, 12],
             [6, 0, 8, 12, 3, 0],
             [4, 8, 0, 0, 11, 0],
             [0, 12, 0, 0, 5, 0],
             [0, 3, 11, 5, 0, 0],
             [12, 0, 0, 0, 0, 0]]

execCost = [[5, 10],
            [0, 2],
            [4, 4],
            [6, 3],
            [5, 3],
            [4, 0]]

# Task 1 : N1 --> T1, T3, T4, T5, T6, 
#          N2 --> T2

# Execution cost = x11 + x31 + x41 + x51 + x61 + x22 
ExecSet1 = 5 + 4 + 6 + 5 + 4 + 2
print(ExecSet1)

# Communication cost = c12 + c32 + c42 + c52 + c62
CommSet1 = 6 + 8 + 12 + 3 + 0
print(CommSet1)

Total1 = ExecSet1 + CommSet1

# Task 2 : N1 --> T4, T5, T6,
#          N2 --> T1, T2, T3

# Execution cost = x41 + x51 + x61 + x12 + x22 + x32
ExecSet2 = 6 + 5 + 4 + 10 + 2 + 4
print(ExecSet2)

# Communication cost = c41 + c51 + c61 + c42 + c52 + c62 + c43 + c53 + c63
CommSet2 = 0 + 0 + 12 + 12 + 3 + 0 + 0 + 11 + 0
print(CommSet2)

Total2 = ExecSet2 + CommSet2

if(Total1 > Total2):
    print("Task assignment 2 is more optimum than Task 1 because the total cost is lesser which is" + Total2)
else:
    print("Task assignment 1 is more optimum than Task 2 because the total cost is lesser which is" + Total1)
