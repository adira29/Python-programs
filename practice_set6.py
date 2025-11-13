# #1 . Write a program to find the greatest of four numbers entered by the user.
# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
# 4. Write a program to find whether a given username contains less than 10
# characters or not.
# 5. Write a program which finds out whether a given name is present in a list or not.
# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
# 7. Write a program to find out whether a given post is talking about “Harry” or not.



a1 = int(input("enter no.1 : "))
a2 = int(input("enter no.2 : "))
a3 = int(input("enter no. 3: "))
a4 = int(input("enter no.4 : "))

if(a1>a2 and a1>a3 and a1>a4):
    print("greatest no. is a1", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greater", a3)

else:
    print("a4 is greatest", a4)


marks1 = int(input("enter marks 1 : "))
marks2 = int(input("enter marks 2 :"))
marks3 = int(input("enter marks 3 : "))

# check for percentage 

total_percentage = (100*(marks1 + marks2 +marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3 >=33):
    print("you are pass", total_percentage)
else:
    print("you failed",total_percentage)

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("enter your comment : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message )):
    print("this message is spam")

else:
    print("this comment is not a spam")


username = input("enter user name :")

if(len(username) <=10):
    print("your username contains less than 10 characters")

else:
    print("all good")



l = ["Harry","Rohan","Shubham","Divya"]

name = input("enter your name : ")

if(name in l ):
    print("your name is in the list")

else:
    print("your name is not in the list")


marks = int(input("enter the marks to get the result : "))

if(marks<=100 and marks>=90):
    print("grade is EX ")

elif(marks<90 and marks>=80):
    print("grade is A ")

elif(marks<80 and marks>=70):
    print("grade is B")

elif(marks<70 and marks >=60):
    print("grade is C ")

elif(marks<60 and marks >= 50):
    print("grade is D")
else:
    print("grade is F ")

print("end of result checking , thanks for your time ")




post = "Hey harry is good "

if("harry".lower() in post.lower()):
    print("this post is about harry")
else:
    print("this post is not talking about harry")


