number_of_classes_held = int(input("number_of_classes_held : "))
number_of_classes_attended = int(input("number_of_classes_attended : "))

percentage_of_class_attended = (
    number_of_classes_attended / number_of_classes_held
) * 100

print(f"percentage_of_class_attended -> {percentage_of_class_attended:.2f}%")

if percentage_of_class_attended < 75:
    print(f"Not allowed to sit in exam.")
else:
    print(f"Allowed to sit in exam.")
