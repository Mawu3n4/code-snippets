
print "nth order:.. ",
u_input = raw_input()

ll_sys = {'0': "01", '1': "10"}
output = "0"
for i in range(int(u_input)):
    result = ""
    print str(i), output
    for char in output:
        result += ll_sys[char]
    output = result
