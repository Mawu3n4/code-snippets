days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
d = sorted([l.strip() for l in open("windfarm.dat")], key=lambda x: x[:4] + str(days.index(x[5:8])))
r = [7 * [0] for x in range(int(d[-1][:4]) - int(d[0][:4]) + 1)]
for e in d:
    r[int(e[:4]) - int(d[0][:4])][days.index(e[5:8])] += int(e[9:])
print 5 * " " + " | ".join([""] + days) + "\n".join([""] + ["#" + str(y + int(d[0][:4])) + " |" + " |".join(["%4d" % x for x in r[y]]) for y in range(len(r))])
