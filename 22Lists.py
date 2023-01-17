# LIST

lst1 = [1,2,3, "Red", "Green", "Blue"]
# index-0 1 2     3      4        5
print(lst1)
print(lst1[1])  # will show 2nd one bcz list starts with 0
print(lst1[-3])  # negative indexing
'''NOTE - make the negative index positive first
= print(lst1[len(lst1)-3])  # same as upper index code
= print(lst1[6-3]) i.e red is at 3rd position
'''

if 4 in lst1:  # [if "Red"] can be considered too or/ [if "ed" in "Red"]
    print("yes")
else:
    print("no")

lst2 = [9, 8, 7, 6, "Vivek", "Harry", "Chomu"]
print(lst2)
print(lst2[:])  # prints all
print(lst2[1:])  # will neglate 1st value
print(lst2[:1])  # will only print 1st Value
print(lst2[1:4])  # will print from 2nd to 4th position, neglate 1st and remaining position after 4th
print(lst2[1:-3])  # make it first positive index and upper one will be same
print(lst2[1:4:2])  # will jump by 2 values i.e. 0,2,4,6,8
print(lst2[1:4:3])  # will jump by 3 values

# LIST COMPREHENSION

lst3 = [ in i in range(5)]
print(lst3)