# Simple script that generates a random 
# combination of words from separate strings

colours = ['red','blue','green'.'yellow']
shapes = ['circle','square','triangle','star']

import random
x = random.randint(0, 2)
y = random.randint(0, 2)

combination = colours[x] + (" ") + shapes[y]

print(combination)
