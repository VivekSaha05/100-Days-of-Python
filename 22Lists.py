# LIST

lst1 = [1,2,3, "Red", "Green", "Blue"]
# index-0 1 2     3      4        5
print(lst1)
print(lst1[1])  # will show 2nd one bcz list starts with 0
print(lst1[-3])  # negative indexing
# = print(lst1[len(lst1)-3])  # same as upper index code
# = print(lst1[6-3]) i.e red is at 3rd position

if 4 in lst1:
    print("yes")
else:
    print("no")
