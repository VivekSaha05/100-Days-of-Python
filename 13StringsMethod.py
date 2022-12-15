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

print(name2.endswith("!"))  # does it end with this "" ? (true or false)

print(name2.endswith("!", 10, 19))  # can give specific location

print(name2.find("a"))  # will find first occurrence

print(name2.index("bhai"))  # same as find but will raise exception if not found

print(name2.isalnum())  # throw true only if string made up of A-Z, a-z, 0-9
# return false as there is !
print(name2.isalpha())  # same as isalnum but not requires 0-9 property

print(name2.islower())  # is every character in lower or not

print(name2.isprintable())  # printable or not, give false if there is \n

print(name2.isspace())  # true if there is empty space

print(name2.istitle())  # check if first letter of each word is capital or not

print(name2.isupper())  # is every character upper or not

print(name2.startswith("op"))


