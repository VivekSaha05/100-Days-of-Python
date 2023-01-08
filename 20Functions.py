# FUNCTION
"""
>we are going to make a block of code and then using it later
instead of creating that code again and again later in a shortcut version.
>it will make the code clean and effective if we want to change anything
later on.
ex of built in functions:-
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
"""

# ex:
def calmean(a, b):  # we will call this function
    mean = (a * b) / (a + b)
    print(mean)

def isgreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second Number is greater")

def islesser(a, b):
    pass  # pass = "leave it for now, will complete it later"

a = 54
b = 6
# mean1 = (a*b)/(a+b)
# print(mean1)
calmean(a, b)  # called function
isgreater(a, b)

# again for another value
c = 7
d = 70
# mean2 = (c*d)/(c+d)  # same formula but different variable
# print(mean2)
calmean(c, d)  # called function
isgreater(c, d)
