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

