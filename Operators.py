a =  4
b = 2
# addition
print(a + b)
#substraction
print(a - b)
#multiplication
print(a * b)
#division
print(a/b)
#modulo
print(a%b)
#exponent
print(a**b)
#floor division
print(14//3)

#Assignment Operator
# =
# +=
# -=
# *=
# /=
# %=
# //=
# **=
# &=
# |=
# ^=
# >>=
# <<=
# :=

#comparison operator - return Bool
print(4 > 2)
print(2 < 1)
print(5 == 8)
print(2 != 7)
print(4 >= 18)
print(4 <= 18)

#logical operators - return Bool
print(5>1 and 4<6)
print(True or False)
print(not(1))

#identity operators - return Bool
x = 5
y=5
print(x is y)
print(x is not y)

#Membership Operators - Return Bool
z = [1,2,3]
print(1 in z)
print(5  not in z)

#Bitwise operators - binary multiplicated result
print(1 & 2) #1 if both bits are 1 else 0
print(1 | 2) # 1 if either of the bits are 1, else 0
print(1 ^ 2) # 1 if only one of the bits is 1
print(~-2) # inverts all the bits
print(3 << 2) # left shit with number of zeros specified at the right side 0000000000000011 becomes 0000000000001100
print(3 >> 2) # right shift with number of zeros specified at the right side 0000000000000011 becomes 0000000000000000


#precedence
# ()	Parentheses
# **	Exponentiation
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
# *  /  //  %	Multiplication, division, floor division, and modulus
# +  -	Addition and subtraction
# <<  >>	Bitwise left and right shifts
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
# not	Logical NOT
# and	AND
# or