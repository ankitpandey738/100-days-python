# Two main concept in this we are going to learn is Indexing and Slicing.

#Accessing Substrings from a String

#Concept of Indexing:
c="hello"
print(c)

print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])

''' Types of Indexing
1--> Positive Indexing: In this we assume the first index number is positive 
and then move forward by +1 Like in Hello where H index number is 0  E is 1 and so on.
In this index number goes from left to right.

2--> Negative Indexing:In this we go from right to left. Like for Hello H index number
is -5 E is -4 and so on. 
'''


print(c[-1])
print(c[-2])
print(c[-3])
print(c[-4])
print(c[-5])


# Concept of Slicing : The process of extracting multiple Character is known as Slicing.
#In slicing we provide a range. EX:
c = "Hello World"
print(c)

print(c[0:5])

print(c[2:])

print(c[:4])

print(c[:])

print(c)

print(c[2:6:2])

print(c[0:8:3])

print(c[0:6:-1])

print(c[-5:-1:2])

print(c[::-1])

print(c[-1:-5:-1])