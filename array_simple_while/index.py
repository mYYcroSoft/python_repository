import random
import os
array =  [
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
    ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️",],
]

point_array = []

max1 = -1
for x in array:
    for x in x:
        max1 += 1
    break

max2 = len(array) -1

max_array = [max1,max2]
print(max_array)
q = False
dot_array = [0,4]


#for array in array:
#    array[0] = "🟢"
#    print(array)


generated_points = 0
def generate_points():
    point_x = random.randint(0, 15) 
    point_y = random.randint(0, 14) 
    point_array.append([point_x, point_y])
    print(point_array)
    array[point_x][point_y] = "🔻";
    

while not generated_points == 2:
    generate_points()
    generated_points += 1
 
score = 0
def check_point():
    global score
    
    
    for point in point_array:
       
        print(f"Player: {dot_array[0]} .. {dot_array[1]}")
        print(f"Points: {point[1]} .. {point[0]}")
        if point[1] == dot_array[0]:
            if point[0] == dot_array[1]:
                point_array.remove(point)
                score = score+1 
        
                
                


while not q == True:
    array[dot_array[1]][dot_array[0]] = "🟢";
    for arr in array:
        print(" ".join(arr))

    print(f'Tvoje score je: {score} || Zbývá {len(point_array)} pointů')
    action = input("[w,a,s,d] Zadejte akci:")
    
    if action == 'd':
        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[0] == max_array[0]:
            dot_array[0] += 1
            check_point()
    if action == 'a':
        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[0] == 0:
            dot_array[0] -= 1
            check_point()

    if action == 'w':

        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[1] == 0:
            dot_array[1] -= 1
            check_point()

    if action == 's':
        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[1] == max_array[1]:
            dot_array[1] += 1
            check_point()
    
    os.system('cls')
