""" 
1. Make the flow
2. Calculate the base case
3. optional - look for expection 
example:
suppose,
n = 5 -> 5+4+3+2+1
f(5) -> 5+4+3+2+1
     -> 5+f(4)
f(N) -> N+f(N-1) 

"""


def foo(num):
    if num == 1:  # base case
        return 1
    return num + foo(num - 1)


print(foo(5))
