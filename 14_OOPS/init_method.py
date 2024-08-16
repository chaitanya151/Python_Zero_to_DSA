class Student:
    # Magic/Dunder Methods
    def __init__(self):
        self.idd = int(input("Enter ID = "))
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.address = "Surat"

    # Methods
    def setDetails(self):
        pass

    def display(self):
        print(f"ID = {self.idd}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Address = {self.address}")


s1 = Student()
print("------------")
s1.display()
# s2 = Student()
# s1.display()
# s2.display()
