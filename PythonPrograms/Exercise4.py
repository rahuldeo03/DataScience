#Exercise -4
#Write a python function, find_square() that accepts an integer number, n and returns the square of n. Invoke the function and display the square of the number. 
#Write a python function, find_sum() that accepts an integer, n and returns the sum of first, n numbers. Invoke the function and display the sum of first n numbers.
#Write a python function, find_factorial() that accepts an integer, n and returns the factorial

print('Program to find square, sum of first n numbers and factorial')

def find_square(num1):
    print('Square of ' + str(num1) + ' is ' + str(num1*num1))


def find_sum(num1):
    sum = 0
    i = 0
    for i in range(1, num1+1):
        sum = sum + i
    print('Sum of first ' + str(num1) + ' numbers is : ' + str(sum))

def find_factorial(num1):
    fact = 1
    i = 0
    for i in range(1, num1+1):
        fact = fact*i
    print('Factorial of ' + str(num1) + ' is : ' + str(fact))

num1 = int(input('Enter the number: '))
find_square(num1)
find_sum(num1)
find_factorial(num1)