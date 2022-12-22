# WHILE LOOPS
# There is no Do-While Loop In Python

for i in range(3):  # for loop
    print(i)

# while Loop
i = int(input("Enter any number less than 5: "))
while i < 5:  # can be used <= if we want n value
    print(i)
    i = i + 1

a = 5
while a > 0:  # Decrementing loop
    print(a)
    a = a - 1  # if + then infinite loop

# Else with While Loop
b = 5
while b > 0:
    print(b)
    b = b - 1
else:
    print("I am inside else")

