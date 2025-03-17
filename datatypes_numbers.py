#DataTypes in Python
a = 5 #int
b = 'Viji' # str
c = 3.4 #float
d = 1+3j #complex
e = True #Bool
f = [1,2,3] #list
g = (1,2,3) #Tuple
h = {1,2,3} #set
i = {"first":1, "second":2, "third":3} #dictionary
j = range(2) #range
k = frozenset({1,2,3}) #frozenset - Immutable as opposed to set
l = bytes('Hello', 'ascii') #bytes - To encode the string into bytes, by default, uses UTF-8
l1 = b'Hello' #bytes without encoding
m = bytearray(2) #bytearray - similar to bytes, but mutable
n = memoryview(bytes(5)) #memoryview -
o = None #noneType - It is a data type of the class NoneType object. To denote null value or null object
#find the type by type method
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))
print(k, type(k))
print(l, type(l), l[0])
print(l1, type(l1), l1[0])
print(m, type(m), m[0])
print(n, type(n), n[0])
print(o, type(o))



# Creating a memory view of a bytearray
# data = bytearray("Hello", "utf-8")
# data1 = bytes("Hello", "utf-8")
# mv = memoryview(data)
# mv1 = memoryview(data1)
# print(data1)
# print(mv)
# print(mv[0])
# print(mv1)
#mv[1] = 105
#print(data)
