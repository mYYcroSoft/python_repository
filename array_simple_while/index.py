array_width = [
    input("Zdajete X: "),
    input("Zdajete Y: "),
]

array =  [
    ["⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬛️", "⬛️", "⬛️", "⬛️"],
]


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


while not q == True:
    array[dot_array[1]][dot_array[0]] = "🟢";
    for arr in array:
        print(" ".join(arr))

    action = input("Zadejte akci:")
    
    if action == 'd':
        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[0] == max_array[0]:
            dot_array[0] += 1
    if action == 'a':
        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[0] == 0:
            dot_array[0] -= 1

    if action == 'w':

        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[1] == 0:
            dot_array[1] -= 1

    if action == 's':
        array[dot_array[1]][dot_array[0]] = "⬛️"
        if not dot_array[1] == max_array[1]:
            dot_array[1] += 1
    
    

      