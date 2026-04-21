'''
List
1> What is List
1> List vs Array
2> Create
3> Access
4> Edit
5> Add
6> Delete
7> Operations
8> Functions
'''
'''
1> What is List ?
ans> List is a datatype where we way we can store the multiple data.

# Array and List are fundamentally same but there are some important difference are:
    1> Array homogenous : It means the items inside of the array will be of same datatype like if the item is integer then the datatype will be integer and so on
    1> List heterogenous: In this we can have different datatypes inside a single list like it can have integer,boolean,complex and so on
    2> Array me continuous memory allocation pai cheezen store hoti h
    3> Arrays are much faster .
    4> List are more programmer friendly
    
'''


'''
How to create a list?
ans>  Empty list : L = []
      Homogenous list: In this all items will be of same datatype.
                        L =[1,2,3,4,5]
       Heterogenous list: In this different types of list will be together.
                        L2 =["Hello",4,5,6,True,5+6j]
'''


L = []
print(L)

L1 =[1,2,3,4,5]
print(L1)

L2 =["Hello",4,5,6,True,5+6j]
print(L2)

# Multi-dim Lists

# 2D it means in a list there is one more list inside list.
L3 =[1,2,3,[4,5]]
print(L3)

# 3D it means list ke andar list ke andar list

L4 =[[[1,2],[3,4]],[[5,6],[7,8]]]
print(L4)

# We can create a list using a type conversion
L5 = list("Haldia")
print(L5)

L6 =list()
print(L6)

'''
How access a item from a list?
ans> 
'''
L =L1[0]
print(L)

L =L1[-1]
print(L)

L = L1[1:3]
print(L)

L =L1[::-1]
print(L)

# Multi-dim List
l = L3[3]
print(l[0])

l =L3[-1]
print(l[1])

a =L3[-1][0]
print(a)

b =L4[1][1][0]
print(b)

'''
How to edit item in a list?
ans> 
'''
#{1.2.3.4.5} mereko 1 ki jagah 100 chahiye list mai
L1[0]=100 # Lists in python are Mutable
print(L1)
L1[-1]=500 # By negative indexing
print(L1)
L1[1:4] =[200,300,400] #From Slicing
print(L1)

'''
How to add new items in a list?
ans> There are types od add in a list are: 1>append
                                           2>extend
                                           3>insert
'''

E =[100,200,300,400,500]
E.append(1000)
print(E)

E.append("Hello")
print(E)

E.extend([5000,6000,7000])
print(E)
# append and extend both insert the values in the last of the values but append can add a single item at a time but extend can add multiple items at a same time.
E.append([5,6]) #append will always try to append one item.
print(E)

E.extend("goa") #extend will always try to append multiple item.
print(E)

# When we want to add an item on our desired place then we use insert.

E.insert(1,"World")
print(E)

'''
How delete an item from a list?
ans> There are 4 ways to delete an item in a list are: 1> del
                                                       2> remove
                                                       3> pop
                                                       4> clear
'''


F = ["Hii",1,2,False,(4+5j),5,6,44,[5,6],'g','o','a']
'''del F
print(F)'''
del F[0] # It uses the index number to delete the item from the list.
print(F)
del F[-4]
print(F)
del F[-3:]
print(F)


F = ["Hii",1,2,False,(4+5j),5,6,44,[5,6],'g','o','a']
F.remove("Hii") # It uses the Item name to remove the specific item that we want to delete.
print(F)

F.pop() # It removes the last item of the list
print(F)

F.clear()
print(F)

'''
Operations that are available with the list
'''

#Contradiction
A = [1,2,3,4]
B = [5,6,7,8]
c= A+B
print(c)


#Multiplication
c= A*3
print(c)


#Loop works
for i in A:
    print(i)
 
 
#Membership   
D =[1,2,3,[4,5]]
for i in D:
    print(i)
    
E = 4 in D
print(E)
E = [4,5] in D
print(E)


#Functions that are present in list

L = [1,2,3,4]
g =len(L)
print(g)

g1=min(L)
print(g1)

g2=max(L)
print(g2)

g3=sorted(L)
print(g3)

g4=sorted(L,reverse=True)
print(g4)

g5=L.sort()
print(g5)

g6=L.sort(reverse=True)
print(g6)

print(L)
g7 =L.sort()
print(g7)