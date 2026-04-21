#For Loop
#For loop either iterates on a range function or on a sequence function
'''
General structure of a for loop in C,C++ and java:

for(i=0;i<10;i++){
    code
}
'''

'''
To understand Python for loop we have to understand these two things:

1-->  range function: This is a built-in function in a python its major work it that to generate a integer in a ranger.
2-->  sequence function: Whatever we get in a order is known as a sequence 
                        Example: String,Tuples,Sets,Dictionary
'''

#range
'''
This is not a correct syntax its just to print the range and practice set .
a=list(range(1,11))  #Where 1 is included and 11 is excluded means every time in range whatever range we give it will always include the starting range but it will always stop just before the end of the range .
print(a)

b =  list(range(15))
print(b)

c = list(range(1,11,2))   #1 is the start point 11 is the stop point means it always print less than 11 or whatsoever will be the end or stop point is and 2 is number of steps like if we don't give a step it will be automatically one step like 1,2,3 but if step is given 2 then there will be a gap of 1 digit or step like 1,3,5
print(c)

d = list(range(10,0,-1))
print(d)


#Sequence
#String

"Kolkata"

["kolkata","Delhi","Mumbai"]
'''
#Correct syntax
#Iteration on a range
for i in range(1,11):
    print(i)
    
    
for i in range(1,11,2):
    print(i)
    
for i in range(10,0,-1):
    print(i)
    
for i in "Kolkata":
    print(i)
    
for i in[1,2,3,5]:
    print(i)
    
    
for i in (1,2,3,4):
    print(i)
    
for i in(1,2,3,5):
    print(i)
    
'''
When to use 'while_loop' and 'for_loop':

for_loop: If we know that how many times loop has to execute or has to work.
while_loop : If we don't know how many times loop has to execute or has to work.
'''
