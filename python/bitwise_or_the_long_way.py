# bitwise 'or' - the long way:
def bitwise_or(x, y):
    x = x[2::]
    y = y[2::]
    new_string = ""
    new_y = ""
    new_x = ""
    if len(x) > len(y):
        new_y = ((len(x) - len(y)) * "0") + y
        new_x = x
    elif len(y) > len(x):
        new_x = ((len(y) - len(x)) * "0") + x
        new_y = y
    else:
        new_x = x
        new_y = y
    newer_x = []
    newer_y = []
    for i in new_y:
        newer_y.append(i)
    for i in new_x:
        newer_x.append(i)
    for i in newer_y:
        if newer_x[int(i) - 1] == "1" or newer_y[int(i) - 1] == "1":
            new_string += "1"
        else:
            new_string += "0"
    new_string = "0b" + new_string
    return new_string

print bitwise_or("0b1110", "0b101")

# bitwise 'or' - the built-in way:
print bin(0b1110 | 0b101)
