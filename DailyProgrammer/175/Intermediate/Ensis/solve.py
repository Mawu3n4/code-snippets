import sys
import re

if len(sys.argv) < 3:
    print "Usage: python solve.py 'word word' 'l e t t e r s'"
    exit()

letters = "".join(sorted(sys.argv[2].split(" ")))
msz = 0
out = []

for word in sys.argv[1].split(" "):
    if re.search(".*".join(sorted(word)), letters):
        if len(word) > msz:
            msz = len(word)
            out = []
        if len(word) == msz:
            out.append(word)

print " ".join(out) if out else "No Words Found"
