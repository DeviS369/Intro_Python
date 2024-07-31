"""
Program 6 : write a program that takes two strings
and returns a longest common substring between them
"""
def longest_common_substring(s1, s2):
    len1, len2 = len(s1), len(s2)
    lcsuff = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    longest_length = 0
    end_index_s1 = 0
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                lcsuff[i][j] = lcsuff[i - 1][j - 1] + 1
                if lcsuff[i][j] > longest_length:
                    longest_length = lcsuff[i][j]
                    end_index_s1 = i - 1
    else:
        lcsuff[i][j] = 0
    if longest_length == 0:
        return ""
    start_index_s1 = end_index_s1 - longest_length + 1
    return s1[start_index_s1:end_index_s1 + 1]
s1 = "GuviGeeks"
s2 = "GeeksForGuvi"
result = longest_common_substring(s1, s2)
print(f"String 1: {s1}")
print(f"String 2: {s2}")
print(f"Longest common substring: {result}")