# LIST METHODS

"""
methods to manipulate lists
"""

lst = [1,2,3,4,5,6]
print(lst)

lst.append(7)  # adds 7 in the list
print(lst)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()  # will sort it in ascending order
print(num)
num.reverse()  # will reverse it directly
print(num)
num.sort(reverse=True)  # will reverse + sort it in descending order
print(num)

# note - by default list is false i.e. is in ascending order. (chota se bada)

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

