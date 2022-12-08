# Type Casting / Type Conversion
# Method of converting one datatype into another

'''
ex - int(), float(), str(), ord(), hex(),
oct(), tuple(), set(), list(), dict(), etc.

Two Types of Typecasting:
Explicit Conversion (done by the developer)
Implicit Conversion (automatically done by python interpreter, smaller datatype to higher only).
'''

#  Explicit ex1
a = "6"  # string value
# a = 6
b = "9"  # String value
# b = 9

# print(a+b)  # 69 will be the output
print(int(a) + int(b))

# ex2
string = "15"
number = 5
string_num = int(string)  # converting string to int
sum = string_num + number
print("the result is :", sum)

# Implicit Ex1

# a to int
a = 7
# Python automatically converts b to float
b = 3.0
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
