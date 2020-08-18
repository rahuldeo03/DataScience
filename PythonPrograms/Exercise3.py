'''Write a Python program to find the sum of digits of a given number.
    Example: Sum of number 123 will be 6
    Note: Initialize the number with various values and test your program.
'''
# read input number
print("Program to find the sum of digits of a given number")
num1 = int(input('Enter the number: '))
final = 0
rem = 0
while num1 >= 10:
    rem = num1 % 10
    final = final + rem
    num1 = num1 // 10
final = final + num1
print("Sum of integers in the number is :" + str(final))
