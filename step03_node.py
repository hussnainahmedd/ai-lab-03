# Step 3: A NODE = state + parent + path cost + depth
from step01_pakistan_map import ROADS
from step02_problem import RouteProblem


class Node:
    def __init__(self, state, parent=None, cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.cost = cost      # g(n): km driven so far
        self.depth = depth    # number of roads taken so far

    def expand(self, problem):         # make one child per action
        children = []
        for a in problem.actions(self.state):
            s = problem.result(self.state, a)
            g = self.cost + problem.step_cost(self.state, a)
            children.append(Node(s, self, g, self.depth + 1))
        return children

    def path(self):                    # follow parents back to start
        node, route = self, []
        while node:
            route.append(node.state)
            node = node.parent
        return route[::-1]

    def __lt__(self, other):           # lets heapq compare two nodes
        return self.cost < other.cost


if __name__ == "__main__":
    p = RouteProblem("Peshawar", "Lahore", ROADS)
    root = Node(p.initial)
    print("Root:", root.state, "| cost:", root.cost)
    for child in root.expand(p):
        print("  child:", child.state, "| cost:", child.cost,
              "| path:", child.path())
    # Walk one branch by hand: Peshawar -> Nowshera -> Attock
    n = root.expand(p)[0].expand(p)[2]
    print("Hand-built path:", n.path(), "=", n.cost, "km")
