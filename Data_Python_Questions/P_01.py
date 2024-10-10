input_list = [1, 2, [7, 9, [15, [12, 9]], 18, 10]]
# output = [1,2,7,9,15,12,9,18,10]


def flatten_list(input_list: list) -> list:
    l = []
    for num in input_list:
        if type(num) is list:
            l.extend(flatten_list(num))
        else:
            l.append(num)
    return l


print(flatten_list(input_list))
