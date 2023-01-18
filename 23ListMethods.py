# LIST METHODS

"""
methods to manipulate lists
ex-
list.sort(), reverse(), index(), count(), copy(), append(), insert(), extend()
"""

lst = [1,2,3,4,5,6]
print(lst)

lst.append(7)  # adds 7 in the list
print(lst)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()  # will sort it in ascending order
print(num)
print(num.index(6))  # will print first occurance of that number
num.reverse()  # will reverse it directly
print(num)
num.sort(reverse=True)  # will reverse + sort it in descending order
print(num)
print(num.count(1))  # will count it occurance

# note - by default list is false i.e. is in ascending order. (chota se bada)

colors = ["violet", "indigo", "blue", "green"]
colors2 = ["black", "white"]
newlist = colors.copy()
colors.sort()  # sorted wrt alphabets
print(colors)
print(newlist)
colors.insert(1, "red")  # will insert at position 1
print(colors)
colors.extend(colors2)  # will extend/ merge both list
print(colors)

newcolor = colors + colors2
print(newcolor)