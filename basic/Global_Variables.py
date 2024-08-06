# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#new 

# The global Keyword
# Normally, when you create a variable inside a function, 
# that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.
def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is 2 " + x)