finishers = ['sam', 'bob','kai']

# Making a list consisting of squares from 1-10
squares = [x**2 for x in range(1,11)]
print(squares)

# Making a list consisting of cubes from 1-10
cubes = [x**3 for x in range(1,11)]
print(cubes)

# Make a list of bikes consisting of different colors
# Append 'black' into the list of bikes
bikes = ['red', 'blue', 'green']
bikes.append('black') # The list should now include four different types of colors
bikes.append(input('What color do you want to add in the list of bikes? ')) # Allows you to input your favorite color if not included
print(bikes)
print(f'There are {len(bikes)} colors in this list now.')
first_bike = bikes[0]
print(first_bike)
first_bike = {'Color': 'Red', 'Price' : '$200'}
print("The bike's color is " + first_bike['Color'])
print("The red bike cost " + first_bike['Price'])
#%%
pi = input('What is the value of pi? ')
pi = float(pi)
print(pi)
# %%

#%%
colors = {"Red", "Blue" , "Yellow", "Green"}
colors_popped = colors.pop()
print(colors_popped)
red_popped = colors.pop(0)
if colors_popped == "Yellow":
    print(f'The color popped is {colors_popped} !')
else:
    print("Dawg nabbit it ain't yellow!")

# %%
