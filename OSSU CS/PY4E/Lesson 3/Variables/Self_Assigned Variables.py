# The variable 'x' can be changed from its own expression to gain a new value and replace the old value in 'x'
x = 0.6
print(x)
x = 3.9 * x * (1 - x)
print(x)