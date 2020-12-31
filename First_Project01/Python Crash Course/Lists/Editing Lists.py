mari_favorite_food = []
mari_favorite_food.append("MackyCheese")
mari_favorite_food.insert(0,"Pizza")
mari_favorite_food.append("Chocolate")
mari_favorite_food.insert(4, "Poms")
print(mari_favorite_food) # Regular List

mari_favorite_food.reverse() # Reversed list: .reverse()
print(mari_favorite_food)

mari_favorite_food.sort() # Sorted list in alphabetical order: .sort()
print(mari_favorite_food)

mari_favorite_food.sort(reverse=True) # Reverses list in sort: .sort(reverse=True)
print(mari_favorite_food)

print(sorted(mari_favorite_food)) # Sorts list only in the print function temporarily: print(sorted(list name here))

print(mari_favorite_food) # List comes back to normal after sorted print function

popped_mari_fav_food = mari_favorite_food.pop() # Takes element from from list temporarily: .pop()
print(mari_favorite_food)
print(f'The last thing Mari ate is {popped_mari_fav_food}!')

    
nums = [] # Shaun's example of a squared list from 0-12
i = 0   
while i < 12:
    nums.append(i*i)
    i += 1
print(nums)