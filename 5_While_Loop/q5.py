"""
Ask a start number from user = 6
Ask a end number from the user = 15

6,7,8....,14,15

Ask a start number from user = 15
Ask a end number from the user = 8

8,....,14,15
"""

st = int(input("Enter st number: "))
en = int(input("Enter en number: "))
i = st
j = en
if i < j:
    while i <= j:
        print(i, end=" ")
        i += 1
    print("Loop ends here for st is smaller than en")
else:
    while j <= i:
        print(j, end=" ")
        j += 1
