for thing in [9, 23, 41, 65, 45, 64]:
    print(thing)

largest_so_far = -1
print(f'Before: {largest_so_far}')
for the_num in [9, 23, 41, 65, 45, 64]:
    if the_num > largest_so_far:
        print(f'Before: {largest_so_far}, After: {the_num}')
        largest_so_far = the_num
    
print(f'After: {largest_so_far}')