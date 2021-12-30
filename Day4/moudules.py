#modules are a group of functions

print() #the print function is already there we do not have to import

import math
#print(dir(math)) give me direction

print(math.sqrt(4))
print(math.sqrt(9))
print(math.pi)
print(math.floor(9.81)) # 9 making it down
print(math.ceil(9.81)) # 10 making up
print(math.ceil(3.14)) # 4 making up


print(round(5.5)) # the usual rounding
print(round(3.134, 2)) # round it and with two decimals

from math import sqrt, floor, ceil, pi
print(sqrt(2))

from math import sqrt, floor, ceil as roof, pi
print(math.ceil(3.14))

from math import *
print(sqrt(2))

from pprint import pprint

import random 
print(dir(random))
print(random.randint(0, 10))

lottery = []
for i in range(7):
    n = random.randint(0, 10)
    lottery.append(n)

def get_lucky_numbers(n):
    import random
    lottory = []
    for i in range(n):
        n = random.randint(0, 10)
        lottory.append(n)
    return lottory 

print(get_lucky_numbers)










