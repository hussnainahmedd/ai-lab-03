# Step 5: Depth-First Search (LIFO stack)
from step01_pakistan_map import ROADS
from step02_problem import RouteProblem
from step03_node import Node


def dfs(problem, verbose=True):
    frontier = [Node(problem.initial)]   # a Python list used as a stack
    done = set()                         # cities already expanded
    expanded = 0
    while frontier:
        node = frontier.pop()            # take the NEWEST node
        if problem.is_goal(node.state):
            return node, expanded
        if node.state in done:
            continue
        done.add(node.state)
        expanded += 1
        if verbose:
            print(f"Expand {node.state:<11}",
                  "| stack:", [n.state for n in frontier])
        for child in node.expand(problem):
            if child.state not in done:
                frontier.append(child)
    return None, expanded


if __name__ == "__main__":
    p = RouteProblem("Peshawar", "Lahore", ROADS)
    goal, n = dfs(p)
    print("\nDFS path :", " -> ".join(goal.path()))
    print("Roads:", goal.depth, "| Distance:", goal.cost,
          "km | Nodes expanded:", n)
