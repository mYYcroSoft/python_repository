import math
import os 
import random 
terrain = [
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
]




max_x = -1
max_y = len(terrain) -1
for x in terrain:
    for x in x:
        max_x += 1
    break

player_coords = [4,5]
player_inventory = []
player_hunger = 10
player_health = 100

# Generate trees
generated_trees = 0 
while not generated_trees == 8:
    tree_x = random.randint(0, max_x)
    tree_y = random.randint(0, max_y)
    print(f"{tree_y} .. {tree_x}")
    print(f"{max_y} .. {max_x}")
    terrain[tree_y][tree_x] = "🌳"
    generated_trees += 1
# Generate Stone
generated_stones = 0 
while not generated_stones == 8:
    tree_x = random.randint(0, max_x)
    tree_y = random.randint(0, max_y)
    print(f"{tree_y} .. {tree_x}")
    print(f"{max_y} .. {max_x}")
    terrain[tree_y][tree_x] = "🪨"
    generated_stones += 1

# Create player 



# ---------------------
# Player movement 
# ---------------------
terrain[player_coords[1]][player_coords[0]] = "👷🏻";


player_moving = True
while player_moving == True:
        
    for ter in terrain:
        print(" ".join(ter))
    print(f"Health: {player_health} || Hunger: {player_hunger} || Inventory: {player_inventory}")
    action = input("Player command: ")
    
    if action == 'd':
        array[player_coords[1]][player_coords[0]] = "⬛️"
        if not player_coords[0] == max_x:
            player_coords[0] += 1
            check_point()
    if action == 'a':
        array[player_coords[1]][player_coords[0]] = "⬛️"
        if not player_coords[0] == 0:
            player_coords[0] -= 1
            check_point()

    if action == 'w':

        array[player_coords[1]][player_coords[0]] = "⬛️"
        if not player_coords[1] == 0:
            player_coords[1] -= 1
            check_point()

    if action == 's':
        array[player_coords[1]][player_coords[0]] = "⬛️"
        if not player_coords[1] == max_y:
            player_coords[1] += 1
            check_point()