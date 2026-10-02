# Step 6: Uniform-Cost Search (priority queue on g(n))
import heapq
from step01_pakistan_map import ROADS
from step02_problem import RouteProblem
from step03_node import Node


def ucs(problem, verbose=True):
    frontier = [(0, Node(problem.initial))]  # (cost so far, node)
    best = {problem.initial: 0}              # cheapest cost found per city
    expanded = 0
    while frontier:
        g, node = heapq.heappop(frontier)    # take the CHEAPEST node
        if g > best[node.state]:
            continue                         # old, costlier copy: skip
        if problem.is_goal(node.state):      # late goal test
            return node, expanded
        expanded += 1
        if verbose:
            print(f"Expand {node.state:<11} g={g:<4}",
                  "| frontier:", sorted((c, n.state) for c, n in frontier))
        for child in node.expand(problem):
            if child.cost < best.get(child.state, float("inf")):
                best[child.state] = child.cost
                heapq.heappush(frontier, (child.cost, child))
    return None, expanded


if __name__ == "__main__":
    p = RouteProblem("Peshawar", "Lahore", ROADS)
    goal, n = ucs(p)
    print("\nUCS path :", " -> ".join(goal.path()))
    print("Roads:", goal.depth, "| Distance:", goal.cost,
          "km | Nodes expanded:", n)
