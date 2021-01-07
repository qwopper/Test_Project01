data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@') # Finding the firt '@' position in the data string
print(atpos) # 21st position in string

sppos = data.find(' ', atpos) # Searching for the first space position after the 'atpos' position
print(sppos)

host = data[atpos + 1 : sppos] # Adds 1 to include the 'u' in 'uct' since it starts from 21-31, it should be  22-23 to print 'uct.ac.za'
print(host)