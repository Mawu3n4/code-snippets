
# unit: [factor, type]
# type: 0 == mass; 1 == distance
units = {'kilograms': [1000, 0],
         'pounds': [453.592, 0],
         'ounces': [28.3495, 0],
         'hogsheads': [440700, 0],
         'metres': [1, 1],
         'inches': [0.0254, 1],
         'miles': [1609.344, 1],
         'attoparsecs': [0.0308567758, 1]}

# input validity; false while it's invalid
valid = 0

error = "Error: Wrong input: {0}"

while not valid:
    uinput = raw_input().split(' ')

    if not len(uinput) == 3:
        print error.format("not enough arguments")
        print "Expected input: N base_unit dest_unit"
    elif not uinput[1] in units or not uinput[2] in units:
        print error.format("wrong units")
        print "Available units: " + " ".join([x for x in units])
    elif units[uinput[1]][1] != units[uinput[2]][1]:
        print error.format("can't convert between units")
        print "You can convert between: " + " ".join([x for x in units if not units[x][1]])
        print "Or between: " + " ".join([x for x in units if units[x][1]])
    else:
        nb = float(uinput[0])
        src_unit = float(units[uinput[1]][0])
        des_unit = float(units[uinput[2]][0])
        result = nb * src_unit / des_unit
        valid = 1


print " ".join(uinput[:1]), " ".join(["is", str(result), "in", uinput[2]])


