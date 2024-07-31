"""
Program 7 : write a program that takes a string and returns the most frequent character in it
"""
def most_frequent_character(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            most_frequent = max(frequency, key=frequency.get)
            return most_frequent
string = "Guvi Geeks Network Private Network"
result = most_frequent_character(string)
print(f"String: {string}")
print(f"Most frequent character: {result}")