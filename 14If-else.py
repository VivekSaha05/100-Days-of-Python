# IF ELSE CONDITION

"""
if, if-else, if-else-elif, nested if-else-elif

Conditional operator :
>, <, <=, >=, ==, !=
"""
a = int(input("Enter a number to check the satisfy:"))
print(a == 18)
print(a > 18)
print(a < 18)
print(a >= 18)
print(a <= 18)
print(a != 18)

# If-else condition
age = int(input("Enter Your age:"))
print("Your age is", age)
if age > 18:  # can add age>18 inside ()
    print("you can drive")
else:
    print("You can't drive")
