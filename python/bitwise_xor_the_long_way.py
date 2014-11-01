# xor the long way:
def bitwise_xor(x, y):
    # i don't want the '0b' part of the binary inputs
    x = x[2::]
    y = y[2::]

    # some other defs
    new_string = ""
    new_y = ""
    new_x = ""

    # make sure that both inputs are the same length,
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

    # i'll need these lists for comparing elements
    newer_x = []
    newer_y = []

    # actually populating those lists
    for i in new_y:
        newer_y.append(int(i))
    for i in new_x:
        newer_x.append(int(i))
    print "x: %s, y: %s" % (newer_x, newer_y)


    # this is where testing happens
    for i in range(len(newer_x)):
        print "index %s: x=%s, y=%s" % \
        (i, newer_x[i], newer_y[i])
        
        if \
        newer_x[int(i)] != newer_y[int(i)]:
            print "(above is if condition)"
            new_string += "1"
        else:
            print "(above is else condition)"
            new_string += "0"

    new_string = "0b" + new_string
    return new_string

print bitwise_xor("0b1110", "0b101")

# xor the built-in way:
print bin(0b1110 ^ 0b101)
