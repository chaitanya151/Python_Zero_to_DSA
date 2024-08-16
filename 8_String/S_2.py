def upper_str(my_str: str) -> str:
    u_str = ""
    for ch in my_str:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            ascii_code -= 32
            u_str += chr(ascii_code)
        else:
            u_str += ch
    return u_str


print(upper_str("VinLand"))
