# MATCH CASE
# new addition in py 3.10
# same as SWITCH CASE statement in Java and C

x = int(input("Enter the value of x:"))

match x:
    case 0:
        print("case is 0")
    case 1:
        print("case is 1")
    case _ if x != 69:  # _ default if x = 69 then _ value.
        print(x, ",it isn't 69")
    case _:  # _ is used for default value
        print(x, "- kudos for unlocking lv69")

# it doesnt require break like java and c.
