# BREAK AND CONTINUE

# BREAK - enables a prog to skip over a part of the code, terminates the very loop.
# CONTINUE - will terminate the iteration

# for i in range(12):
#     if i == 10:
#         break  # will break the condition after it doesn't satisfy
#     print("5 X", i+1, "=", 5 * (i+1))  # if +1 not given then will start from 0

for i in range(12):
    if i == 10:
        continue  # will skip the given if condition
    print("5 X", i+1, "=", 5 * i+1)
