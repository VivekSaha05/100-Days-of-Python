# IF ELSE CONDITION

"""
if, if-else, if-else-elif, nested if-else-elif

Conditional operator :
>, <, <=, >=, ==, != (! =)
"""
a = int(input("Enter a number to check the satisfy:"))
print(a == 18)
print(a > 18)
print(a < 18)
print(a >= 18)
print(a <= 18)
print(a != 18)

# If-else condition
# ex1
age = int(input("Enter Your age:"))
print("Your age is", age)
if age > 18:  # can add age>18 inside ()
    print("you can drive")
elif age >= 18:  # elif condition
    print("Kudos...just passed")
else:
    print("You can't drive")

# ex2
num = int(input("Enter the Number for If-else-elif check:"))
if num < 0:
    print("Number is Negative")
elif num == 0:
    print("Null Value")
elif num == 69:
    print("Special Value")
else:
    print("Number is Positive")

# Nested if Statement (If else under If else.....making tree inside it)

num1 = int(input("Enter Your Number For Nested Check :"))
if num < 0:
    print("Number is Negative.")
elif num > 0:
    if num <= 10:
        print("Number is Less than Or equal to 10")
    elif 10 < num <= 20:
        print("Number is in btw 10-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Null")

