print(1)
print(2)
print(3)

for i in range(1,6):
    print(i)

# while loops - the block keeps executing until the condition is true 


i = 1

while(i<6):
    print(i)
    i +=1

a = 0
while(a<51):
    print(a)
    a +=1

l = [1,"Harry",False,"This","Rohan","Shubham"]
i =0

while(i<len(l)):
    print(l[i])
    i +=1


# for loop

for i in range(0,4):
    print(i)

l = [1,4,6,234,6,764]
for i in l :
    print(i)

t = (6,231,76,98)

for i in t:
    print(t)

s = "Harry"

for i in s:
    print(i)


l =[1,7,8]

for item in l:
    print(item)

else:
    print("done")


for i in range(100):
    if(i==34):
        break #exit the loop
    print(i)


for i in range(50):
    if(i ==9):
        continue #skip the value
    print(i)


for i in range(7):
    if(i ==4):
        pass #nothing will happen 
    print(i)

