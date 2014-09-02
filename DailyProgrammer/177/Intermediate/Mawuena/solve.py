import time

try:
    import winsound
except ImportError:
    import os
    def beep(frequency, duration):
        os.system('beep -f %s -l %s' % (frequency, duration))
else:
    def beep(frequency, duration):
        winsound.Beep(frequency, duration)

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
         "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
         "..-", "...-", ".--", "-..-", "-.--", "--.", "-----", ".----", "..---",
         "...--", "....-", ".....", "-....", "--...", "---..", "----."]

morse = [01, 1000, 1010, 100, 0, 0010, 110, 0000, 00, 0111,
         101, 0100, 11, 10, 111, 0110, 1101, 010, 000, 1,
         001, 0001, 011, 1001, 1011, 110, 11111, 01111, 00111,
         00011, 00001, 00000, 10000, 11000, 11100, 11110]

for c in raw_input("Enter a phrase to be coded: "):
    code = ''
    if 'a' <= c.lower() <= 'z':
        code = morse[ord(c.lower()) - ord('a')]
    if not len(code):
        time.sleep(0.6)
    for c_morse in code:
        beep(880, 300 if c_morse == '-' else 100)
        time.sleep(0.2)
    time.sleep(0.4)

