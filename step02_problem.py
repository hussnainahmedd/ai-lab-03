# Step 2: Describe the search PROBLEM
from step01_pakistan_map import ROADS


class RouteProblem:
    def __init__(self, initial, goal, roads):
        self.initial = initial
        self.goal = goal
        self.roads = roads

    def actions(self, state):          # where can I drive from here?
        return list(self.roads[state].keys())

    def result(self, state, action):   # driving to a city puts me there
        return action

    def is_goal(self, state):          # have I reached the goal?
        return state == self.goal

    def step_cost(self, state, action):  # km for this one road
        return self.roads[state][action]


if __name__ == "__main__":
    p = RouteProblem("Peshawar", "Lahore", ROADS)
    print("Start:", p.initial, "| Goal:", p.goal)
    print("Actions from Peshawar:", p.actions("Peshawar"))
    print("Result of driving to Mardan:", p.result("Peshawar", "Mardan"))
    print("Cost Peshawar -> Mardan:", p.step_cost("Peshawar", "Mardan"), "km")
    print("Is Lahore the goal?", p.is_goal("Lahore"))
    print("Is Attock the goal?", p.is_goal("Attock"))
