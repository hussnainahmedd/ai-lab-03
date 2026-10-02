# Step 4: Breadth-First Search (FIFO queue)
from collections import deque
from step01_pakistan_map import ROADS
from step02_problem import RouteProblem
from step03_node import Node


def bfs(problem, verbose=True):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node, 0
    frontier = deque([node])           # FIFO: first in, first out
    reached = {problem.initial}
    expanded = 0
    while frontier:
        node = frontier.popleft()      # take the OLDEST node
        expanded += 1
        if verbose:
            print(f"Expand {node.state:<11}",
                  "| frontier:", [n.state for n in frontier])
        for child in node.expand(problem):
            if problem.is_goal(child.state):   # early goal test
                return child, expanded
            if child.state not in reached:
                reached.add(child.state)
                frontier.append(child)
    return None, expanded


if __name__ == "__main__":
    p = RouteProblem("Peshawar", "Lahore", ROADS)
    goal, n = bfs(p)
    print("\nBFS path :", " -> ".join(goal.path()))
    print("Roads:", goal.depth, "| Distance:", goal.cost,
          "km | Nodes expanded:", n)
