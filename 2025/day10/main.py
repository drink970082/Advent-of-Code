import multiprocessing


def dfs(dp, button, node, search, switch):
    if tuple(sorted(list(search))) in dp:
        return dp[tuple(sorted(list(search)))]
    res = float("inf")
    for i in search:
        for n in node[i]:
            switch[n] = not switch[n]
        if switch == button:
            res = 1
        else:
            res = min(res, 1 + dfs(dp, button, node, search - {i}, switch))
        dp[tuple(sorted(list(search)))] = res
        for n in node[i]:
            switch[n] = not switch[n]
    return res


def part1(input):
    buttons = []
    nodes = []
    for line in input:
        ele = line.split(" ")
        buttons.append([0 if i == "." else 1 for i in ele[0][1:-1]])
        nodes.append([[int(i) for i in s[1:-1].split(",")] for s in ele[1:-1]])
    total = 0
    for i in range(len(buttons)):
        button, node = buttons[i], nodes[i]
        search_idx = set(range(len(node)))
        dp = {}
        total += dfs(dp, button, node, search_idx, [False for _ in range(len(button))])
    return total


import numpy as np
from ortools.sat.python import cp_model


def part2(input):
    """
    minimize     1^T x
    subject to   A x = b
                 x_j ∈ ℤ_{≥ 0}   for all j
    where
    x_j: the number of times button j is pressed (integer, x_j >= 0)
    A: m*n coefficient matrix, where
        A[i, j] = 1 if pressing button j increases switch i by 1, 0 otherwise
    b: length-m target vector, where
        b[i] = the required final value of switch i (integer >= 0)
    Objective: minimize the total number of button presses
        minimize sum_j x_j
    """
    joltages = []
    buttons = []
    for line in input:
        ele = line.split(" ")
        joltages.append([int(i) for i in ele[-1][1:-1].split(",")])
        buttons.append([[int(i) for i in s[1:-1].split(",")] for s in ele[1:-1]])
    res = 0
    for i in range(len(joltages)):
        B = np.array(joltages[i])
        btns = buttons[i]
        m = len(B)
        n = len(btns)
        model = cp_model.CpModel()
        ub = int(B.sum())
        x = [model.NewIntVar(0, ub, f"x_{j}") for j in range(n)]
        for i in range(m):
            model.Add(sum(x[j] for j in range(n) if i in btns[j]) == int(B[i]))
        model.Minimize(sum(x))
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        sol = [int(solver.Value(v)) for v in x]
        res += sum(sol)
    return res
