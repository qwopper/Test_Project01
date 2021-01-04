found = False
print(f'Before: {found}')
for value in [9, 23, 41, 65, 45, 64, 46]:
    if value == 65:
        found = True
        print(f'Value = True: {value}')
        #  Insert 'break' here to find immediate true value
    else:
        found = False
        if found == False:
            print(f'Value = False: {value}')

    


