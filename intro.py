

# DSA INTRO

# This tutorial is made to help you learn Data Structures and Algorithms (DSA) fast and easy.

# Data Structures is about how data can be stored in different structures.
# Algorithms is about how to solve different problems, often by searching through and manipulating data structures.


# FIBONACCI SEQUENCE USING A FOR LOOP for values up to 10 
val1 = 0
val2 = 1

for i in range(10):
    fib = val1 + val2
    print(fib)
    val1 = val2
    val2 = fib


# 2. FIBONACCI SEQUENCE USING RECURSION

val_1 = 0
val_2 = 1
count = 2 # initial number of fibonacci nums

def fib(val_1,val_2):   # function
    global count   # change the global count var
    if count <= 19:   # we are creating up to 20 fib nums
        num = val_1 + val_2
        print(num)
        val_1 = val_2
        val_2 = num
        count+=1
        fib(val_1,val_2)
    else:
        return "yes"   
    
fib(val_1,val_2)



# # 2. FIBONACCI SEQUENCE USING RECURSION TO FIND THE Nth FIB USING MATHS

def fib_res(n):
    if n <= 1:
        return n
    else:
        return fib_res(n-1) + fib_res(n-2)
    
print(fib_res(19))
