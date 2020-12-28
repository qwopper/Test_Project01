mari_favorite_food = []
mari_favorite_food.append("MackyCheese")
mari_favorite_food.insert(0,"Pizza")
mari_favorite_food.append("Chocolate")
mari_favorite_food.insert(4, "Poms")
print(mari_favorite_food) # Regular List

mari_favorite_food.reverse() # Reversed list
print(mari_favorite_food)

mari_favorite_food.sort() # Sorted list in alphabetical order
print(mari_favorite_food)

mari_favorite_food.sort(reverse=True) # Reverses list in sort
print(mari_favorite_food)

print(sorted(mari_favorite_food)) # Sorts list only in the print function

print(mari_favorite_food) # List comes back to normal after sorted print function

popped_mari_fav_food = mari_favorite_food.pop()
print(mari_favorite_food)
print(f'The last thing Mari ate is {popped_mari_fav_food}!')

for types in mari_favorite_food:
    print(f"{types} is mari's favorite food!")
    
