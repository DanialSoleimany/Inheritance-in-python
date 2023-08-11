class Person:
 
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def intro(self):
        print(self.firstname, self.lastname)

class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome to our university ")
        print(self.firstname, self.lastname, self.graduationyear)

s1 = Student("Danial", "Soleimany", 2023)
s1.welcome()
