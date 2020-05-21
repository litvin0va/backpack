import pulp

def run_algorithm(prices, weights, max_сapacity, size):
    x = []
    for i in range(size):
        name = "x" + str(i)
        x.append(pulp.LpVariable(name, lowBound = 0, upBound = 1, cat = pulp.LpInteger))
    problem = pulp.LpProblem('0-1', pulp.LpMaximize)

    problem += pulp.lpSum(prices[i] * x[i] for i in range(size))
    problem += pulp.lpSum(weights[i] * x[i] for i in range(size)) <= max_сapacity
    problem.solve()
    ans = 0
    for variable in problem.variables():
        if variable.varValue != 0:
            fix = variable.name.split("x")
            ans += prices[int(fix[1])]
    return ans
