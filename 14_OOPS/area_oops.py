class Rectangle:
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length  # Class variables
        self.breadth = breadth  # Class variable

    def __str__(self) -> str:
        # if we don't have this method in place and print the object we get the address
        # of an object. We use it we get the below output for the print object.
        return f"Length = {self.length} Breadth = {self.breadth}"

    def area(self) -> str | float:
        return f"Area : {self.length * self.breadth}"

    def perimeter(self) -> str | float:
        return f"Perimeter = {2 * (self.length + self.breadth)}"

    def is_square(self) -> bool:
        # return True if self.length == self.breadth else False
        return self.length == self.breadth


r = Rectangle(
    5, 6
)  # __init__ is invoked. Never returns. Assigns, prints but never returns.
ans = r.area()
perimeter = r.perimeter()
check = r.is_square()
print(r)  # prints the __str__ result.
print(ans)
print(perimeter)
print(check)
