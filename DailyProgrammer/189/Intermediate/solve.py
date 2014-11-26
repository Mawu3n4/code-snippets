
roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}

u_input = raw_input('Enter numeral number: ')

print [roman[x] for x in u_input][:-1]

if not set(roman.keys()) >= set(u_input):
    print 'Wrong number, refer to:'
    print roman
else:
    def convert_rom2dec(s):
        return sum([
                roman[num] if roman[num] >= roman[s[i+1]] else -roman[num]
                for i, num in enumerate(s[:-1])], roman[s[-1]])

    def convert_dec2rom(nb):
        return ""

    print convert_rom2dec(u_input)
