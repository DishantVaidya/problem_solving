# Question:
# Given an integer n, print all the numbers from 1 to n as a single continuous string without spaces.
# You are NOT allowed to use any string methods.
#
# Input:
# An integer n.
#
# Output:
# Print the numbers from 1 to n consecutively without spaces.
#
# Example:
# Input: 3
# Output: 123

n = int(input("Enter a number :"))

for i in range(1, n + 1):
    print(i, end='')

#end=' ' removes new line