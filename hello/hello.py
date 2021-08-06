# Datatypes
print(type(4))
print(type("Hello"))
print(type(True))
print(type(1.3))

# variables
firstname = "Jess"
lastname = "Mitchell"

douplicateString = "abc"
# sting concatenation
print(firstname + " " + lastname)

print(douplicateString * 2)


# functions with str unser input
first = input("Enter your first name ")
last = input("Please enter your lastname ")


def welcome_user(fname, lname):
    print("Welcome to Python " + fname + lname)


welcome_user(first, last)

# input numbers 
# imputs are always read as string
num1 = input("Enter a number ")
num2 = input("Enter another number ")

sum = int(num1) + int(num2)
print(sum)

# variable in string
age = 1244
user_info = "I am user" + age + "!"

print(user_info)


