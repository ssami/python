# list comprehension

import random 

rnums = [ random.randint(0, 10) for i in range(50) ]

def even_only(n):
    return n % 2 == 0

filtered_list = filter(even_only, rnums)
print filtered_list
filtered_list = filter(lambda x: x % 2 == 0, rnums)
print filtered_list