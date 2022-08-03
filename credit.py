# TODO
from cs50 import get_int, get_string
import sys

MINLENGTH = 13
MAXLENGTH = 16

# Prompt for input and check if number is of correct length
ccnumber = get_int("Credit card number: ")
if ccnumber < 3000000000000:
    print("INVALID")
    sys.exit()
if len(str(ccnumber)) < MINLENGTH or len(str(ccnumber)) > MAXLENGTH:
    print("INVALID")
    sys.exit()

# Getting the digits sorted in an array from right to left
digits = [int(x) for x in str(ccnumber)]

# Multiply by 2 every other number starting from the second-to-last and add up the numbers
checksum = 0
for i in range(len(digits) - 2, -1, -2):
    multiply = digits[i] * 2
    checksum = checksum + (multiply % 10) + ((multiply % 100) // 10)

# Adding the ones that were not multiplied
for i in range(len(digits) - 1, -1, -2):
    checksum = checksum + digits[i]

# Check if the last digit of checksum is zero and find credit card brand
if checksum % 10 == 0:
    if digits[0] == 4 and (len(digits) == 13 or len(digits) == 16):
        print("VISA")
    elif digits[0] == 5 and (digits[1] >= 1 and digits[1] <= 5) and len(digits) == 16:
        print("MASTERCARD")
    elif digits[0] == 3 and (digits[1] == 4 or digits[1] == 7) and len(digits) == 15:
        print("AMEX")
    else:
        print("INVALID")
else:
    print("INVALID")