my_list = [4, 5, 3, 2, 7, 8, 6, 8, 9, 3]

print(my_list.sort())  # Sorts the list internally. None output. In-place sorting

print(sorted(my_list))
print(my_list)

"""
sort andar hi andar sort karta hai. Sorted nayi sorted list deta hai.
Sorted can be used in the loop. Sort can't because nothing is returned.
If one wants to sort the list by keeping the original list unchanged == SORTED 
"""
