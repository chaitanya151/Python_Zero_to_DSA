class Student:
    # Class Variables / Attributes
    idd = 0
    name = ""
    age = 0
    gender = ""

    # Methods
    def setDetails(self):
        self.idd = int(input("Enter ID = "))
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")

    def display(self):
        print(f"ID = {self.idd}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


s1 = Student()
s2 = Student()
s1.setDetails()
s1.display()
s2.display()
