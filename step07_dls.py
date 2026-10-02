# Step 7: Depth-Limited Search (DFS that stops at a depth limit)
from step01_pakistan_map import ROADS
from step02_problem import RouteProblem
from step03_node import Node


def dls(problem, limit, verbose=True):
    count = {"expanded": 0}

    def recurse(node):
        if problem.is_goal(node.state):
            return node
        if node.depth == limit:
            return "cutoff"                  # not allowed to go deeper
        count["expanded"] += 1
        if verbose:
            print("   " * node.depth + f"{node.state} (depth {node.depth})")
        cutoff = False
        for child in node.expand(problem):
            if child.state in node.path():   # don't drive in circles
                continue
            result = recurse(child)
            if result == "cutoff":
                cutoff = True
            elif result is not None:
                return result                # found the goal
        return "cutoff" if cutoff else None

    return recurse(Node(problem.initial)), count["expanded"]


if __name__ == "__main__":
    p = RouteProblem("Peshawar", "Lahore", ROADS)
    for limit in (3, 6):
        print(f"\n--- Depth limit = {limit} ---")
        result, n = dls(p, limit, verbose=(limit == 3))
        if isinstance(result, Node):
            print("Found:", " -> ".join(result.path()),
                  "|", result.cost, "km | expanded:", n)
        else:
            print("Result:", result, "| expanded:", n)
