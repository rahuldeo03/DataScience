# Write a python program that displays a message as follows for a given number:
# If it is a multiple of three, display "Zip".
# If it is a multiple of five, display "Zap".
# If it is a multiple of both three and five, display "Zoom".
# If it does not satisfy any of the above given conditions, display "Invalid".

# Store input number
print("Program to check if a number is divisible by 3 or 5 or both")
try:
    num1 = int(input('Enter the number: '))
    # Implement Logic and print result
    if num1 % 3 == 0:
        if num1 % 5 == 0:
            print("Zoom-multiple of both.")
        else:
            print("Zip-multiple of three.")
    elif num1 % 5 == 0:
        print("Zap-multiple of five.")
    else:
        print("Not divisible by 3 or 5")
except:
    print("Something went wrong")
