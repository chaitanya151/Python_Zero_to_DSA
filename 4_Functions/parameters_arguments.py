# def average(num_1: int, num_2: int, num_3: int):
#     add = (num_1 + num_2 + num_3) / 3
#     print(f"addition of 3 numbers -> {add}")


# average(5, 10, 9)  # Arguments


def marks(m1: int, m2: int, m3: int, m4: int, m5: int):
    total_marks = m1 + m2 + m3 + m4 + m5
    percentage_marks = (total_marks / 500) * 100
    print(f"sum of marks {total_marks}")
    print(f"percentage of marks {percentage_marks}")


marks(10, 15, 20, 25, 30)
