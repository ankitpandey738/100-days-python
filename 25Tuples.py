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


#Difference btw List and Tuple is in edit

# Edit  
#List : List is mutable means if a list has been created and we want to edit a item inside the list then we csn do it easily.
L = [1,2,3,4,5]
L[0] = 100
print(L)

#Tuple : Means if a tuple has been created then we cannot edit the item's that is present inside the tuple.
'''
T2
T2[0]=100
print(T2)'''
#Tuple just like strings are immutable.
# We cannot add any new items in the existing tuples because as we know it tuple is immutable.

# Deleting Tuple
'''
T1
del T1
print(T1)
'''
'''
We cannot delete a single item inside a tuple because one item deletion in tuple means overall data is being changed due to this we cannot delete a part of a tuple .
T2
del T2[-1]
print(T2)
'''


# Operations that are same as it is available for list.
T2
T3
T7 = T2+T3
T8= T2*3
print(T7)
print(T8)
for i in T2:
    print(i)
    
L= 1 in T2
print(L)


# Functions are also same as it is available for list.

A = len(T2)
print(A)
b = min(T2)
print(b)
c=max(T2)
print(c)
d = sum(T2)
print(d)
e= sorted(T2)
print(e)
f=sorted(T2,reverse=True)
print(f)

# Tuples are read-only data type but it doesn't have the write ability like a list has the write ability as well as read ability.

