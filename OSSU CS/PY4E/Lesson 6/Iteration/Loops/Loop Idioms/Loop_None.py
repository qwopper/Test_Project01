# Only use 'is' and 'is not' on boolean values and none types
smallest = None

for value in [9, 23, 41, 7, 3, 65, 45, 64]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)