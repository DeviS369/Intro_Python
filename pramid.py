
"""
Program 2 : Create a pramid of numbers 1 to 20 using For loop
"""
n = 20
num = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
        if num > n:
            break
    print()  # New line for each level of the pyramid
    if num > n:
        break
