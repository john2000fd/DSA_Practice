import random
import sys

# BUBBLE SORT IMPLEMENTATION


lis = []
for x in range(21):
    val = random.randint(1,1000)
    lis.append(val)

print(lis)

n = len(lis)
for i in range(n-1):
    for j in range(n-i-1):   # loop goes through one less element each time it runs 
        if lis[j] > lis[j+1]:
            lis[j], lis[j+1] = lis[j+1], lis[j]   # CORRECT SWAP LINE, DO ON SAME LINE 
print(lis)




# UPDATED BUBBLE SORT USING A SWAPPED VAL TO DETERMINE IF A LOOP HAS GONE THROUGH ONCE WITHOUT SWAPPING
# WE DONT NEED TO KEEP RUNNING THE LOOP AS IT HAS BEEN COMPLETELY SORTED
'''
arr = [3,9,21,90,54,32]

n = len(arr)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if swapped != True:
        break
                

print(arr)    
'''






arr = [20,50,34,1,5,67,234,72,12,2,3,4]

n = len(arr)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if swapped != True:
        break 


print(arr)