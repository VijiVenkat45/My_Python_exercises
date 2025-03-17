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
#Import - to import packages and modules
import keyword
print(keyword.kwlist)
#False - Boolean Data Type to denote 0 or false
print(1 > 2)
#None - None type (null value or null object)
FF = None
print(FF, type(FF))
#True - Boolean Data Type to denote 1 or True
print(2 >1 )
#and - logical operator
print(1<2 and 2>1)
#as - alias name
#assert - Used to debug code
x = 5
assert x == 5 #checks if x is 5 in your code
#async - used to define asynchronous functions
#await - is used to pause the execution of a task until the result of another task or operation is ready. used in asynchronous programming

#def - keyword used to define function
def sumsamp(x):
    return x+2
print(sumsamp(2))
#class - keyword to define class
#del - keyword to delete object
class bingo():
    def __init__(self, name):
        self.name = name

o = bingo('hive')
del o

#elif - Else if keyword (more than one condition)
# if - conditional statement
#else - if not satisfied
def odd_or_even(_x):
    if _x == 0:
        print('even')
    elif (_x % 2 == 0):
        print('even')
    else:
        print('Odd')

odd_or_even(4)
#

#for - looping command
#in - to check if values is in the collection or iterate in the loop
ex = 'Viji'
for x in ex:
    print(x)

#lambda - Anonymous function
def times_five(x):
    return lambda a: a * x

a=times_five(5)
print(a(2))

#From - to specify the module from which packages can be imported
from math import sqrt

#Global - to specify the scope of variable even outside a function
bub = 3
def whatcha():
    global bub
    bub = 4
    print(bub)

whatcha()

#break - exists out of the loop itself
#continue - exists out of the current iteration and proceeds to the next iteration
#pass - does nothing
sig = ['green','yellow','red']
for ele in sig:
    if ele == 'red':
        break
    elif ele == 'yellow':
        continue
    else:
        pass


#while - looping statement with condition check first
i = 5
while i > 0:
    print(i)
    i -= 1

#or - logical statement - returns True if any of the condition returns true
print(1>2 or 3>1)
#not - logic to give complement
print(not True)