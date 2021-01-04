while True: # Loops until it gets the desired input
    line = input('> ')
    if line == 'done':
        break # When the variable 'line' inputs 'done', it skips the next order in the loop and ends afterwards
    print(line)
print('Done')