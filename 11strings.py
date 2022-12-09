# Strings

name = "vivek"
friend = "chutiya"
another_friend = 'gandu'
name2 = "my surname is 'saha'"  # "" can be written under single quotes or vice versa
name3 = '''hi guys 
my name is vivek
saha.
'''  # multiline string under '''xyz''' or """xyz"""

print("my name and my friends name are," + name, friend, another_friend)
print(name2)
print(name3)

print(name[0])  # indexing of a string
print(name[3])  # v=0 i=1 v=2 e=3 k=4

# FOR LOOP

print("Using For loop")
for character in name2:
    print(character)
