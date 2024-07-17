start = int(input("Number: "))
end = int(input("Number: "))


def total(start, end):
    if start < end:
        total = 0
        for i in range(start, end + 1):
            total = total + i
    return total


def div_by_seven(start, end):
    if start < end:
        total = 0
        for i in range(start, end + 1):
            if i % 7 == 0:
                total = total + i
    return total


# print(total(start, end))
print(div_by_seven(start, end))
