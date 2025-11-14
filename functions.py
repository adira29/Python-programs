# a = int(input("enter the number : "))
# b = int(input("enter the number : "))
# c = int(input("enter the number : "))

# average = (a+b+c)/3

# print(average)


# function defination
def avg():
    a = int(input("enter the number : "))
    b = int(input("enter the number : "))
    c = int(input("enter the number : "))

    average = (a+b+c)/3

    print(average)

avg() #function call


def greet(name, ending):
    print("good day, " + name)
    print(ending)
    return "done"

a = greet("Adira","Thanks")
print(a)

def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry")
goodDay("Rohan", "thanks")

# recursion

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)

n = int(input("enter a number : "))
print(f"the factorial of this number is : {factorial(n)}")



