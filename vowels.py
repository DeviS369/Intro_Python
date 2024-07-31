"""
Program 1 : Write a python program to calculate total number of vowels
and count of each individual vowels A,E,I,O,U
in the string ' Guvi Geeks Network Private Network
"""
def count_vowels(s):
    s = s.lower()
    vowels = 'aeiou'
    vowel_count = {v: 0 for v in vowels}
    total_vowels = 0
    for char in s:
        if char in vowels:
            vowel_count[char] += 1
    total_vowels += 1
    return total_vowels, vowel_count
string = 'Guvi Geeks Network Private Network'
total_vowels, vowel_count = count_vowels(string)
print(f"Total number of vowels: {total_vowels}")
print("Count of each individual vowel:")
for vowel, count in vowel_count.items():
    print(f"{vowel.upper()}: {count}")