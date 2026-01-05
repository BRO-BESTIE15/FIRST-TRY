print("Hello")
print("Welcome")
print("This is my first simple calculator")

# value input
x = float(input("Enter your first value: "))
y = float(input("Enter your second value: "))

# value dictionary (operations)
m = (x + y)
n = (x - y)
o = (x * y)

# division needs care
if y != 0:
    p = (x / y)
    q = (x // y)
else:
    p = None
    q = None

# operation explanation
print("\nYour first value is:", x)
print("Your second value is:", y)
print("\nOperations are:")
print("a. addition")
print("b. subtraction")
print("c. multiplication")
print("d. division")
print("e. floor division")

do = input("Choose operation (a, b, c, d or e): ")

if do == "a":
    print("Your value is:", m)

elif do == "b":
    print("Your value is:", n)

elif do == "c":
    print("Your value is:", o)

elif do == "d":
    if p is not None:
        print("Your value is:", p)
    else:
        print("Cannot divide by zero")

elif do == "e":
    if q is not None:
        print("Your value is:", q)
    else:
        print("Cannot divide by zero")

else:
    print("Wrong operation chosen")

print("\nThanks for using my first Python calculator")