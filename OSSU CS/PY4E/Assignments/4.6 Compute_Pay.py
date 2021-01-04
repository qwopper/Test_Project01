# Print "Pay 498.75" with 45 hours and rate of 10.5, if hours is passed 40, multiply overtime pay by 1.5 using def function
"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
Do not name your variable sum or use the sum() function.
>>> Pay 498.75
"""

def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours + rate
    return pay


sh = input('Enter hours: ')
sr = input('Enter rate: ')
fh = float(sh)
fr = float(sr)
xp = computepay(fh, fr)
print("Pay", xp)
