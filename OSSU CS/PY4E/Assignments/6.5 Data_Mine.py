"""
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
>>> 0.8475
"""

text = "X-DSPAM-Confidence:    0.8475"
front_data = text.find('0')
back_data = text.find('5')
print(front_data)
print(back_data)
decimal = float(text[front_data:back_data + 1])
print(decimal)
