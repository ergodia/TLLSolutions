"""
calculations_statespace.py

- Calculates the state spaces of different problems
"""


import math

def order_repetition(r,n):
    x = n**r
    return x

def order_no_repetition (r, n):
    x = (math.factorial(n))/(math.factorial(n-r))
    return x

def no_order_no_repetition (r, n):
    x = (math.factorial(n))/((math.factorial(r))*(math.factorial(n-r)))
    return x

def no_order_repetition (r, n):
    x = (math.factorial(r+n-1))/((math.factorial(r))*(math.factorial(n-1)))
    return x

r = 20
n = 3


# exercise 1
r = 12
n = 25

print('\nOpdracht 1:', no_order_no_repetition(r, n))


# exercise 2
r = 20
n = 3

print('Opdracht 2:', no_order_repetition(r, n))


# exercise 3
r = 25
n = 3

print('Opdracht 3:', no_order_repetition(r, n))



# exercise 4
r = 32
n = 110

print('Opdracht 4:', no_order_no_repetition(r, n))


# exercise 5
r = 7
n = 26

print('Opdracht 5:', order_no_repetition(r, n))


# exercise 6
# total 
r = 45
n = 3

x = no_order_repetition(r, n)

# minus 0 - 30 = 31 possibilities, so 45 - 31 = 14
r = 14
n = 3

y = no_order_repetition(r,n)

result = x-y

print('Opdracht 6:', result)

# state space of railNL
r = 61
n = 9

print('State space:', order_repetition(r, n)*20)

# state space 2 of railNL
r = 13
n = 61

print('State space:', order_no_repetition(r, n)*20)
