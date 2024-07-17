"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""

###########Solution_`###################

# for i in range(5, 0, -1):
#     for j in range(5, 0, -1):
#         print(i, end=" ")
#     print()

###########Solution_2###################
for i in range(1, 6):
    for j in range(5, 0, -1):
        print(j, end=" ")
    print()
