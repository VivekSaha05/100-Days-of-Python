# LOOPS
"""
There are mainly 2 type of loops:
i. For Loops
ii. While Loops
"""

# FOR LOOP

name = "Vivek"  # for list ["a","b","c"]
for i in name:  # we can write anything in place of i
    print(i, end=", ")  # end="," -> to make it in a horizontal sequence

# RANGE()

for k in range(5):
    print(k)  # if k+1 then 1 -> 5, if not then 0 ->4
#
for k in range(1, 11):  # always make range ending to be +1 to get n-1
    print(k)  # if k then 1 -> 10, if k+1 then 2 -> 11

for k in range(1, 12, 3):  # will take 3 step at a time until it reaches 12 from 1
    print(k)  # 1 -> 4 -> 7 -> 10
