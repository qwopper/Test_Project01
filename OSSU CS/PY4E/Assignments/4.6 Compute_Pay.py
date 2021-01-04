# Print "Pay 498.75" with 45 hours and rate of 10.5, if hours is passed 40, multiply overtime pay by 1.5 using def function

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
