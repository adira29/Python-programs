# Array 
# 1.Remove duplicate 
# 2. Print duplicate 
# 3. Sum of array 
# 4. Print Even form array 
# 5. Odd print 
# 6. Print array in ascending order 
# 7. Print 2nd last from the array 
# 8. Print larger and smaller from array


arr = [1,2,3,4,5,2,4]

unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

print(unique)


arr = [1,2,3,2,4,5,5,3]
unique = []
dups = []

for x in arr:
    if x in unique and x not in dups:
        print(x)
        dups.append(x)

    else:
        unique.append(x)


arr = [1,2,3,4,5]
total = 0

for x in arr:
    total = total + x

print(total)


arr = [8,4,5,6,2]

for x in arr:
    if x%2==0:
        print(x)


arr = [1,4,5,6,9,23,88]

for x in arr:
    if x%2!=0:
        print(x)


arr = [8,4,6,7,2]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]> arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(arr)


arr = [5,8,9,34,76,89]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]> arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

# print(arr[-2])
print(arr[-1])
print(arr[0])

