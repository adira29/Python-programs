class Employee:
    language = "Py"
    salary = 1200000

    
    def getInfo(self):
        print(f"The language is {self.language} . The salary is {self.salary}")


harry = Employee()
harry.name = "Harry"
print(harry.language,harry.name,harry.salary)


rohan = Employee()
rohan.name = "Rohan"
print(rohan.salary,rohan.name, rohan.language)


harry.getInfo()