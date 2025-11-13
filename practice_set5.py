# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
# 5. s = {}
# What is the type of 's'?
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# 7. If the names of 2 friends are same; what will happen to the program in problem
# 6?
# 8. If languages of two friends are same; what will happen to the program in problem
# 6?
# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}


words = {
    "madad":"Help",
    "kursi":"Chair",
    "billi":"cat"
}

word = input("enter the word you want meaning of: ")

print(words[word])




s = set()
n = input("enter no. 1 : ")
s.add(int(n))
n = input("enter no. 2 : ")
s.add(int(n))
n = input("enter no. 3 : ")
s.add(int(n))
n = input("enter no. 4 :")
s.add(int(n))
n = input("enter no. 5 :")
s.add(int(n))
n = input("enter no. 6 :") 
s.add(int(n))
n = input("enter no. 7 :")
s.add(int(n))
n = input("enter no. 8 :")
s.add(int(n))

print(s)



s = set()
s.add(18)
s.add("18")
print(s)


s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)

# 1==1.0 True
# if value is same, then data type is not required , return true only

print(len(s))



s ={}
print(type(s))


d ={}
name = input("enter friends name : ")
lang = input("enter the language name : ")
d.update({name: lang})
name = input("enter friends name : ")
lang = input("enter the language name : ")
d.update({name: lang})
name = input("enter friends name : ")
lang = input("enter the language name : ")
d.update({name: lang})
name = input("enter friends name : ")
lang = input("enter the language name : ")
d.update({name: lang})

print(d)


s= {8,7,12,"Harry",[1,2]}
# can't update , u cannot even have a list as an element in a set becz sets in Python require all their ele,ments to be immutable and hashable.




