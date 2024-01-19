

#Function to take two strings from the user 
def fullname(a,b):
    return a+" "+b

#Function that returns every other char in the full_name string
def string_alternative(c):
    return c[::2]

#take input and assigning to variables
First_name = input("first name : ")
last_name = input("last name : ")

#Call fullname function
Full_name= fullname(First_name,last_name)

print("Full Name: "+Full_name)

#Call string_alternative and printing the same
print(string_alternative(Full_name))


