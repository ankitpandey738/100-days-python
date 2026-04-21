# Keyword :
'''
--> Python is a case sensitive programming language

Definition
----> In programming,a keyword is a word that is reserved by a program because the word has a special meaning.
      Keywords can be commands or parameters.
      Every programming language has a set of keywords that cannot be used as variable names. 
'''


# Python has 33 keywords to see them the syntax is this
import keyword
print(keyword.kwlist)
'''Output:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']

--> These are the special word which reserved for the compiler and we cannot use
    these word as a variable and if we use this in compiler then there is a huge 
    chance of getting error.
'''



# Identifiers

'''
Definition

---> A Python identifier is a name used to identify a variable,function,class,module or other object.

Rules for setting Identifiers


--> can only start with an alphabet or _
--> Followed by 0 or more letter,_and digits
--> keywords cannot be used as a identifiers
'''

name = "Ankit"
print(name)

_ = "Ankit"
print(_)

#2 = "Ankit"
#print(2)
'''Error and also special character shows u the error'''

first_name="Ankit"
print(first_name)