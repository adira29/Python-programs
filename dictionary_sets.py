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
 