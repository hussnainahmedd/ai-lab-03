# Step 1: The road map as a Python dictionary
# Each city -> {neighbour city: distance in km}

ROADS = {
    "Peshawar":   {"Nowshera": 45, "Mardan": 60},
    "Nowshera":   {"Peshawar": 45, "Mardan": 30, "Attock": 55},
    "Mardan":     {"Peshawar": 60, "Nowshera": 30, "Swabi": 40},
    "Swabi":      {"Mardan": 40, "Attock": 45},
    "Attock":     {"Nowshera": 55, "Swabi": 45, "Rawalpindi": 80},
    "Rawalpindi": {"Attock": 80, "Islamabad": 15,
                   "Chakwal": 90, "Jhelum": 115},
    "Islamabad":  {"Rawalpindi": 15},
    "Chakwal":    {"Rawalpindi": 90, "Sargodha": 150},
    "Jhelum":     {"Rawalpindi": 115, "Gujrat": 50},
    "Gujrat":     {"Jhelum": 50, "Gujranwala": 50},
    "Gujranwala": {"Gujrat": 50, "Lahore": 70},
    "Sargodha":   {"Chakwal": 150, "Lahore": 190},
    "Lahore":     {"Gujranwala": 70, "Sargodha": 190},
}

if __name__ == "__main__":
    print("Cities on the map:", len(ROADS))
    for city, nbrs in ROADS.items():
        print(f"{city:<11} -> {nbrs}")
    # Check: every road works in both directions
    ok = all(ROADS[b][a] == d for a in ROADS for b, d in ROADS[a].items())
    print("All roads two-way?", ok)
