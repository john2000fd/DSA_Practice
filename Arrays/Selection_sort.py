import random

# SELECTION SORT ALGORITHM IMPLEMENTATION
# THIS FINDS SMALLEST ELEMENT IN THE ARRAY EACH ITERATION, PLACES IT AT THE FRONT OF THE ARRAY  

'''
print(arr)
n = len(arr)
for i in range(n-1):
    smallest = i # SMALLEST INDEX Is val
    for j in range(i+1, n):
        if arr[j] < arr[smallest]:  
            smallest = j
        else:
            pass  
    min_value = arr.pop(smallest)    # POP/REMOVE SMALLEST VALUE
    arr.insert(i,min_value)    # INSERT SMALLEST AT THE BEGINNING OF UNSORTED ARRAY    

print(arr)        
'''
# look through array to find smallest value
# place that at the front of the unsorted array
# go through the array as many times as there is elements



# SELECTION SORT OPTIMISATION USING SWAPPING VARIABLES RATHER THEN ARRAY POP/INSERT.
# AVOIDS ARRAY ELEMENT SHIFTING
'''
arr = []
for x in range(10):
    val = random.randint(1, 20)
    arr.append(val)

n = len(arr)

for i in range(n-1):
    smallest = i
    for j in range(i+1, n):
        if arr[j] < arr[smallest]:
            smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]        

print(arr)
'''




arr= []

for x in range(10):
    val = random.randint(1,20)
    arr.append(val)
print(arr)
n = len(arr)

# select sort
for i in range(n-1):
    smallest = i
    for j in range(i+1, n):
        if arr[j] < arr[smallest]:
            smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]        

print("This is our sorted array using selection sort", arr)