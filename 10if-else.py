#if-else statement is also known as decision making statement
'''
if,else,elif 
if is the top branch and else is the end branch where elif is the middle branch between if and else and we can write elif inside a elif which is also known as nested if-else statement
'''


#Correct email- campusx@gmail.com
#Password - 1234

email = input("Apna email bata: ")
if '@' in email:
    pass
    password = input("Apna password bhi bata: ")

    if email == "campusx@gmail.com" and  password == "1234":
        print("Welcome")
        
    elif email == "campusx@gmail.com" and password != "1234":
        print("Password Incorrect")
        password=input("Password firse bol")
        if password == "1234":
            print("Finally correct")
        else:
            print("Still incorrect")
        
    else:
        print("Incorrect credentials")
else:
    print("Email galat hai dhayan do ")