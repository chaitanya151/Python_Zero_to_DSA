def create_list(len: int) -> list[int]:
    my_list = []
    for i in range(len):
        x = int(input(f"Enter element {i+1}= "))
        my_list.append(x)
    return my_list


n_list = create_list(5)
print(n_list)
