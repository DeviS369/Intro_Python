"""
Program 4 :Write a program that takes a string and returns the number of unique characters in it
"""
def count_unique_characters(s):
    unique_chars = set(s)
    return len(unique_chars)
string = "Guvi Geeks Network Private Network"
unique_char_count = count_unique_characters(string)
print(f"String: {string}")
print(f"Number of unique characters: {unique_char_count}")