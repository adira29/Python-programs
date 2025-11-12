# dictionary is a collection of key value pairs.

marks ={
    "Ram":100,
    "Shubham":56,
    "Rohan":23
}

print(marks,type(marks))

print(marks["Ram"])
print(marks["Rohan"])

# it is unordered,mutable,indexed,cannot contain duplicate keys.

# methods


print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ram":99})
print(marks)
 
print(marks.get("Ram2")) #prints None
print(marks["Ram2"]) #returns an error 

d={} # Empty dictionary
print(type(d))


# sets - contains unique value , didn't maintain any order , if you want order use list



s = {1,5,32}
e = set() #empty set

print(type(e))
# Don't use s ={} as it will create an empty dictionary


# sets methods

s = {1,5,32,54,"Ram",5,5,6}
s.add(566)
print(s,type(s))

s.remove(1)
print(s)

s.pop()
print(s)

s1 = {1,45,6}
s2={7,8,1,780}

print(s1.union(s2))

print(s1.intersection(s2))


