"""
Program : 8 write a program that takes a string and
returns True if it anagram of another string ,False otherwise
"""
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)
string1 = "Listen"
string2 = "Silent"
result = are_anagrams(string1, string2)
print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Are anagrams: {result}")