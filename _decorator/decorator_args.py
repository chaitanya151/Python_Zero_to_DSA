def decorator_with_args(func):
    def wrapper(*args, **kwargs):  # Accepts any number of arguments
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@decorator_with_args
def add(a, b):
    return a + b


# Calling the function
add(3, 5)
