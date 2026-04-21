'''
In Python, indentation refers to the spaces (or tabs) at the beginning of a line of code.

Unlike many other programming languages that use { } to define blocks of code, Python uses indentation to define code structure.

🔹 Why Indentation is Important

Indentation tells Python which statements belong to a block of code, such as:

Functions
Loops
Conditional statements
Classes

If indentation is incorrect, Python will raise an IndentationError.
'''
#Example

if True:
    print("This is indented")
    print("This is also indented")
    
print("This is outside the if block")
'''
Here:

The two indented lines belong to the if block.
The last line is outside the block because it is not indented.
'''

'''
🔹 Rules of Indentation
Use 4 spaces per indentation level (standard convention).
Be consistent — do not mix tabs and spaces.
All statements inside the same block must have the same indentation.
'''


#Incorrect Example

1#if True:
#print("Hello")   # ❌ This will cause an error

#This will cause an error because the print statement is not indented.