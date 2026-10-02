# Step 8: Iterative Deepening Search (DLS with limit 0, 1, 2, ...)
from step01_pakistan_map import ROADS
from step02_problem import RouteProblem
from step03_node import Node
from step07_dls import dls


def ids(problem, max_depth=20, verbose=True):
    total = 0
    for limit in range(max_depth + 1):
        result, n = dls(problem, limit, verbose=False)
        total += n
        found = isinstance(result, Node)
        if verbose:
            print(f"limit={limit}: expanded {n:>3} ->",
                  "FOUND" if found else result)
        if found:
            return result, total
    return None, total


if __name__ == "__main__":
    p = RouteProblem("Peshawar", "Lahore", ROADS)
    goal, n = ids(p)
    print("\nIDS path :", " -> ".join(goal.path()))
    print("Roads:", goal.depth, "| Distance:", goal.cost,
          "km | Total expanded:", n)
