# Operators

'''
Define: Operators are used to perform operations on variables and values.

Python has the following operators:
                                    ->Arithmetic Operators
                                    ->Comparison Operators
                                    ->Logical Operators
                                    ->Bitwise Operators
                                    ->Assignment Operators
                                    ->Identity Operators
                                    ->Membership Operators
'''

#Arithmetic Operators
'''x = 5
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)    #True Division
print(x%y)
print(x**y)
print(x // 2)  #Integer Division

#Comparison Operators/Relational Operators
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x==y)
print(x!=y)

#Logical Operators
x= True
y = False

print(x or y)

print(x and y)

print(not x)

#Bitwise Operators

x = 2
y = 3
print(x & y) 
print(x | y)
print(x >>2)  #Right Shift
print(y <<3)  #Left Shift
print(~x)     #Once's Compliment
'''
'''
Explanation:
              &-->  2 binary is 010.3 binary is 110 | |--->     |
                010                                 | 010       |
                110                                 | 110       |
                -----                               |------     |
                010                                 |110        |
                -----                               |------     |
'''

'''
#Assignment Operators:The process of assigning a value to a variable is known as Assignment Operators
a = 3
print(a)

a+=3  #Actual means is a=a+3
print(a)
a-=3
print(a)
a*=3
print(a)
a &=3
print(a)

#Python doesn't support this : a++ , ++a

#Identity Operator: It checks that the two variable are on the same memory place or not.


#If the variable are on the same place then it is identical because it has same value and stored in a same memory place.
a = 3
b = 3
print(a is b)

a = "Hello"
b = "Hello"
print(a is b)
#It doesn't imply that if they are seeing similar that they might be stored in a same place 
a = [1,2,3]
b = [1,2,3]
print(a is b)

a = "Hello-world"
b = "Hello-world"
print(a is b)
'''

#Membership Operator

x = "Delhi"
print("D" not in x)

x = [1,2,3]
print(1 in x)
