def marks(m1: int | float, m2: int, m3: int, m4: int, m5: int):
    total_marks = m1 + m2 + m3 + m4 + m5
    percentage_marks = (total_marks / 500) * 100
    print(f"sum of marks {total_marks}")
    print(f"percentage of marks {percentage_marks:.2f}")


marks(10.5, 15, m3=20, m4=25, m5=0)
