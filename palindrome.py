
"""
Program 5 : Write a program that takes a string and
returns True if it is palindrome , False otherwise
"""

def is_palindrome(s):
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_str == cleaned_str[::-1]
test_string = "A man, a plan, a canal, Panama"
result = is_palindrome(test_string)
print(f"String: {test_string}")
print(f"Is palindrome: {result}")