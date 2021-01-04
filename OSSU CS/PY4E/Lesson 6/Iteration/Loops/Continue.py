while True:
    line = input('> ')
    if line[0] == '#':
        continue # If line gets the input '#', it will continue the loop
    if line == 'done':
        break # If line gets the input 'done', it will end the loop
    print (line)
print('Done!')
