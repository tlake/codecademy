# bitwise 'or' - the long way:
def bitwise_or(x, y):
    # i don't want the '0b' part of the binary inputs
    x = x[2::]
    y = y[2::]

    # some other defs
    new_string = ""
    new_y = ""
    new_x = ""

    # make sure that both imputs are the same length,
    # then store them in new_x and new_y
    if len(x) > len(y):
        new_y = ((len(x) - len(y)) * "0") + y
        new_x = x
    elif len(y) > len(x):
        new_x = ((len(y) - len(x)) * "0") + x
        new_y = y
    else:
        new_x = x
        new_y = y

    # i'll need these lists for comparing the elements
    newer_x = []
    newer_y = []

    # actually populating those lists
    for i in new_y:
        newer_y.append(int(i))
    for i in new_x:
        newer_x.append(int(i))

    # this is where testing happens
    for i in newer_y:
        if newer_x[i] == 1 or newer_y[i] == 1:
            new_string += "1"
        else:
            new_string += "0"

    # format and return
    new_string = "0b" + new_string
    return new_string

print bitwise_or("0b1110", "0b101")

# bitwise 'or' - the built-in way:
print bin(0b1110 | 0b101)
