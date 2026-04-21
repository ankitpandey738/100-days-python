'''
Break,Continue and Pass statement are generally with loop.

Break Statement: If a loop i going and we put a break then it terminates the loop . 
                 Break condition is useful in a Linear Searching

Continue Statement: The continue statement is Python is a loop control statement that skips the rest of the code inside the loop for the current iteration and moves to the next iteration immediately.
                    
Pass Statement: The pass statement in Python is a placeholder that does nothing when executed. It is used to keep code blocks valid where a statement is required but no logic is needed yet.


'''

#Example for br

for i in range(1,11):
    if i == 5:
        break
    print(i)
    
    
#Example of continue

for i in range(1,11):
    if i == 5:
        continue
    print(i)
    print("Hello")
    
    
#Example of pass

for i in range(1,11):
    pass