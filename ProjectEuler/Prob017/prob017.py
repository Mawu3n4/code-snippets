

nb = ['one', 'two', 'three', 'four',
      'five', 'six', 'seven', 'eight', 'nine']


teens = len('ten'+'eleven'+'twelve'+'thirteen'+'fourteen'+'fifteen'+
            'sixteen'+'seventeen'+'eighteen'+'nineteen')

tens = len('twenty'+'thirty'+'forty'+'fifty'+
           'sixty'+'seventy'+'eighty'+'ninety')

one_to_ninetynine = (sum(len(n) for n in nb)
                     + teens + (tens*10)
                     + (sum(len(n) for n in nb) * 8))

res = one_ninetynine

for i in range(len(nb)):
    res += len(nb[i]) + len('hundred')
    res += one_ninetynine + (99 * (len(nb[i]) + len('hundred'+'and')))

res += len('one'+'thousand')

print res
