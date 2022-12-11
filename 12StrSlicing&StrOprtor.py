# STRING SLICING AND OPERATIONS ON STRING

names = "Vivek,Saha"
print(len(names))  # length of the string
print(names[0:4])  # 0 -> 4

fruit = "pineapple"
len1 = len(fruit)
print("Pineapple is a", len1, "letter word.")

# STRING AS AN ARRAY

pie = "AppelPie"
print(pie[:5])  # python will skip 0 automatically
print(pie[6])   # returns character at specified index
print(pie[:])   # will count full length

pie2 = " rassberryPie"
print(pie2[:5])      # Slicing from Start
print(pie2[5:])      # Slicing till End
print(pie2[2:6])     # Slicing in between
print(pie2[-8:])     # Slicing using negative index

# QUICK QUIZ:

nm = "VivekSaha"
print(nm[-4:-2])  # length of nm(9) -4 -> length of nm(9) -2. so 5:7 = 5th to 7th place i.e. Sa
# So "Sa" will be output
