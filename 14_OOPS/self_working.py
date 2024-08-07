class Student:
    # Class Variables / Attributes
    idd = 0
    name = ""
    age = 0
    gender = ""

    # Methods
    def display(self):
        print(self)
        print(f"ID = {self.idd}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


s1 = Student()
s2 = Student()
s1.idd = 1
s1.name = "Anirudh"
s1.age = 18
s1.gender = "Male"
print(s1)
s1.display()
s2.display()

# objects that calls the function becomes self.
# self equates to print(s1). First parameter is object.
