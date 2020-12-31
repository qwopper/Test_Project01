# Unfriendly variables to set while inconvenient
xlaso = 35.0
xlasp = 12.50
xlasq = xlaso * xlasp
print(xlasq)

# Friendly variables to set while convenient
a = 35.0
b = 12.50
c = a * b
print(c)

# Much better variables which allows the viewer of this code to understand the context
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

# Personal pratice
hours_input = float(input('Enter your total hours: '))
print(f'\nTotal Hours: {hours_input}')
rate_input = float(input('Enter your rate: '))
print(f'Current Rate: {rate_input}')
pay = float(hours_input * rate_input)
print(f'Your total payout for this week is ${pay}')
