# a tuple is an immutable data type in python

a = (1,2,3,4,6)
print(type(a))
b = (1,)
print(type(b))

# a[0] = 9
# print(a) cannot be change 

# methods 

a = (1,2,3,4,6)
no = a.count(2)
print(no)

i = a.index(4)
print(i)

print(2 in a)
