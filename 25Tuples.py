#Tuples
'''
1>Create
2>Access
3>Edit
4>Add
5>Delete
6>Operations
7>Functions
'''

# Create
#Empty tuple:
T1 =()
print(T1)

#Homogenous Tuples
T2 =(1,2,3,4,5)
print(T2)

#Heterogenous Tuple
T3 =("Hello",4,5,6)
print(T3)

# 2-D Tuples
T4 =(1,2,3,(4,5))
print(T4)

#If we have to create a tuple of one item
T5=(1)
print(T5)
print(type(T5))

T5 = ("Hello")
print(type(T5))

# How to create a single item in a tuple
T5 = ("Hello",)
print(type(T5))

T6 = tuple("Goa")
print(T6)

T6 =tuple([1,2,3,4,5])
print(T6)
# If we want to create a tuple of a single item then place a comma after the item then that item will be converted into tuple.


# How to Access a item from a tuple:
T2 =(1,2,3,4,5)
print(T2[0])
print(T2[-1])
print(T2[:4])
T3 =("Hello",4,5,6)
print(T3)
T4 =(1,2,3,(4,5))
print(T4)
print(T4[-1][0])
