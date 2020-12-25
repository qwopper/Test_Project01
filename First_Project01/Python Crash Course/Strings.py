#%%
first_str = "This is how you make a string."
print("A string can be printed by typing 'Print('type here')'")
print(first_str)
second_str = 20
# strings can be created as a container for words or numbers
print(first_str, second_str)
if second_str == 21:
    print('The string is equal to the value of 21!')
elif second_str != 21:
    print('The string is not equal to 21!')

# f-string combines multiple strings into one variable
first_second_str = (f'{first_str} {second_str}')
print(first_second_str)

# %%
