

# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"



# Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

#in this not decalre to data type

a="one"
b=2
c=["1","2","3"]
d=True

print("hey i am a:-",a)
print("hey i am b:-",b)
print("hey i am c",c)
print("hey i am c",d)

#Casting
#If you want to specify the data type of a variable, this can be done with casting.



#here it will convert  number to string
x = str(3)    # x will be '3'


#here it will convert in to int
y = int(3)    # y will be 3
#here it will convert in to float
z = float(3)  # z will be 3.0

print("casting output \n ",x,y,z)


# how to get type in python

print("type of X is :-",type(x))
print("type of Y is :-", type(y))


# Case-Sensitive
# Variable names are case-sensitive.
a=4
A=6
print("case senstive :-",a,A)


# Assign Multiple Values
# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)