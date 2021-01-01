true_str = 'Hello Bob'
try:
    int_str = int(true_str)
except:
    int_str = -1
print("First", int_str)

true_int = '123'
try:
    int_str = int(true_int)
except:
    int_str = -1
print('Second', int_str)

# Combined Conditional Statements
raw_str = input('Enter a number: ')
try:
    input_value = int(raw_str)
except:
    input_value = -1

if input_value > 0:
    print('Nice work')
else:
    print('Not a number')