"""
input = 'geekcoders@gmail.com'
output = 'g*********s@gmail.com'
"""


def hide(input: str):

    e_s = ""
    initial = input.split("@")[0]
    domain = input.split("@")[1]
    print(initial)
    print(domain)
    return initial[0] + (len(initial) - 2) * "*" + initial[-1] + "@" + domain


input = "geekcoders@gmail.com"
print(hide(input))
