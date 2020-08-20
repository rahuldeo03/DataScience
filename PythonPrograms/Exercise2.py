'''
Write a Python function to check whether the given year is leap year or not.
Write a Python function to find and display the maximum of three given numbers.
Write a Python function to check the given number is prime number or not.
Write a Python function to print first n Fibonacci numbers.
'''

print("What do you want to do?")
print("1. Find leap year")
print("2. Find highest of 3 numbers")
print("3. Check if a number is Prime or not")
print("4. Print first n Fibonacci numbers")

def leap_year(year):
    if year % 4 == 0:
        print("Year " + str(year) + " is a leap Year")
    else:
        print("Year " + str(year) + " is not a leap year")


def max_number(num1, num2, num3):
    print("The entered numbers are : " + str(num1) + ", " + str(num2) + ", " + str(num3))
    if (num1 > num2) & (num1 > num3):
        print(str(num1) + ' is the highest number')
    elif (num2 > num1) & (num2 > num3):
        print(str(num2) + ' is the Highest number')
    elif (num3 > num1) & (num3 > num2):
        print(str(num3) + ' is the Highest number')
    else:
        print('There is no clear Highest number')


def isPrime(num1):
    prime = 0
    for x in range(2, num1):
        if num1 % x == 0:
            prime = 1
            break
        else:
            continue
    if prime == 0:
        print(str(num1) + " is a prime Number")
    else:
        print(str(num1) + " is not a prime Number")


def fibonacci(num1):
    prev = 0
    curr = 1
    next = 1
    i = 0
    print(str(curr))
    while i < num1:
        next = curr + prev
        print(str(next))
        prev = curr
        curr = next
        i = i+1


option = int(input('Enter the option: '))
if option == 1:
    print('---------------------')
    year = int(input('Enter the year: '))
    leap_year(year)
elif option == 2:
    print('---------------------')
    print("Program to find highest of 3 numbers")
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    max_number(num1, num2, num3)
elif option == 3:
    print('---------------------')
    num1 = int(input('Enter the number to check prime: '))
    isPrime(num1)
elif option == 4:
    print('---------------------')
    num1 = int(input('Enter the number for Fibonacci Series: '))
    fibonacci(num1)