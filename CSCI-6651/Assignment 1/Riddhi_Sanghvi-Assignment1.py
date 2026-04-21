x = "Hello World"
print(x)
print(type(x)) # output <class 'str'>

print("ID of x: ",id(x))   # ID of the object "Hello World"

y = x + "1"
print(y)
#Output Hello World1 i.e. the value of x is modified.

print("ID of x: ",id(x))   # ID of the object "Hello World"
print("ID of Y:",id(y))   # ID of the object "Hello World1"


#x is not modified; instead, a new string object is created (y).
'''Strings in python are immutable. This means that strings cannot be altered once created.
When we concatenate strings, a new string object is created and the variable y points to the new string object, not the original string.
The variable x still points to the original string.
'''