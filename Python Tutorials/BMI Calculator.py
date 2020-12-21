# BMI means Body Mass Index
name = 'Gertrude'
height_in = 70
weight_lb = 180

BMI = float(((weight_lb) / (height_in ** 2) * 703))
print(f"BMI: {BMI}")
if BMI < 25:
    print(f'{name} is not over weight.')
else:
    print(f'{name} is over weight.')
