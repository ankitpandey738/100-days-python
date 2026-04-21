'''
Operations on Strings
>Arithmetic Operations
>Relational Operations
>Logical Operations
>Loops on Strings
>Membership Operations
'''

#Arithmetic Operations
a = "Hello" + "-" + "World"
print(a)

print("*"*50)

print("Hello"*4)

#Relational Operations

b = "Hello" == "World"
print(b)

d = "Hello"  != "World"
print(d)

e = "Mumbai" > "Pune"  #In this comparison is being done in Lexiographically.Means the word which comes first is smaller and whichever comes after is the bigger .
print(e)

f = "Goa" < "Kolkata"
print(f)

g = "kol" <"Kol" #Small letter is smaller than capital letter that's why this relational operation is False.
print(g)

#Logical Operations

a = "hello" and "world"
print(a)

'''
In Python empty strings is always false.
In non-empty strings is always true in Python
"" -->False : Ex of Empty Strings
"worldsf" -->True :Ex of Non-Empty Strings
'''
a = "" and "Hello"
print(a)


b = "" or "world"
print(b)

c= "hello" or "world"
print(c)

d = "hello" and "world"
print(d)

e = not "hello"
print(e)

f = not ""
print(f)

# Loops Operation

c = "Hello World"
for i in c :
    print(i)
    
d = "Hello World"
for i in d[2:7:2] :
    print(i)

    
e = "Hello World"
for i in e[::-1]:
    print(i)
    
# Membership Operation (in ; not-in)

c 
print(c)

f = 'H' in c
print(f)

f = 'h' in c
print(f)

f = 'wprld' in c
print(f)

f = 'World' in c
print(f)