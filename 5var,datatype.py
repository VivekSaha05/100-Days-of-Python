'''
IN PYTHON EVERYTHING IS AN "OBJECT". EVERYTHING MEANS EVERYTHING.
'''

# VARIABLE AND DATA TYPE
'''
VARIABLE is like container. just put data inside container.
DATATYPE is simple types of data that we are going to store in a container.
'''

a = 149  # int type
a2 = 1.1  # float
a3 = complex(8, 2)  # complex
b = "vivek"  # string type
c = True  # boolean type either true or false
d = None  # none

print(a)
print(a2)
print(a3)
print(b)
print(a+a2)

print("the type of a is", type(a))
print("the type of b is", type(b))
print("the type of c is", type(c))
print("the type of d is", type(d))

# Built-in datatypes
'''
1. Numeric data: int, float, complex
int: 3, -8, 0
float: 7.349, -9.0, 0.0000001
complex: 6 + 2i

2. Text data: str
str: "Hello World!!!", "Python Programming"

3. Boolean data:
Boolean data consists of values True or False.

4. Sequenced data: list, tuple
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.
Lists are mutable and can be modified after creation.

Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses.
Tuples are immutable and can not be modified after creation.

5. Mapped data: dict
dict: unordered collection of data containing a key:value pair.
The key:value pairs are enclosed within curly brackets.
'''
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
