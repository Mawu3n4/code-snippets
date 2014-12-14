import sys


with len(sys.argv) >= 2 and open(sys.argv[1]) as f:
    words = set(map(str.strip, f))
    def max_word(word):
        c_subw = 0
        for i in range(len(word)):
            for j in reversed(range(i+2, len(word)+1)):
                if word[i:j] in words:
                    c_subw += 1
        return c_subw
    print max(words, key=max_word)
