a = 5 #No need to declare the variable
a = 'Viji' #Implicit type casting
print(a) #The latest assigned variable will be considered
#another example
b = 1 + 2j
b = 4.5
print(b)

#variable names can have alphanumeric & _ in the name
a_4 = 'Velammal'
print(a_4)
#Variable Names can start with _ or alphabet but not number
_4 = 'Nijaesh'
print(_4)
# 4a = 'Nijaesh' # SyntaxError: invalid decimal literal
#Variable Names are case sensitive.
a = 5
A = 'sgd'
print(f'{a}{A}')

#Keywords in Python
import keyword
print(keyword.kwlist)