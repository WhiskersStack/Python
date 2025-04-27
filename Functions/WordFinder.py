#  Longest Word Finder

print("\nLongest Word Finder\n")

str = "The quick brown fox jumps over the lazy dog"

def longest_word(text):
    longest_word = ""
    length = 0
    for word in text.split():
        if len(word) > length:
            length = len(word)
            longest_word = word

    return (longest_word, length)


print("Longest word in the string is: ", longest_word(str)[0])
print("Length of the longest word is: ", longest_word(str)[1])
