#Definition: In a program if you have to do a same work repeatedly then we put that work in a loop.
'''
There are two types of loops in Python:
                                        1-->while
                                        2-->for
'''

#while loop syntax
'''
while(condition){
    code
}
In C,Java and in different laguages

'''

'''
For python

while condition:
    code
'''

#Asking user a number to print the  table of that number

number = int(input("Enter the number: "))

i = 1

while i<11:
    print(number,"*",i,"=",number*i)
    i+=1