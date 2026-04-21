# Definition: Whenever we use a loop inside a loop is known as nested loop.
# Time complexity of the nested loop is : n*2 if we use 2 nested loop. 
# n*o . If o=2 means 2 nested loop then n*2.If o=3 means 3 nested loop then n*3.


'''
*
**
***
****
*****
'''
rows = int(input("Enter the number of rows: "))

for i in range(1,rows +1):
    for j in range (0,i):
        print("*",end=" ")
        
    print(" ")
    