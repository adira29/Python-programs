f = open("file.txt")
data = f.read()
print(data)
f.close()

# write in file 

st = "Hey Girl!! you are amazing"

f = open("myfile.txt","w")

f.write(st)
f.close()


f= open("file.txt")

lines = f.readlines()
print(lines, type(lines))
f.close()




st = "Hey Girl!! you are amazing"

f = open("myfile.txt","a")

f.write(st)
f.close()

