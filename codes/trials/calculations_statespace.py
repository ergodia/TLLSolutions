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


# Opdracht 1
r = 12
n = 25

print('\nOpdracht 1:', no_order_no_repetition(r, n))


# Opdracht 2
r = 20
n = 3

print('Opdracht 2:', no_order_repetition(r, n))


# Opdracht 3
r = 25
n = 3

print('Opdracht 3:', no_order_repetition(r, n))



# Opdracht 4
r = 32
n = 110

print('Opdracht 4:', no_order_no_repetition(r, n))


# Opdracht 5
r = 7
n = 26

print('Opdracht 5:', order_no_repetition(r, n))


# Opdracht 6
# total 
r = 45
n = 3

x = no_order_repetition(r, n)

# minus 0 - 30 = 31 mogelijkheden, dus 45 - 31 = 14
r = 14
n = 3

y = no_order_repetition(r,n)

result = x-y

print('Opdracht 6:', result)

# State space
r = 61
n = 9

print('State space:', no_order_repetition(r, n)*20)
