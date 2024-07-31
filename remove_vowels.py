"""
Program 3 : Write a program that takes a string and returns a new string with the all vowels removed
"""
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ''.join([char for char in s if char not in vowels])
    return result
string = "Guvi Geeks Network Private Network"
new_string = remove_vowels(string)
print(f"Original string: {string}")
print(f"String with vowels removed: {new_string}")