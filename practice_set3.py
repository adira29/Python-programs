# 1 problem - Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

name = input("enter your name : ")
print(f"Good Afternoon {name}")

#   2 problem - Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|


letter = """ Dear <|Name|>,
             You are selected!
             <|Date|>"""
print(letter.replace("<|Name|>", "Ram").replace("<|Date|>", "29 Nov 2025"))


# 3 problem - Write a program to detect double space in a string.

name = "Ram is a good  boy and"
print(name.find("  "))

# 4 problem - Replace the double space from problem 3 with single spaces


name = "Ram is a good  boy and"
print(name.replace("  ",""))


# 5 problem - Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Harry, this python course is nice. Thanks!"


letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"

print(letter)