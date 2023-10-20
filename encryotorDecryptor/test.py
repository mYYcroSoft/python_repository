string = "AJEHJAJOK"
math = [0, 1, 2, 1, 0, 1, 2, 1, 0,1,2, 1, 2, 0, 1,2]
rails = [[], [], []]
string_list = list(string)



for x in range(len(string)):
    print (f'x: {x}  math: {math[x]} > {string_list[x]}')
    print( math[x])
    rail_index = math[x]
    rails[rail_index].append(string_list[x])

print(rails)

