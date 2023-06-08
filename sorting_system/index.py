from function import *
import math 
import os 
import random 
import time 

numbers_arr =  []

numbers_number = 1000


for x in range(numbers_number):
    add_number(random.randint(0, 5000), numbers_arr)
    print(numbers_arr)

print("----------------")
print("GENERATING DONE")
print("----------------")
time.sleep(5)
for b in range(numbers_number):
    for x in range(len(numbers_arr)):
        if not x +1 == numbers_number:
            if numbers_arr[x] > numbers_arr[x + 1]: 
                num_a = numbers_arr[x]
                num_b = numbers_arr[x + 1]
                numbers_arr[x] = num_b
                numbers_arr[x +1] = num_a
    print(numbers_arr)


print("----------------")
print("SORTING DONE")
print("----------------")
    
print(numbers_arr)  