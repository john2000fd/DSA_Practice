import random


#ARRAYS: FIND SMALLEST

arr = []

for x in range(20):
    val = random.randint(1,1000)
    arr.append(val)


def find_smallest(arr):
    smallest = arr[0]  #STEP 1
    for x in arr: # STEP 2
        print(f"VALUE: ", {x})
        if x < smallest: # STEP 3
            smallest = x
            print(f"NEW SMALLEST FOUND: ", {smallest})
        else:
            pass    
    print(f"SMALLEST IS : ", {smallest}) # STEP 4

find_smallest(arr)