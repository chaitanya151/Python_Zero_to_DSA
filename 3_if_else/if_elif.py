# Ask  a mark from a user
"""
91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
1 - 60 -> E
"""
marks = int(input("Enter marks : "))
if (marks >= 91) and (marks <= 100):
    print("A")
elif (marks >= 81) and (marks <= 90):
    print("B")
elif (marks >= 71) and (marks <= 80):
    print("C")
elif (marks >= 61) and (marks <= 70):
    print("D")
elif (marks >= 1) and (marks <= 60):
    print("E")
else:
    print("Not in range.")
