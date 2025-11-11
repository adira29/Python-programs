#  1. Write a program to store seven marks in a list entered by the user.
# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.
# 3. Check that a tuple type cannot be changed in python.
# 4. Write a program to sum a list with 4 numbers.
# 5. Write a program to count the number of zeros in the following tuple:


fruits= []
f1 = input("enter  name : ")
fruits.append
f2 = input("enter  name : ")
fruits.append
f3 = input("enter  name : ")
fruits.append
f4 = input("enter  name : ")
fruits.append
f5 = input("enter  name : ")
fruits.append
f6 = input("enter  name : ")
fruits.append
f7 = input("enter  name : ")
fruits.append(f7)


print(fruits)


marks = []

m1 = int(input("enter mark here : "))
marks.append(m1)
m2 = int(input("enter mark here : "))
marks.append(m2)
m3 = int(input("enter mark here : "))
marks.append(m3)
m4 = int(input("enter mark here : "))
marks.append(m4)
m5 = int(input("enter mark here : "))
marks.append(m5)
m6= int(input("enter mark here: ")) 
marks.append(m6)

marks.sort()

print(marks)


a= (34,234,"Ram")
a[2] = "Larry"

l = [34,23,645,123]

print(sum(l))



a=(7,0,8,0,0,9)
n = a.count(0)
print(n)