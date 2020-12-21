squares = [x**3 for x in range(1,11)]
print(squares)

finishers = ['sam', 'bob','kai']
first_person = finishers[0]
second_person = finishers[1]
third_person = finishers[2]
first_two = finishers[:2]
last_two = finishers[-2:]
print(first_two)
print(last_two)
print(third_person)

print(f'Finishers currently have {len(finishers)} names in the list...')
if len(finishers) >= 3:
	print('There are three finishers in the list,' + " I'm adding one more...")
	finishers.append('jose')
	print('Now you have four people in the list...')
	print(finishers)
elif len(finishers) <= 3:
	print('Uh oh, there is one finisher missing in the list count,' + ' Lets add two more to compensate...')
	finishers.append('jose')
	finishers.append('skye')
	print(finishers)
	print ('Well done, you succesfully filled the section with five finishers')