def first_decorator(func):
    def wrapper(*args, **kwargs):
        print("First decorator")
        return func(*args, **kwargs)

    return wrapper


def second_decorator(func):
    def wrapper(*args, **kwargs):
        print("Second decorator")
        return func(*args, **kwargs)

    return wrapper


@first_decorator
@second_decorator
def say_hello():
    print("Hello!")


# Calling the function
say_hello()
