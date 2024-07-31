"""
Program 9 : write a program that takes a string and returns the number of words in it
"""
def count_words(s):
    words = s.split()
    return len(words)
string = "Guvi Geeks Network Private Network"
word_count = count_words(string)
print(f"String: {string}")
print(f"Number of words: {word_count}")