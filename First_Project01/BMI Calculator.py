# BMI means Body Mass Index
name_1 = 'Gertrude'
height_in_1 = 70
weight_lb_1 = 180

name_2 = 'Alexa'
height_in_2 = 48
weight_lb_2 = 100

name_3 = 'Chaz'
height_in_3 = 69
weight_lb_3 = 170

BMI = float(((weight_lb_1) / (height_in_1 ** 2) * 703))
print(f"BMI: {BMI}")
if BMI < 25:
    print(f'{name_1} is not over weight.')
else:
    print(f'{name_1} is over weight.')

def BMI_Calc(name, weight_lb, height_in):
    BMI = int(((weight_lb) / (height_in ** 2) * 703))
    print(f"BMI: {BMI}")
    if BMI < 25:
        print(f'{name} is not over weight')
    else:
        print(f'{name} is over weight')      
BMI_Calc(name_1, weight_lb_1, height_in_1)
BMI_Calc(name_2, weight_lb_2, height_in_2)
BMI_Calc(name_3, weight_lb_2, height_in_3)