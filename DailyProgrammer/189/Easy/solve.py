# difficulty = {
#     'easy': 1,
#     'medium' : 2,
#     'hard' : 5
#     }.get(raw_input('Difficulty [EASY|medium|hard] ?: ').lower(), 1)

word = [c for c in raw_input('Enter a word to be guessed: ') if c.isalpha()]

guessed = ['_'] * len(word)

hangman = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '  _________________ ',
    ' /                /|',
    '/________________/ /',
    '_________________|/ ',
    ]

steps = [
    #(xs, xe), (ys, ye), chars
    ((10, 10), (7, 4), '||||'),
    ((10, 10), (3, 1), '|||'),
    ((10, 13), (0, 0), '____'),
    ((14, 18), (0, 0), '_____'),
    ((18, 18), (1, 2), '|@'),
    ((17, 19), (3, 3), '/|\\'),
    ((17, 19), (4, 4), '/ \\')
    ]

def get_letter():
    print ' '.join(guessed)
    return raw_input('Letter ?: ')

def guess(hangman):
    global guessed
    global word
    u_input = get_letter()
    while u_input and u_input[0] in word and '_' in guessed:
        guessed = [ wc if u_input[0] == wc else gc
                    for wc, gc in zip(word, guessed) ]
        word = [ ' ' if u_input[0] == wc else wc
                 for wc in word ]
        print 'Correct guess !'
        if '_' in guessed:
            u_input = get_letter()
    if not '_' in guessed:
        return
    else:
        print 'Wrong guess !'
        print '\n'.join(hangman)

guess(hangman)
for step in steps:
    if '_' in guessed:
        x, xe = step[0]
        y, ye = step[1]
        for char in step[2]:
            hangman[y] = hangman[y][:x-1] + char + hangman[y][x:]
            y += 1*(y < ye) + -1*(y > ye)
            x += 1*(x < xe) + -1*(x > xe)
        guess(hangman)

if '_' in guessed:
    print 'You lost!'
else:
    print 'You won!'
    print ' '.join(guessed)
