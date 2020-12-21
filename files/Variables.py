# Variables are containers which consists of numbers and letters
a = 1 # Variable 'a' refers to the value '1'

print(a)

a, b, c = 1, 2, 3 # Multiple variables can bet set in one line like so

print(a) # = 1
print(b) # = 2
print(c) # = 3

print(a + b + c)

# Trying to make a function to confirm whether or not the value of a, b, or c is greater, less, or equal to the current variable value when math is applied
def A_Value():
    a, b, c = 1, 2, 3
    if c-b == a:
        print(a + ' is the current value equal to a')
    elif c-b < a:
        print('The value is greater than a')
    elif c-b > a:
        print('The value is less than a')  
def B_Value():
    a, b, c = 1, 2, 3
    if c-a == b:
        print(b + ' is the same value equal to b')
    elif c-a < b:
        print('The value is greater b')
    elif c-a > b:
        print('The value is less than b') 
def C_Value():
    a, b, c = new_func()
    if a+b == c:
        print(c + ' is equal to c')
    elif a+b < c:
        print('The value is greater than c')
    elif a+b > c:
        print('The value is less than c')

def new_func():
    a, b, c = 1, 2, 3
    return a,b,c
print(C_Value(any)) # idk what this is

# Swaping variables
v1 = "first string"
v2 = "second string"
print(f'{v1} {v2}')
# Create temporary variables
temp1 = v1
temp2 = v2
# Reassign new variables
v1 = temp2
v2 = temp1
print(f'{v1} {v2}')
