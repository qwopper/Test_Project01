fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# Better loop alternate
for letter in fruit:
    print(letter)

# Loop Counting
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print(count)    