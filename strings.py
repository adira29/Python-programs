# we can primarily write a string in these three ways.

a='harry'
b="harry"
c='''harry'''

name ="Harry"
# string is immutable
nameshort = len(name)
nameshort = name[0:3]
print(nameshort)
character1 = name[1]
print(character1)


name = "Harry"
print(name[0:3])
print(name[-4:-1])
print(name[:4]) #starts from 0 to 4

word = "amazing"
print(word[1:6:2])
word = "amazing"
print(word[:7])

print(name.endswith("rry"))

a = "Ram is a good boy \n but not a bad boy"

print(a)

