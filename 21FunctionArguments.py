# FUNCTION ARGUMENTS

"""
passing an argument to a function
as a tuple or dictionary
"""

def average(a=2, b=4):  # default argument is 2 and 4 respectively
    print("the avrg is ", (a+b)/2)

# average()  # will take default argument
# average(4)  # value of a=4 and b wil be default
# average(b=10, a=5)  # keyword argument (order will be defined)
# average(4,10)  # required arguments (required if a and b is defined in function without default argument)

