# Exercise 3 - Good Morning Sir
# Use Time Module and use If-else-elif

import time

time = int(time.strftime("%H"))  # hour is there only, min and sec can be added
# taking int to make it easy, for 12hr formate use %l
# check condition for time detection

if 5 <= time <= 11:
    print("Its Morning Sir")
elif 12 <= time <= 17:
    print("Good Afternoon Sir")
elif 18 <= time <= 21:
    print("Good Evening Sir")
else:
    print("Good Night Sir.")

