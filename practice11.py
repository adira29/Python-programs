# Q1. Remove duplicate characters from a string
# Problem:

# Input string se duplicates remove karke unique characters print karo.
# (First occurrence ko rakhna hai)

str = "banana"

unique = ""

for x in str:
    if x not in unique:
        unique+= x

print(unique)

# Q2. Print duplicate characters from a string
# Problem:

# Jo characters string me 1 se zyada baar aaye hain, unko print karo.

# Example:
# "mississippi" → i, s, p


str = "mississippi"

unique = ""
dups = ""

for x in str:
    if x in unique and not x in dups:
        print(x)
        dups +=x
    else:
        unique +=x


# Q3. Find the sum of digits present in a string
# Problem:

# String ke andar jitne digits (0–9) hain, unka total sum nikalna hai.

# Example:
# "a1b2c3" → 1 + 2 + 3 = 6

str = "a1b2c3"
total = 0

for x in str:
    if x.isdigit():
        total = total +int(x)
print(total)


# # Q4. Print characters present at even index of a string
# Problem:

# String ke even indexes (0,2,4,6...) par jo characters hain, unko print karna hai.

# Example:
# "abcdef" → a, c, e

str = "abcdef"
print(str[0::2])

# Q5. Reverse the string
# Problem:

# String ko reverse karna hai, bina built-in functions ([::-1] ya .reverse()) use kiye.

# Example:
# "hello" → "olleh"

str = "hello"
rev = ""

for i in range(len(str)-1,-1,-1):

    rev +=str[i]
print(rev)


# String for Q6:
# "zyxwabc"
# Expected output:

# abcwxyz

s = "zyxwabc"
chars = list(s)

for i in range(len(chars)):
    for j in range(i+1, len(chars)):
        if chars[i] > chars[j]:
            chars[i], chars[j] = chars[j], chars[i]

result = "".join(chars)
print(result)


#  Q7 (2nd last character print karna)?

s = "zyxwabc"
chars = list(s)

for i in range(len(chars)):
    for j in range(i+1, len(chars)):
        if chars[i] > chars[j]:
            chars[i], chars[j] = chars[j], chars[i]

result = "".join(chars)
print(result[-2])

# Q8 (smallest & largest character)?

s = "zyxwabc"
chars = list(s)

for i in range(len(chars)):
    for j in range(i+1, len(chars)):
        if chars[i] > chars[j]:
            chars[i], chars[j] = chars[j], chars[i]

result = "".join(chars)
print(result[0])
print(result[-1])