
roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}

dec = {1: 'I',
       4: 'IV',
       5: 'V',
       9: 'IX',
       10: 'X',
       40: 'XL',
       50: 'L',
       90: 'XC',
       100: 'C',
       400: 'CD',
       500: 'D',
       900: 'CM',
       1000: 'M'}

u_input = raw_input('Enter numeral number: ')

if not set(roman.keys()) >= set(u_input):
    print 'Wrong number, refer to:'
    print roman
else:
    def convert_rom2dec(s):
        return sum([
                roman[num] if roman[num] >= roman[s[i+1]] else -roman[num]
                for i, num in enumerate(s[:-1])], roman[s[-1]])

    def convert_dec2rom(nb):
        res = ''
        for dec2rom in reversed(dec.keys()):
            while nb >= dec2rom:
                res += dec[dec2rom]
                nb -= dec2rom
        return res

    print convert_dec2rom(convert_rom2dec(u_input))
