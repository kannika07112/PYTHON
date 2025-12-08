# Program 10: Custom Exception Example

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative not allowed!")
    print("Square:", num**2)
except NegativeNumberError as e:
    print("Error:", e)
