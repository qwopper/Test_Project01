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
red_bike = bikes[0]
print(red_bike)
red_bike = {'Color': 'Red', 'Price' : '$200'}
print("The bike's color is " + red_bike['Color'])
print("The red bike cost " + red_bike['Price'])
#%%
pi = input('What is the value of pi? ')
pi = float(pi)
print(pi)
# %%
