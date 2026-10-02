# Step 9: Run all five algorithms and compare
from step01_pakistan_map import ROADS
from step02_problem import RouteProblem
from step04_bfs import bfs
from step05_dfs import dfs
from step06_ucs import ucs
from step07_dls import dls
from step08_ids import ids

p = RouteProblem("Peshawar", "Lahore", ROADS)
runs = [
    ("BFS", *bfs(p, verbose=False)),
    ("DFS", *dfs(p, verbose=False)),
    ("UCS", *ucs(p, verbose=False)),
    ("DLS(6)", *dls(p, 6, verbose=False)),
    ("IDS", *ids(p, verbose=False)),
]

print(f"{'Algorithm':<10}{'Roads':>6}{'km':>6}{'Expanded':>10}   Path")
print("-" * 78)
for name, goal, n in runs:
    print(f"{name:<10}{goal.depth:>6}{goal.cost:>6}{n:>10}   "
          + " > ".join(goal.path()))

cheapest = min(runs, key=lambda r: r[1].cost)
print("\nCheapest route found by:", cheapest[0], "=", cheapest[1].cost, "km")
