# STRINGS METHOD

"""
Python provides a set of built-in
methods that we can use to alter and modify the strings.
Strings are immutable.
"""

name = "VivekSaha"
print(name.upper())  # uppercase
print(name.lower())  # lowercase

name2 = "!!!!! op bhai !!!!!"
print(name2.rstrip("!"))  # rstrip remove from end only

name3 = "bibek"
print(name3.replace("bibek", "vivek"))  # replace name3 with new name

print(name2.split(" "))  # splits the word inside []

print(name3.capitalize())  # will make 1st letter of word capital

print(name.center(20))  # will add 20 more space in front

print(name2.count("!"))  # will count ! in name2

print(name2.endswith("!"))  # does it end with this "" ?


