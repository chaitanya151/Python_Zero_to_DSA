"""
Ask a start number from the user
Ask a end number from user
end number > start number
"""

# start_number = int(input("Start : "))
# end_number = int(input("End : "))
# while start_number <= end_number:
#     print(start_number, end=" ")
#     start_number += start_number
start_number = int(input("Start : "))
end_number = int(input("End : "))

i = start_number
j = end_number

while i <= j:
    print(i, end=" ")
    i += 1
