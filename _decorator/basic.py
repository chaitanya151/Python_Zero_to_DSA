def simple_decorator(func):
    def wrapper():  # the wrapper() function runs before and after the original function.
        print("Function is  about to be called.")
        func()
        print("Function has been called")

    return wrapper


@simple_decorator
def say_hello():
    print("Hello")


# function call
say_hello()
