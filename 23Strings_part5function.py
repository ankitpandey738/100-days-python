'''
String Function 


There two categories of String Function: 1> Common Functions
                                         2> Fixed Functions


1>Common Functions: These are those function which can be found on all the iterables like on list,set,tuples,dictionary.

2>Fixed Functions: These function are fixed for some specific strings and they cannot be applied on a list,set,dictionary,tuples because they are specific to string data type.
'''


'''
Common function:
                .len
                .max
                .min
                .sorted

'''
c = "kolkata"
print(len(c))
print(max(c))
print(min(c))
print(sorted(c)) # Ascending Order
print(sorted(c,reverse=True)) #For Descending Order


# Fixed Function
'''1.Capitalize/Title/Upper/Lower/Swapcase
   2.Count Function
   3.Find/Index
   4.endswith/startswith
   5.format
   6.isalnum/isalpha/isdecimal/isidentifier
   7.Split
   8.Join
   9.Replace
   10.Strip
'''
# 1 Capitalize/Title/Upper/Lower/Swapcase

#capitalize : It converts the first letter of the string in the capital letters.

c 
print(c) #original string
print(c.capitalize()) #After the use of capitalize function

d = "it is raining today"
print(d)
print(d.capitalize())

# Title: In this however words are there in the sentence it will convert them into capital letters.

print(d.title())

# Upper/Lower

print(d.upper()) #In this every character will be converted into capital letters.
print(d.lower()) #In this every character will be converted into small letters.

#Swapcase  : In this every character of the string will be swapped to the opposite letters like upper letter(Capital) will be converted to lower letter(Small) and lower letter(Small) will be converted to upper letter(Capital).

f = "kolkAtA"
print(f.swapcase())

# 2 Count Function : It tells us the count of the  particular sub-string.

g = "iIt is raining "
print(g.count("i"))

# 3 Find/Index

# Find

h = "it is raining "
print(h.find("x")) # -1 means that sub-string is not present in the string that's why it's output will be in minus.

# Index

#print(h.index(x)) # this is the difference btw Find and Index function in Find it gives us the output in the minus term but in Index output gives us the error.


# 4 endswith/startswith

#endswith

p = "it is raining"
print(p.endswith("ing"))
print(p.endswith("ind"))

#startswith
print(p.startswith("it"))
print(p.startswith("the"))

# 5 format

q = "Hello my name is {} and I am {}"
print(q.format("Ankit",21))


q = "Hello my name is {1} and I am {0}"
print(q.format("Ankit",21))


q = "Hello my name is {name} and I am {age}"
print(q.format(name = "Ankit", age = 21))


q = "Hello my name is {age} and I am {name}"
print(q.format(name = "Ankit", age = 21))


q = "Hello my name is {name} and I am {weight}"
print(q.format(name = "Ankit", age = 21 ,weight = 68 ))


# 6 isalnum/isalpha/isdecimal/isdigit/isidentifier

x = "FLAT20"
print(x.isalnum()) # It checks that the strings has all the thing either alphabetic or numerical.

y = "FLAT"
print(y.isalpha()) # It checks that the strings has all the thing is alphabetic or not

a = "20"
print(a.isdigit()) # It checks that the strings has al the this is digit or not.

b = "hello world"
print(b.isidentifier()) # It checks that in the string there should'nt be any special character.

# 7 Split 
d = "who is the pm of india"
print(d.split())
print(d.split("pm"))
print(d.split("x")) # we cannot perform this specific print because as we can see in the string there

# 8 Join: Join is the reverse of the split function

e = ['who', 'is', 'the', 'pm', 'of', 'india']
print(" ".join(e))
print("/".join(e))
print("-".join(e))

# 9 Replace 
a = "Hi my name is Nitish "
print(a.replace("Nitish","Ankit"))

# 10 Strip
name = "                      ankit"
print("Hi" +name.strip())