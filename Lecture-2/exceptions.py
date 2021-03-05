import sys

try:
    x = int(input("x : "))
    y = int(input("y : "))
except ValueError:
    print("ERROR: Invalid input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("ERROR: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")