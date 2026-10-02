# AI Lab 03 — Uninformed Search Algorithms

**Artificial Intelligence Lab — BSCS 5th Semester, Air University, Islamabad**

This lab implements the classic *uninformed (blind) search* algorithms from the AI search unit in pure Python. A small road map of northern Pakistan (13 cities, distances in km) is modelled as a weighted graph, and five search strategies are built step by step to find a route from **Peshawar to Lahore**:

- **BFS** — Breadth-First Search
- **DFS** — Depth-First Search
- **UCS** — Uniform-Cost Search
- **DLS** — Depth-Limited Search
- **IDS** — Iterative Deepening Search

Each algorithm is written from scratch on top of a shared `Problem` / `Node` framework, and the final step runs all five on the same route and compares them side by side.

## Lab objectives

By the end of this lab, the following concepts are implemented and compared:

1. Representing a real-world road network as a Python dictionary (adjacency list with edge costs).
2. Formalising a search problem: `initial state`, `actions`, `result`, `goal test`, and `step cost`.
3. The `Node` abstraction: state, parent pointer, path cost *g(n)*, and depth — plus expansion and path reconstruction.
4. How the **frontier data structure** alone changes the search behaviour:
   - FIFO queue → BFS, LIFO stack → DFS, priority queue on *g(n)* → UCS.
5. Depth-limited search with `cutoff` handling and cycle avoidance, and iterative deepening built on top of it.
6. Comparing algorithms on path length (roads), total distance (km), and nodes expanded.

## Tech stack

| Item | Detail |
|---|---|
| Language | Python 3 (developed and tested on Python 3.14; verified on 3.12) |
| Libraries | Python standard library only — `collections.deque`, `heapq` |
| Dependencies | None — no `pip install` required |
| IDE | PyCharm |

## Project structure

```
ai-lab-03/
├── step01_pakistan_map.py   # The road map: 13 cities, weighted two-way roads
├── step02_problem.py        # RouteProblem: initial/actions/result/is_goal/step_cost
├── step03_node.py           # Node: state, parent, cost g(n), depth, expand(), path()
├── step04_bfs.py            # Breadth-First Search (FIFO queue)
├── step05_dfs.py            # Depth-First Search (LIFO stack)
├── step06_ucs.py            # Uniform-Cost Search (priority queue on g(n))
├── step07_dls.py            # Depth-Limited Search (recursive, with cutoff)
├── step08_ids.py            # Iterative Deepening Search (DLS at limits 0,1,2,...)
├── step09_compare.py        # Runs all five algorithms and prints a comparison table
├── main.py                  # Default PyCharm starter file (not part of the lab tasks)
├── 242816.docx              # Lab report with output screenshots for each step
└── README.md
```

The road map used throughout the lab:

| City | Connected roads (km) |
|---|---|
| Peshawar | Nowshera 45, Mardan 60 |
| Rawalpindi | Attock 80, Islamabad 15, Chakwal 90, Jhelum 115 |
| Lahore | Gujranwala 70, Sargodha 190 |
| … | *(full map of 13 cities is in `step01_pakistan_map.py`)* |

## Setup

No installation is needed beyond Python 3:

```bash
git clone https://github.com/hussnainahmedd/ai-lab-03.git
cd ai-lab-03
```

## How to run

Every step is a standalone, runnable script. Each one prints a trace of its own working, so the steps can be run in order to follow the build-up:

```bash
python step01_pakistan_map.py   # prints the map and verifies all roads are two-way
python step02_problem.py        # demos the RouteProblem API on Peshawar → Lahore
python step03_node.py           # demos Node expansion and path reconstruction
python step04_bfs.py            # BFS route Peshawar → Lahore
python step05_dfs.py            # DFS route Peshawar → Lahore
python step06_ucs.py            # UCS route Peshawar → Lahore
python step07_dls.py            # DLS with depth limits 3 (cutoff) and 6 (found)
python step08_ids.py            # IDS, limit by limit, until the goal is found
python step09_compare.py        # full comparison of all five algorithms
```

## Results

Output of `step09_compare.py` (Peshawar → Lahore, verified by running the code):

```
Algorithm  Roads    km  Expanded   Path
------------------------------------------------------------------------------
BFS            6   610        10   Peshawar > Nowshera > Attock > Rawalpindi > Chakwal > Sargodha > Lahore
DFS            8   510         8   Peshawar > Mardan > Swabi > Attock > Rawalpindi > Jhelum > Gujrat > Gujranwala > Lahore
UCS            7   465        12   Peshawar > Nowshera > Attock > Rawalpindi > Jhelum > Gujrat > Gujranwala > Lahore
DLS(6)         6   610        13   Peshawar > Nowshera > Attock > Rawalpindi > Chakwal > Sargodha > Lahore
IDS            6   610        57   Peshawar > Nowshera > Attock > Rawalpindi > Chakwal > Sargodha > Lahore

Cheapest route found by: UCS = 465 km
```

### Observations

- **BFS** finds the route with the fewest roads (6), but at 610 km it is not the cheapest in distance — BFS optimises for number of steps, not cost.
- **UCS** finds the cheapest route (465 km) because it always expands the lowest-cost frontier node first — this is the only cost-optimal result in the table.
- **DFS** dives deep quickly and expands the fewest nodes (8), landing on a mid-cost 510 km route by chance of exploration order.
- **IDS** reaches the same 6-road route as BFS but expands 57 nodes in total, since every iteration re-expands the shallower levels.
- **DLS** with limit 3 correctly returns `cutoff` (Lahore is 6 roads away); with limit 6 it finds the goal.

## Lab report

`242816.docx` is the submitted lab report containing the run-output screenshots for each of the nine steps.

---

*Coursework — Artificial Intelligence Lab, BSCS (5th Semester), Air University.*
