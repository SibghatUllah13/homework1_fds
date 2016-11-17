# Importing all the important packages for this program
import os
import numpy as np

# Getting a Number as an input from the User. Please only give walid input, otherwise program might crash. It is expected
# here. While it is good to write all the checks here by programmer, I' m only assuming that you would give a Valid input.
print("Tell me the number :")
n=input()
n=int(n)
#Prime Number Coding. The underlying logic is simplest. Any number "n" which can be written as
# "p raise to the power q" while p and q are from the set of natural numbers, is simply not a prime number
# Therefore, I am checking here with a while loop (I already have worked in c++ and Java for a long time, and therefore
# am in the position to use the while loop ) if a given number "n" is divisible by 2......sqrt(n)... If it is divisible
# by any number starting from 2....sqrt(n), i break the loop and print that number, because that number is smallest divisor
# If i dont find such a number untill i reach the sqrt(n), that means this number is a Prime Number because its only divisible by 1 or itself..
# This logic should take less than 1 second for 1 trillion, as i have tested it 
i=2
s=np.sqrt(n)
logical=1
if(n==2):
    print (" Prime Number ")
else:
    while(i<=s):
        if(n % i ==0):
            print(i)
            logical=0
            break
        i=i+1
####################################
if(logical==1):
    print(" Prime ")
####################################


            
            
            
