import re # This imports regex module
k = 0 # Just a flag value
email = input() # Takes the email ID as input from the user
pattern = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+') # Stores all possible cases(considered as different possible patterns here) when considered with following constrains
equivalent = pattern.finditer(email) # Stores all locations and matches(in our case, the number of matches found is only one) and their names(strings)
for match in equivalent: # Checks whether the equivalent is empty or not(if empty, email entered is invalid)
    k+=1
if k == 1:
    print('valid email')
else:
    print('not a valid mail')


